[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](./LICENSE)

# almaops.ct_postgres_exporter

# Install
With command line from Ansible Galaxy:
```
ansible-galaxy install almaops.ct_postgres_exporter
```

With requirements file:
```
~# cat /path/to/your/requirements.yml
# from Ansible Galaxy
- src: almaops.ct_postgres_exporter
# from Git repository
- src: https://github.com/almaops/ansible-role-ct_postgres_exporter.git
  name: almaops.ct_postgres_exporter
~# ansible-galaxy install -r /path/to/your/requirements.yml
```

# Requirements
This role requires Docker Engine installed on target host.

# Role variables
Please refer to [defaults/main.yml](./defaults/main.yml) for full list of available variables. 

# Dependencies
[`almaops.pip_install`](https://galaxy.ansible.com/almaops/pip_install)

# Example playbook
```
- hosts:
    - servers
  become: true
  roles:
    - role: almaops.ct_postgres_exporter
      ct_postgres_exporter_env_data_source_name: "postgresql://postgres:password@localhost:5432/postgres?sslmode=disable"
      ct_postgres_exporter_bind_addr: "192.168.1.10"
```

# License
[MIT](./LICENSE)

# Contributors
[Valentin Gostev](https://github.com/ussrlongbow)
