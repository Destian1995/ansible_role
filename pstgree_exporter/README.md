# Ansible Роль: Postgres Exporter

Эта роль устанавливает и настраивает Postgres Exporter для мониторинга с помощью Prometheus.

## Требования
- Ansible версии >= 2.9
- Поддерживаемые операционные системы:
  - CentOS 7/8
  - Debian 10/11
  - Ubuntu 16.04/20.04/22.04

## Переменные роли

| Переменная | Значение по умолчанию | Описание |
|------------|-----------------------|----------|
| `postgres_exporter_version` | `0.16.0` | Версия Postgres Exporter, которую необходимо установить. |
| `postgres_exporter_user` | `postgres_exporter` | Пользователь, от имени которого будет запускаться Exporter. |
| `postgres_exporter_group` | `postgres_exporter` | Группа, к которой принадлежит пользователь Exporter. |
| `postgres_exporter_port` | `9187` | Порт, на котором будут доступны метрики. |


