import sqlite3

# TODO: Enable the function to find path instead of manually type in path
# TODO: How to parse the value returned by query.
# TODO: How to only return one value in query

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


def return_type(table, module, qualname=None, limit=None):
    raw_query = """
    SELECT
        module, qualname, arg_types, return_type, yield_type
    FROM {table}
    WHERE
        module == ?
    """.format(table=table)
    cur = conn.cursor()
    cur.execute(raw_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def return_type_short(table, function):
    query = "SELECT arg_types from " + table + " WHERE qualname == " + function
    print(query)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    dbFilename = "example/termfrequency/monkeytype.sqlite3"
    conn = sqlite3.connect(dbFilename)
    # return_type("monkeytype_call_traces", "termfrequency")
    return_type_short("monkeytype_call_traces", "\"StopWordManager.is_stop_word\"")
