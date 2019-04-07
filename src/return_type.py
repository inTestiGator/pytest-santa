import sqlite3
import json

# TODO: need a function or file to configure the path of database
# TODO: How to parse the value returned by query.

# def make_query(table, module, qualname, limit):
#     raw_query = """
#     SELECT
#         module, qualname, arg_types, return_type, yield_type
#     FROM {table}
#     WHERE
#         module == ?
#     """.format(table=table)
#     values = module
#     if qualname is not None:
#         raw_query += " AND qualname LIKE ? || '%'"
#         values.append(qualname)
#     raw_query += """
#     GROUP BY
#         module, qualname, arg_types, return_type, yield_type
#     ORDER BY date(created_at) DESC
#     LIMIT ?
#     """
#     values.append(limit)
#     return raw_query, values


def return_type_short(function):
    table = "monkeytype_call_traces"
    # there are usually repeated qualname due to being called multiple times
    query = "SELECT DISTINCT arg_types from " + table + " WHERE qualname == " + function
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    row = cur.fetchone()
    dict_row = json.loads(row[0])  # convert the string into dictionary
    print(dict_row.keys())  # return the parameter
    for k, v in dict_row.items():
        print(v['qualname'])  # return the type(qualname) itself
        # for vk, vv in v.items():
        #     print(vv)  # return the type itself
        # print(str(k) + str(v))  # return each parameter and its type
    # print(row[0])
    # return row[0]
    # print(v.values())  # this print out the types, however not only the type itself
    return v['qualname']


if __name__ == '__main__':
    dbFilename = "example/monkeytype.sqlite3"
    conn = sqlite3.connect(dbFilename)
    # return_type("monkeytype_call_traces", "termfrequency")
    return_type_short("\"StopWordManager.is_stop_word\"")
