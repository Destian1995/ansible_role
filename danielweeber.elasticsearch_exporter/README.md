[![CI](https://github.com/DanielWeeber/ansible-role-elasticsearch_exporter/actions/workflows/release.yml/badge.svg?branch=master)](https://github.com/DanielWeeber/ansible-role-elasticsearch_exporter/actions/workflows/release.yml)

# Ansible Role: Elasticsearch exporter

This role installs Prometheus' [Elasticsearch exporter](https://github.com/prometheus-community/elasticsearch_exporter) on elasticsearch hosts.

## Requirements

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    elasticsearch_exporter_version: '1.3.0'

The version of elasticsearch exporter to install. Available releases can be found on the [tags](https://github.com/prometheus-community/elasticsearch_exporter/tags) listing in the elasticsearch exporter repository. Drop the `v` off the tag.

If you change the version, the `elasticsearch_exporter` binary will be replaced with the updated version, and the service will be restarted.

    elasticsearch_exporter_arch: 'amd64'
    elasticsearch_exporter_download_url: https://github.com/prometheus-community/elasticsearch_exporter/releases/download/v{{ elasticsearch_exporter_version }}/elasticsearch_exporter-{{ elasticsearch_exporter_version }}-{{ elasticsearch_exporter_arch }}.tar.gz

The path where the `elasticsearch_exporter` binary will be downloaded and installed from.

    elasticsearch_exporter_options: ''

Any additional options to pass to `elasticsearch_exporter` when it starts.

    elasticsearch_exporter_state: restarted
    elasticsearch_exporter_enabled: true

Controls for the `elasticsearch_exporter` service.

## Dependencies

None.

## Example Playbook

    - hosts: all
      roles:
        - role: ansible-role-elasticsearch_exporter

## License

MIT / BSD 

## Author Information

This role was created in 2021 by [Daniel Weeber](https://github.com/DanielWeeber). Heavily inspired and forked from [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
