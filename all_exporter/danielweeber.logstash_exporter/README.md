[![CI](https://github.com/DanielWeeber/ansible-role-logstash_exporter/actions/workflows/release.yml/badge.svg?branch=master)](https://github.com/DanielWeeber/ansible-role-logstash_exporter/actions/workflows/release.yml)

# Ansible Role: Logstash exporter

This role installs Prometheus' [logstash exporter](https://github.com/alxrem/prometheus-logstash-exporter) on logstash hosts.

## Requirements

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    logstash_exporter_version: '0.7.0'

The version of logstash exporter to install. Available releases can be found on the [tags](https://github.com/alxrem/prometheus-logstash-exporter/tags) listing in the logstash exporter repository. Drop the `v` off the tag.

If you change the version, the `logstash_exporter` binary will be replaced with the updated version, and the service will be restarted.

    logstash_exporter_arch: 'amd64'
    logstash_exporter_download_url: https://github.com/alxrem/prometheus-logstash-exporter/releases/download/{{ logstash_exporter_version }}/prometheus-logstash-exporter_{{ logstash_exporter_version }}_linux_{{ logstash_exporter_arch }}

The path where the `logstash_exporter` binary will be downloaded and installed from.

    logstash_exporter_options: ''

Any additional options to pass to `logstash_exporter` when it starts.

    logstash_exporter_state: restarted
    logstash_exporter_enabled: true

Controls for the `logstash_exporter` service.

## Dependencies

None.

## Example Playbook

    - hosts: all
      roles:
        - role: ansible-role-logstash_exporter

## License

MIT / BSD 

## Author Information

This role was created in 2021 by [Daniel Weeber](https://github.com/DanielWeeber). Heavily inspired and forked from [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
