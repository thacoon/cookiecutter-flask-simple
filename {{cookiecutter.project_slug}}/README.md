LinkList
========

{{cookiecutter.pipeline_status}}
{{cookiecutter.coverage_report}}

## Installation

```bash
$ pip install pip-tools
# Install all base and development requirements via the update helper script.
$ sh requirements/update.sh --upgrade
```

## Contribute

### Upgrade dependencies
```bash
# Easy
# sh requirements/update.sh --upgrade
# Verbose
$ pip-compile --upgrade requirements/base.in
$ pip-compile --upgrade requirements/development.in
$ pip-sync requirements/base.txt requirements/development.txt
```

### Install dependencies
```bash
# Easy
$ sh requirements/update.sh --update
# Verbose if base.txt and development.txt were already created
$ pip-sync requirements/base.txt requirements/development.txt
```

### Code analysis
```bash
$ pylint path/to/your/dir/
$ pylint app/
```

### Tests
```bash
$ python -m unittest 
```

### Test coverage parsing
```bash
TOTAL\s+\d+\s+\d+\s+(\d+)%$
```
