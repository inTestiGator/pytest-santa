""" Example to test the simple add function"""


from hypothesis import given
import hypothesis.strategies as st
from src import util


table = "monkeytype_call_traces"
dbFilename = "example/monkeytype.sqlite3"

type_add_output = get_output_type(
         #function="simpleadd.",
        # module="termfrequency.tf_objectoriented",
     )

# TODO:
# use monkey type to run the example first to create database
# get_output_type
# read_type
# create_st
# use * to pass in the given decorator
# specify how many parameters needed in the test case like below

@given(*stfunc_both())
def test_add(a, b):
    assert add(a, b) == a + b
