""" Read from return_type and create statement that compatible with @given()"""
# from hypothesis import given
import hypothesis.strategies as st


def read_type(type_dict):
    """ Read type from the return types and convert into a list"""
    if type is None:  # TODO: will be a exception handling here.
        print("There is no type passed in")
    else:
        type_list = list(type_dict.values())
    return type_list


def create_st(type_list):
    """ Create the compatible kwargs for strategies"""
    for t in type_list:
        if t == 'int':
            pass
        elif t == 'str':
            pass
        elif t == 'float':
            pass
        elif t == 'bool':
            pass
        elif t == 'byte':
            pass
        elif t == 'object':
            pass
        elif t == 'List':
            pass
        elif t == 'Dict':
            pass
        elif t == 'Tuple':
            pass
        elif t == 'Union':
            pass
        elif t == 'Set':
            pass
        elif t == 'type':
            pass


if __name__ == '__main__':
    input_type = {"var" : "int", "boo" : "int"}
    output = read_type(input_type)
    assert output == ['int', 'int']
