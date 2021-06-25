from .. import model_utils as utls


class EmployeesTypeTable:

    @staticmethod
    def insert_type(type_info):
        sql = '''
		INSERT INTO employee_type 
                (emp_type_name, description, date_added, date_modified)
                VALUES (%(emp_type_name)s, %(description)s, %(date_added)s, %(date_modified)s)
              '''

        query_params = {
            'sql' : sql,
            'sql_params' : type_info,
            'fetchable' : False
        }

        return utls.execute_query(query_params)


    @staticmethod
    def get_type_info(type_id):
        col_names = utls.get_column_names('employee_type')
        sql = '''SELECT * FROM employee_type WHERE emp_type_id=%(type_id)s'''

        query_params = {
            'sql' : sql,
            'sql_params' : {'type_id' : type_id},
            'fetchable' : True
        }

        result = utls.execute_query(query_params)
        if result['success'] and len(result['data']) > 0:
            result['data'] =  utls.keyval_tuples2dict(col_names, result['data'][0]) 
             
        return result   


    @staticmethod
    def get_type_info_all():
        col_names = utls.get_column_names('employee_type')
        sql = '''SELECT * FROM employee_type'''

        query_params = {
            'sql' : sql,
            'sql_params' : None,
            'fetchable' : True
        }

        result = utls.execute_query(query_params)
        if result['success']:
            result['data'] = utls.list_tuples2tuple_lists(result['data'])
            result['data'] =  utls.keyval_tuples2dict(col_names, result['data'])

        return result


    @staticmethod
    def update_type_info(type_info):
        sql = '''
		UPDATE employee_type SET
                        description = %(description)s,
                        date_modified = %(date_modified)s
                WHERE emp_type_id = %(emp_type_id)s 
              '''

        query_params = {
            'sql' : sql,
            'sql_params' : type_info,
            'fetchable' : False
        }

        return utls.execute_query(query_params)


    @staticmethod
    def delete_type(type_id):
        sql = '''
                DELETE FROM employee_type WHERE emp_type_id = %(type_id)s 
              '''

        query_params = {
            'sql' : sql,
            'sql_params' : {'type_id' : type_id},
            'fetchable' : False
        }

        return utls.execute_query(query_params)
