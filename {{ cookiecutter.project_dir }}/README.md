# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Usage

```shell
ansible-galaxy install {{ cookiecutter.git_username }}.{{ cookiecutter.project_slug }}
```
{%- if cookiecutter.open_source_license != "Not open source" %}

License: {{cookiecutter.open_source_license}} {%- endif %}

