from . import model_utils as utls



def insert(table_name, info):
    sql = f'INSERT INTO {table_name} ('
    values = 'VALUES ('
    for key in info.keys():
        sql += key + ', '
        values += f'%({key})s, '

    sql = sql[:-2] + ') ' + values[:-2] + ')'

    return utls.send_to_db(sql, info, False)


def get(table_name, rec_dict):
    col_names = utls.get_column_names(table_name)
    k, v = rec_dict.popitem()
    sql = f'SELECT * FROM {table_name} WHERE {k} = %({k})s'
    result = utls.send_to_db(sql, {k : v}, True)

    if result['success'] and len(result['data']) > 0:
        result['data'] = utls.keyval_tuples2dict(col_names, result['data'][0])

    return result


def get_all(table_name):
	col_names = utls.get_column_names(table_name)
	sql = f'SELECT * FROM {table_name}'
	result = utls.send_to_db(sql, None, True)

	if result['success']:
		result['data'] = utls.list_tuples2tuple_lists(result['data'])
		result['data'] = utls.keyval_tuples2dict(col_names, result['data'])

	return result


def get_ids_names(table_name, id_col, name_col):
    sql = f'SELECT {id_col}, {name_col} FROM {table_name}'
    result = utls.send_to_db(sql, None, True)
    
    if result['success']:
        result['data'] = utls.list_tuples2tuple_lists(result['data'])
        result['data'] = utls.keyval_tuples2dict((id_col, name_col), result['data'])

    return result


def get_other_pairs(table_name, id_col, name_col, id):
    sql = f'SELECT {id_col}, {name_col} FROM {table_name}'
    sql += f' WHERE {id_col} != {id}'
    result = utls.send_to_db(sql, None, True)

    if result['success']:
        result['data'] = utls.list_tuples2tuple_lists(result['data'])
        result['data'] = utls.keyval_tuples2dict((id_col, name_col), result['data'])

    return result


def get_columns_by_ids(table_name, cols, id_name, ids):
    sql = 'SELECT '
    for col in cols:
        sql += str(col) + ', '

    sql = sql[:-2] + f' FROM {str(table_name)} WHERE '

    for id in ids:
        sql += f'{str(id_name)} = {str(id)} OR '

    sql = sql[:-4] + f' ORDER BY {id_name}'

    result = utls.send_to_db(sql, None, True)

    if result['success']:
        result['data'] = utls.list_tuples2tuple_lists(result['data'])
        result['data'] = utls.keyval_tuples2dict(tuple(cols), result['data'])

    return result




def record_exists(table_name, record):
    sql = f'SELECT * FROM {table_name} WHERE '
    for col in record.keys():
        sql += f'{col} = %({col})s AND '
    
    result = utls.send_to_db(sql[:-5], record, True)
    
    if result['success'] and len(result['data']) > 0:
        return True

    return False


def update(table_name, info, prim_col):
	sql = f'UPDATE {table_name} SET '
	for key in info.keys():
		if key != prim_col:
			sql += f'{key} = %({key})s, '

	sql = sql[:-2] + f' WHERE {prim_col} = %({prim_col})s'

	return utls.send_to_db(sql, info, False)


def delete(table_name, rec_dict):
	k, v = rec_dict.popitem()
	sql = f'DELETE FROM {table_name} WHERE {k} = %({k})s'

	return utls.send_to_db(sql, {k : v}, False)


