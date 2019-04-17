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

## Monkeytype

To create traceback database with monkeytype first you need to be in the example
directory by using: `cd example`

Then run the following:

```
pipenv run monkeytype run termfrequency/runtermfreq.py inputs/input.txt
```

Optional commands to apply the types to the code:

```
pipenv run monkeytype stub termfrequency.tf_objectoriented
pipenv run monkeytype apply termfrequency.tf_objectoriented
```

To learn more about MonkeyType please go to [MonkeyType](https://github.com/Instagram/MonkeyType) via this link.
