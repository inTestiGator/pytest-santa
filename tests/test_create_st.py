""" Test for create_st """
import pytest
from src import create_strategy
import hypothesis.strategies as st


def test_read_type():
    """ Test if read_type can create list of types correctly from the dict"""
    input_type = {"var": "int", "boo": "int"}
    output = create_strategy.read_type(input_type)
    assert output == ["int", "int"]


def test_read_type_exception_no_type_given():
    """ Test read_type can handle type empty"""
    input_type = {}
    with pytest.raises(Exception) as e:
        create_strategy.read_type(input_type)
    assert str(e.value) == "No type given"


@pytest.mark.parametrize(
    "input_type, expected_output",
    [
        (["int", "int"], [st.integers(), st.integers()]),
        (["int", "int", "str"], [st.integers(), st.integers(), st.text()]),
        (
            ["int", "int", "int", "int", "int"],
            [st.integers(), st.integers(), st.integers(), st.integers(), st.integers()],
        ),
        (["int", "float"], [st.integers(), st.floats()]),
        (["bool", "float"], [st.booleans(), st.floats()]),
    ],
)
def test_create_st(input_type, expected_output):
    """ Test if create_st can create a list of strategy from the given list of types"""
    output = create_strategy.create_st(input_type)
    assert output == expected_output
