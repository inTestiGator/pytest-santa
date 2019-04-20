""" Read from return_type and create search strategies that compatible with @given()"""
import hypothesis.strategies as st


def read_type(type_dict):
    """ Read type from the return types and convert into a list"""
    if not type_dict:
        raise Exception("No type given")
    type_list = list(type_dict.values())
    return type_list


def create_st(type_list):
    """ Create the compatible arguments for strategies"""
    st_list = []
    for t in type_list:
        if t == "int":
            st_list.append(st.integers())
        elif t == "str":
            st_list.append(st.text())
        elif t == "float":
            st_list.append(st.floats())
        elif t == "bool":
            st_list.append(st.booleans())
        # TODO: Enable create_st for complex types
        # elif t == "object":
        #     pass
        # elif t == "List":
        #     pass
        # elif t == "Dict":
        #     pass
        # elif t == "Tuple":
        #     pass
        # elif t == "Union":
        #     pass
        # elif t == "Set":
        #     pass
        # elif t == "type":
        #     pass
    return st_list
