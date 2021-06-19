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


def list_tuples2tuple_lists(list_tuples):
    """
    INPUT: list_tuples - list of tuples where the length of each tuple should be greater than 1.
    RETURNS: It returns tuple where each element of it is a list which contains elements of tuples at the input.
    EXAMPLE:
	input: [(1, 'Azamat', 'Tuychiev', 'programmer'), (2, 'Ganisher', 'Ganiev', 'analitik'), (3, 'Barak', 'Obama', 'stajor')]
        output: ([1,2,3], ['Azamat','Ganisher','Barak'], ['Tuychiev','Ganiev','Obama'], ['programmer','analitik','stajor']) 
    """
    list_of_lists = []
    tuple_len = len(list_tuples[0])
    for _ in range(tuple_len):
        list_of_lists.append([])
    
    for tup in list_tuples:
        for i in range(tuple_len):
            list_of_lists[i].append(tup[i])

    return tuple(list_of_lists)


def execute_query(query_params):
    conn = None
    cur = None
    success = False
    results = None

    try:
        conn = pg2.connect(query_params['conn_info'])
        cur = conn.cursor()
        cur.execute(query_params['sql'], query_params['sql_params'])
        if query_params['fetchable']:
            results = cur.fetchall()
        else:
            conn.commit()
        success = True

    except pg.Error as e:
        if not query_params['fetchable']:
            conn.rollback()
        print(e)
        # TODO: the error needs to be saved to log table

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    if query_params['fetchable']:
        return results

    return success
    

 
