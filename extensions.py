#!/usr/bin/env python3
from cookiecutter.utils import simple_filter

@simple_filter
def gen_project_dir(value: str) -> str:
    return '-'.join([s for s in value.lower().split() if s.isalpha()])
