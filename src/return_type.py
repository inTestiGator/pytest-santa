"""This module returns provides function to return the parameters and types of a function"""
import sqlite3
import json

# pylint: disable=W0511
# TODO: need a function or file to configure the path of database
# TODO: can it handle types like List[str]?

table = "monkeytype_call_traces"
dbFilename = "example/monkeytype.sqlite3"  # global for now


def connect_database_query(query):
    """Connect and make query to database"""
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
    """The function connects the database and make queries"""
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


if __name__ == "__main__":
    # types_sorted = get_input_type(function="sort", module="termfrequency.tf_pipeline")
    types_sorted_output = get_output_type(
        function="StopWordManager.is_stop_word",
        module="termfrequency.tf_objectoriented",
    )
    # print(test_return)
    # print(types_sorted)
    print(types_sorted_output)
