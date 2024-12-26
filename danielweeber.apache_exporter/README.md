[![CI](https://github.com/DanielWeeber/ansible-role-apache_exporter/actions/workflows/release.yml/badge.svg?branch=master)](https://github.com/DanielWeeber/ansible-role-apache_exporter/actions/workflows/release.yml)

# Ansible Role: Apache exporter

This role installs Prometheus' [Apache exporter](https://github.com/Lusitaniae/apache_exporter) on Apache hosts.

## Requirements

Setup Status Page of Apache

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    apache_exporter_version: '0.10.1'

The version of Apache exporter to install. Available releases can be found on the [tags](https://github.com/Lusitaniae/apache_exporter/tags) listing in the Apache exporter repository. Drop the `v` off the tag.

If you change the version, the `apache_exporter` binary will be replaced with the updated version, and the service will be restarted.

    apache_exporter_arch: 'amd64'
    apache_exporter_download_url: https://github.com/Lusitaniae/apache_exporter/releases/download/v{{ apache_exporter_version }}/apache_exporter-{{ apache_exporter_version }}-{{ apache_exporter_arch }}.tar.gz

The path where the `apache_exporter` binary will be downloaded and installed from.

    apache_exporter_options: ''

Any additional options to pass to `apache_exporter` when it starts.

    apache_exporter_state: started
    apache_exporter_enabled: true

Controls for the `apache_exporter` service.

## Dependencies

None.

## Example Playbook

    - hosts: all
      roles:
        - role: ansible-role-apache_exporter

## License

MIT / BSD 

## Author Information

This role was created in 2021 by [Daniel Weeber](https://github.com/DanielWeeber). Heavily inspired and forked from [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).