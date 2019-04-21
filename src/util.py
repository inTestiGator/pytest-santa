"""This module returns provides function to return the parameters and types of a
function and read from return_type and create search strategies that
compatible with @given()"""

import sqlite3
import json
import hypothesis.strategies as st

# TODO: need a function or file to configure the path of database
# TODO: can it handle types like List[str]?

table = "monkeytype_call_traces"
dbFilename = "example/monkeytype.sqlite3"  # global for now


def connect_database_query(query):
    """Connects to the database and passes a query"""
    try:
        conn = sqlite3.connect(dbFilename)
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if not row:
            conn.commit()
        return row
    except sqlite3.Error as e:
        print("Database error: %s" % e)
    finally:
        if conn:
            conn.close()


def get_output_type(function, module):
    """Collects all distinct return types found in the database"""
    try:
        query = f'SELECT DISTINCT return_type from {table} \
                WHERE qualname == "{function}" and module == "{module}"'
        row = connect_database_query(query)
        dict_row = json.loads(row[0])  # convert the string into dictionary
        # print(dict_row.keys())  # return the parameter
        types = dict_row["qualname"]
        return types  # return the parameter and its type in a dict type
    except Exception as e:  # pylint: disable=W0703
        print("Exception in _query: %s" % e)


def get_input_type(function, module):
    """The function connects the database and make queries"""
    try:
        query = f'SELECT DISTINCT arg_types from {table} \
                WHERE qualname == "{function}" and module == "{module}"'
        row = connect_database_query(query)
        dict_row = json.loads(row[0])  # convert the string into dictionary
        # print(dict_row.keys())  # return the parameter
        types = {}
        for k, v in dict_row.items():
            types[k] = v["qualname"]
        return types  # return the parameter and its type in a dict type
    except Exception as e:  # pylint: disable=W0703
        print("Exception in _query: %s" % e)


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


# if __name__ == "__main__":
#     types_sorted_output = get_output_type(
#         function="StopWordManager.is_stop_word",
#         module="termfrequency.tf_objectoriented",
#     )
#     print(types_sorted_output)
