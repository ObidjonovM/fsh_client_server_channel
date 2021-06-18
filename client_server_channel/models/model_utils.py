import psycopg2 as pg2

def get_column_names(conn_info, table_name):
    conn = None
    cur = None
    names_list = None
    names = None

    try:
        conn = pg2.connect(conn_info)
        cur = conn.cursor()
        cur.execute('''
                SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME=%(table_name)s''',
                {'table_name' : table_name})
        names_list = cur.fetchall()

    except pg2.Error as e:
        print(e)
        # TODO: the error needs to be saved to log table

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    if names_list:
        names = tuple(name[0] for name in names_list)

    return names


def keyval_tuples2dict(keys_tuple, vals_tuple):
    return dict(zip(keys_tuple, vals_tuple))


 
