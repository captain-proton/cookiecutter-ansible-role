# Ansible Cookiecutter Template

Recipe to create an ansible role. 

## Usage

```shell
git clone https://github.com/captain-proton/cookiecutter-ansible-role.git
cookiecutter --directory cookiecutter-ansible-role
```

This role automatically creates the common folders, also created by `ansible-galaxy role init foo` or `molecule init role foo`, when creating a new role. You end up with a structure like this.

```shell
foo
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── molecule
│   └── default
│       ├── converge.yml
│       └── molecule.yml
├── README.md
├── tasks
│   └── main.yml
├── templates
└── vars
    └── main.yml```

# License

MIT
