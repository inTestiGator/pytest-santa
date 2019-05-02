""" Example to test the simple add function"""

from hypothesis import given
from src import util
from example_src import simpleadd


util.set_path("monkeytype.sqlite3")


test_st = util.generate_st(
    function="add",
    module="simpleadd",
)


@given(*test_st)
def test_add(a, b):
    """ use tool to test add function """
    print(a)
    print(b)
    assert simpleadd.add(a, b) == a + b
