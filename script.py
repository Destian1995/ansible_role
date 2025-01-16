#!/usr/bin/env python3
import requests
import sys
import json
from subprocess import check_output, CalledProcessError, STDOUT
import yaml

ip_consul = "172.20.43.250"
CONSUL_API_URL = f"http://{ip_consul}:8500/v1/catalog/nodes"

def fetch_nodes_from_consul():
    try:
        response = requests.get(CONSUL_API_URL)
        response.raise_for_status()
        print(f"Список узлов получен от Consul: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при обращении к API Consul: {e}", file=sys.stderr)
        sys.exit(1)

def get_system_role_and_owner_from_node(node_address):
    try:
        print(f"Попытка получить данные с узла {node_address}")
        
        # Чтение тегов сервиса
        service_json = check_output(['ssh', node_address, 'cat', '/etc/consul.d/service.json'], stderr=STDOUT).decode('utf-8')
        service_data = json.loads(service_json)
        system_role = service_data.get('service', {}).get('tags', [])
        
        # Чтение метаданных узла
        node_meta_json = check_output(['ssh', node_address, 'cat', '/etc/consul.d/node-meta.json'], stderr=STDOUT).decode('utf-8')
        node_meta_data = json.loads(node_meta_json)
        system_owner = node_meta_data.get('node_meta', {}).get('system_owner', 'unknown')

        return system_role, system_owner
    except CalledProcessError as e:
        print(f"Ошибка выполнения команды на узле {node_address}: {e.output.decode('utf-8')}", file=sys.stderr)
        return [], 'unknown'
    except Exception as e:
        print(f"Не удалось получить данные с узла {node_address}: {e}", file=sys.stderr)
        return [], 'unknown'

def get_host_vars(node, node_address):
    try:
        # Получаем дополнительные переменные для хоста
        host_vars = {
            'ansible_host': node_address,
            'ansible_port': 22  # Пример порта SSH, можно изменить по необходимости
        }
        # Добавляем last_updated из метаданных узла
        last_updated = node.get('Meta', {}).get('last_updated', 'unknown')
        if last_updated != 'unknown':
            host_vars['last_updated'] = last_updated
        # Добавляем владельца из метаданных узла
        _, owner = get_system_role_and_owner_from_node(node_address)
        if owner != 'unknown':
            host_vars['owner'] = owner
        return host_vars
    except Exception as e:
        print(f"Не удалось получить переменные для узла {node_address}: {e}", file=sys.stderr)
        return {}

def group_nodes_by_system_role(nodes):
    grouped_by_role = {}
    all_hosts = {}
    for node in nodes:
        if node["Address"] == ip_consul:
            continue
        node_address = node["Address"]
        node_name = node["Node"]
        system_role, _ = get_system_role_and_owner_from_node(node_address)
        host_vars = get_host_vars(node, node_address)
        for role in system_role:
            if role not in grouped_by_role:
                grouped_by_role[role] = []
            grouped_by_role[role].append(node_name)
        all_hosts[node_name] = host_vars
    return grouped_by_role, all_hosts

def generate_inventory_yaml(grouped_by_role, all_hosts):
    inventory = {
        'all': {
            'hosts': {}
        }
    }
    # Добавляем всех узлов в группу all с переменными
    for host, vars in all_hosts.items():
        inventory['all']['hosts'][host] = vars
    # Группировка по ролям
    for role, hosts in grouped_by_role.items():
        if role not in inventory:
            inventory[role] = {'hosts': {}}
        for host in hosts:
            inventory[role]['hosts'][host] = all_hosts[host]
    return inventory

class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

def main():
    nodes = fetch_nodes_from_consul()
    grouped_by_role, all_hosts = group_nodes_by_system_role(nodes)
    # Генерация YAML-формата для инвентаря
    inventory_yaml = generate_inventory_yaml(grouped_by_role, all_hosts)
    # Вывод инвентаря на стандартный вывод в формате YAML без якорей
    print(yaml.dump(inventory_yaml, default_flow_style=False, allow_unicode=True, Dumper=NoAliasDumper))

if __name__ == "__main__":
    main()
