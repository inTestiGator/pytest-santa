# pytest-santa

[![Build Status](https://travis-ci.com/inTestiGator/pytest-santa.svg?branch=master)](https://travis-ci.com/inTestiGator/pytest-santa)
[![codecov](https://codecov.io/gh/inTestiGator/pytest-santa/branch/master/graph/badge.svg)](https://codecov.io/gh/inTestiGator/pytest-santa)

[pytest-santa](https://intestigator.github.io/pytest-santa/) is a plugin that
collects function argument types using
[MonkeyType](https://github.com/Instagram/MonkeyType) and then generates test
data by [Hypothesis](https://hypothesis.works/) and
[hypothesis-jsonschema](https://github.com/Zac-HD/hypothesis-jsonschema).

## Commands

- If needed, install and upgrade the `pipenv` command: `pip install pipenv --user`
- Install the development dependencies `pipenv` command: `pipenv install --dev`
- To run test for the `src`:
`pipenv run pytest tests`
- To run test for the example:
`pipenv run pytest example/tests`


## Monkeytype

To create traceback database with monkeytype:

```
pipenv run monkeytype run <myscript.py>
```

Optional commands to apply the types to the code

```
pipenv run monkeytype stub <module>
pipenv run monkeytype apply <module>
```
