""" Example to test the simple add function"""


from hypothesis import given
import hypothesis.strategies as st
from src import util
import simpleadd


# TODO:
# get_input_type
# read_type
# create_st
# use * to pass in the given decorator
# specify how many parameters needed in the test case like below

util.set_path("monkeytype.sqlite3")


test_st = util.generate_st(
    function="add",
    module="simpleadd",
)


@given(*test_st)
def test_add(a, b):
    """ use tool to test add function """
    assert simpleadd.add(a, b) == a + b
