Ansible Role: postgres exporter
=========

[![CI](https://github.com/Puller23/ansible-role-postgres_exporter/actions/workflows/ci.yml/badge.svg)](https://github.com/Puller23/ansible-role-postgres_exporter/actions/workflows/ci.yml)

Deploy prometheus [postgres exporter](https://github.com/prometheus-community/postgres_exporter) using ansible.

Requirements
------------

- Ansible >= 2.7

Role Variables
--------------

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) and are listed in the table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `postgres_exporter_version` | 0.9.0 | Postgres exporter package version.|
| `postgres_exporter_install_dir` | "" | Allows to use local packages instead of ones distributed on github.|
| `postgres_exporter_web_listen_adress` | "0.0.0.0:9187" | Address on which postgres exporter will listen |
| `postgres_exporter_web_telemetry_path` | "metrics" | Path under which to expose metrics |
| `postgres_exporter_db_ip` | "localhost" | IP Address of the postgres instance |
| `postgres_exporter_db_port` | 5432 | Port of the postgres instance |
| `postgres_exporter_db_password` | "" | Password of the postgres instance |
| `postgres_exporter_system_user` | "postgres" | User for systemd service |
| `postgres_exporter_system_group` | "postgres" | User for systemd service |


Dependencies
------------

none

Example Playbook
----------------

Use it in a playbook as follows:
```yaml
- hosts: all
  roles:
    - puller23.postgres_exporter
```

License
-------

MIT

Author Information
------------------

This role was created in 2021 by Gregor Bartels.