""" Read from return_type and create statement that compatible with @given()"""
# from hypothesis import given
import hypothesis.strategies as st


def create_st(type_data):
    """ Create the compatible kwargs for strategies"""
    if type is None:  # TODO: will be a exception handling here.
        print("There is no type passed in")
    else:
        pass
