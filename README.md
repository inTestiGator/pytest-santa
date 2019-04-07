# pytest-santa

[![Build Status](https://travis-ci.com/inTestiGator/pytest-santa.svg?branch=master)](https://travis-ci.com/inTestiGator/pytest-santa)
[![codecov](https://codecov.io/gh/inTestiGator/pytest-santa/branch/master/graph/badge.svg)](https://codecov.io/gh/inTestiGator/pytest-santa)

This plugin collects function argument types using
[MonkeyType](https://github.com/Instagram/MonkeyType) and then generates test
data by using [Hypothesis](https://hypothesis.works/) and
[hypothesis-jsonschema](https://github.com/Zac-HD/hypothesis-jsonschema).

## Commands

- If needed, install and upgrade the `pipenv` command: `pip install pipenv --user`
- Install the development dependencies `pipenv` command: `pipenv install --dev`
- Run the program with `pipenv` and `python3` and a small input, `cd` to example
directory and type the following command in terminal
`pipenv run python3 termfrequency/runtermfreq.py inputs/input.txt`
