import sqlite3

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
    query = "SELECT arg_types from " + table + " WHERE qualname == " + function
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    # print the first row
    print(rows[0])
    return rows[0]


if __name__ == '__main__':
    dbFilename = "example/termfrequency/monkeytype.sqlite3"
    conn = sqlite3.connect(dbFilename)
    # return_type("monkeytype_call_traces", "termfrequency")
    return_type_short("\"StopWordManager.is_stop_word\"")
