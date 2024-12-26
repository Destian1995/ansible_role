Ansible Role: redis exporter
=========

Deploy prometheus [redis exporter](https://https://github.com/oliver006/redis_exporter) using ansible.

Requirements
------------

- Ansible >= 2.7

Role Variables
--------------

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) and are listed in the table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `redis_exporter_version` | 1.20.0 | Redis exporter package version. Also accepts latest as parameter. |
| `redis_exporter_install_dir` | "" | Allows to use local packages instead of ones distributed on github.|
| `redis_exporter_web_listen_adress` | "0.0.0.0:9312" | Address on which redis exporter will listen |
| `redis_exporter_system_user` | "0.0.0.0:9312" | Address on which redis exporter will listen |
| `redis_exporter_system_group` | "0.0.0.0:9312" | Address on which redis exporter will listen |
| `redis_exporter_web_telemetry_path` | "metrics" | Path under which to expose metrics |
| `redis_exporter_redis_ip` | "localhost" | IP Address of the Redis instance |
| `redis_exporter_redis_port` | 6379 | Port of the Redis instance |
| `redis_exporter_redis_password` | "" | Password of the Redis instance |
| `redis_exporter_system_user` | "redis-exp" | User for systemd service |
| `redis_exporter_system_group` | "redis-exp" | User for systemd service |


Dependencies
------------

none

Example Playbook
----------------

Use it in a playbook as follows:
```yaml
- hosts: all
  roles:
    - puller23.redis_exporter
```

License
-------

BSD

Author Information
------------------

This role was created in 2021 by Gregor Bartels.