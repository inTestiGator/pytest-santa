# sample ./setup.py file
from setuptools import setup

setup(
    name="pytest-santa",
    packages=["pytest-santa"],
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["pytest-santa = pytest-santa.pluginmodule"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)
