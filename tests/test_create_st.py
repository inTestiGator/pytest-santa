from src import create_st
import hypothesis.strategies as st
import pytest


def test_read_type():
    input_type = {"var" : "int", "boo" : "int"}
    output = create_st.read_type(input_type)
    assert output == ['int', 'int']


@pytest.mark.parametrize(
    "input_type, expected_output",
    [(['int', 'int'], [st.integers(), st.integers()]),
     (['int', 'int', 'str'], [st.integers(), st.integers(), st.text()]),
     (['int', 'int', 'int', 'int', 'int'],
      [st.integers(), st.integers(), st.integers(), st.integers(), st.integers()]),
     (['int', 'float'], [st.integers(), st.floats()]),
     (['bool', 'float'], [st.booleans(), st.floats()])],
)
def test_create_st(input_type, expected_output):
    output = create_st.create_st(input_type)
    assert output == expected_output
