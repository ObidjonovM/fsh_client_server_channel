from . import model_utils as utls


def last_pk_value(table_name):
	col_names = utls.get_column_names(table_name)
	pk_col = col_names[0]
	sql = f'SELECT COUNT({pk_col}) FROM {table_name}'
	result = utls.send_to_db(sql, None, True)
	if not result['success']:
		return {pk_col : -1}
	
	return {pk_col : result['data'][0][0]}


def insert(table_name, info, generate_pk=True):
    if generate_pk:
        pk, val = last_pk_value(table_name).popitem()       # getting the last value of PK column
        sql = f'INSERT INTO {table_name} ({pk}, '
        values = f'VALUES ({val + 1}, '
    else:
        sql = f'INSERT INTO {table_name} ('
        values = f'VALUES ('

    for key in info.keys():
        sql += key + ', '
        values += f'%({key})s, '

    sql += 'active) '
    values += 'TRUE)'
    sql = sql + values
    return utls.send_to_db(sql, info, False)


def get(table_name, rec_dict):
    col_names = utls.get_column_names(table_name)
    k, v = rec_dict.popitem()
    sql = f'SELECT * FROM {table_name} WHERE {k} = %({k})s AND active = TRUE'
    result = utls.send_to_db(sql, {k : v}, True)

    if result['success'] and len(result['data']) > 0:
        result['data'] = utls.keyval_tuples2dict(col_names, result['data'][0])
        if 'active' in result['data']:
            del result['data']['active']
        if 'date_added' in result['data']:
            del result['data']['date_added']
        if 'date_modified' in result['data']:
            del result['data']['date_modified']
        if 'add_emp_id' in result['data']:
            del result['data']['add_emp_id']
        if 'modify_emp_id' in result['data']:
            del result['data']['modify_emp_id']

    return result


def get_all(table_name):
    col_names = utls.get_column_names(table_name)
    sql = f'SELECT * FROM {table_name} WHERE active = TRUE ORDER BY {col_names[0]}'
    result = utls.send_to_db(sql, None, True)


    if result['success']:
        result['data'] = utls.list_tuples2tuple_lists(result['data'])
        result['data'] = utls.keyval_tuples2dict(col_names, result['data'])
        if 'active' in result['data']:
            del result['data']['active']
        if 'date_added' in result['data']:
            del result['data']['date_added']
        if 'date_modified' in result['data']:
            del result['data']['date_modified']
        if 'add_emp_id' in result['data']:
            del result['data']['add_emp_id']
        if 'modify_emp_id' in result['data']:
            del result['data']['modify_emp_id']

    return result


def get_ids_names(table_name, id_col, name_col):
    sql = f'SELECT {id_col}, {name_col} FROM {table_name} WHERE active = TRUE'
    result = utls.send_to_db(sql, None, True)
    
    if result['success']:
        result['data'] = utls.list_tuples2tuple_lists(result['data'])
        result['data'] = utls.keyval_tuples2dict((id_col, name_col), result['data'])

    return result


def run_SQL(sql, cols, fetchone = False, sql_params=None, fetchable=True):
    result = utls.send_to_db(sql, sql_params, fetchable)

    if result['success']:
        if fetchone:
            result['data'] = utls.keyval_tuples2dict(tuple(cols), result['data'][0])
        else:
            result['data'] = utls.list_tuples2tuple_lists(result['data'])
            result['data'] = utls.keyval_tuples2dict(tuple(cols), result['data'])
        if 'active' in result['data']:
            del result['data']['active']
        if 'date_added' in result['data']:
            del result['data']['date_added']
        if 'date_modified' in result['data']:
            del result['data']['date_modified']
        if 'add_emp_id' in result['data']:
            del result['data']['add_emp_id']
        if 'modify_emp_id' in result['data']:
            del result['data']['modify_emp_id']
    
    return result


def get_columns_by_col_names(table_name, name_cols):
    sql = f'SELECT '
    for name_col in name_cols:
        sql += str(name_col) + ', '

    sql = sql[:-2] + f' FROM {table_name} WHERE active = TRUE'
    result = utls.send_to_db(sql, None, True)

    if result['success']:
        result['data'] = utls.list_tuples2tuple_lists(result['data'])

        result['data'] = utls.keyval_tuples2dict((name_cols), result['data'])

    return result


def get_other_pairs(table_name, id_col, name_col, id):
    sql = f'SELECT {id_col}, {name_col} FROM {table_name}'
    sql += f' WHERE {id_col} != {id} AND active = TRUE'
    result = utls.send_to_db(sql, None, True)

    if result['success']:
        result['data'] = utls.list_tuples2tuple_lists(result['data'])
        result['data'] = utls.keyval_tuples2dict((id_col, name_col), result['data'])

    return result


def get_columns_by_ids(table_name, cols, id_name, ids):
    sql = 'SELECT '
    for col in cols:
        sql += str(col) + ', '

    sql = sql[:-2] + f' FROM {str(table_name)} WHERE active = TRUE AND ('

    for id in ids:
        sql += f"{str(id_name)} = '{str(id)}' OR "

    sql = sql[:-4] + f') ORDER BY {id_name}'

    result = utls.send_to_db(sql, None, True)

    if result['success']:
        result['data'] = utls.list_tuples2tuple_lists(result['data'])
        result['data'] = utls.keyval_tuples2dict(tuple(cols), result['data'])

    return result


def record_exists(table_name, record):
    sql = f'SELECT * FROM {table_name} WHERE '
    for col in record.keys():
        sql += f'{col} = %({col})s AND '
    
    sql += 'active = TRUE '
    result = utls.send_to_db(sql[:-5], record, True)
    
    if result['success'] and len(result['data']) > 0:
        return True

    return False


def get_records(table_name, record, unique=True):
    col_names = utls.get_column_names(table_name)
    k, v = record.popitem()
    sql = f'SELECT * FROM {table_name} WHERE {k} = %({k})s AND active = TRUE'
    result = utls.send_to_db(sql, {k : v}, True)

    if result['success'] and len(result['data']) > 0:
        if unique:
            result['data'] = utls.keyval_tuples2dict(col_names, result['data'][0])
        else:
            result['data'] = utls.list_tuples2tuple_lists(result['data'])
            result['data'] = utls.keyval_tuples2dict(col_names, result['data'])
    
    return result


def update(table_name, info, prim_col):
	sql = f'UPDATE {table_name} SET '
	for key in info.keys():
		if key != prim_col:
			sql += f'{key} = %({key})s, '

	sql = sql[:-2] + f' WHERE {prim_col} = %({prim_col})s AND active =  TRUE'

	return utls.send_to_db(sql, info, False)


def delete(table_name, rec_dict):
	k, v = rec_dict.popitem()
	sql = f'UPDATE {table_name} SET active = FALSE WHERE {k} = %({k})s'
	return utls.send_to_db(sql, {k : v}, False)


