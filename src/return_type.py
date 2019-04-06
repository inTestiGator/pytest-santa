import sqlite3


def make_query(table, module, qualname, limit: int):
    raw_query = """
    SELECT
        module, qualname, arg_types, return_type, yield_type
    FROM {table}
    WHERE
        module == ?
    """.format(table=table)
    values = None
    if qualname is not None:
        raw_query += " AND qualname LIKE ? || '%'"
        values.append(qualname)
    raw_query += """
    GROUP BY
        module, qualname, arg_types, return_type, yield_type
    ORDER BY date(created_at) DESC
    LIMIT ?
    """
    values.append(limit)
    return raw_query, values
