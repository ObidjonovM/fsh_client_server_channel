from .. import model_utils as utls


class EmployeesTable:

    @staticmethod
    def insert(emp_info):
        sql = '''
            INSERT INTO employees 
            (emp_type_id, first_name, middle_name, last_name, 
            birth_date, address_1, address_2, city, country, 
            zipcode, phone, email, last_sign_in, date_added, date_modified)
            VALUES 
            (%(emp_type_id)s, %(first_name)s, %(middle_name)s, %(last_name)s,
            %(birth_date)s, %(address_1)s, %(address_2)s, %(city)s, %(country)s,
            %(zipcode)s, %(phone)s, %(email)s, %(last_sign_in)s, %(date_added)s, %(date_modified)s)
            '''

        query_params = {
            'sql': sql,
            'sql_params': emp_info,
            'fetchable': False
        }

        return utls.execute_query(query_params)


    @staticmethod
    def get(emp_id):
        col_names = utls.get_column_names('employees')
        sql = '''SELECT * FROM employees WHERE emp_id=%(emp_id)s'''

        query_params = {
            'sql': sql,
            'sql_params': {'emp_id': emp_id},
            'fetchable': True
        }

        result = utls.execute_query(query_params)
        if result['success'] and len(result['data']) > 0:
            result['data'] = utls.keyval_tuples2dict(
                col_names, result['data'][0])

        return result

    @staticmethod
    def get_all():
        col_names = utls.get_column_names('employees')
        sql = '''SELECT * FROM employees'''

        query_params = {
            'sql': sql,
            'sql_params': None,
            'fetchable': True
        }

        result = utls.execute_query(query_params)
        if result['success']:
            result['data'] = utls.list_tuples2tuple_lists(result['data'])
            result['data'] = utls.keyval_tuples2dict(col_names, result['data'])

        return result


    @staticmethod
    def update(emp_info):
        sql = '''
        UPDATE employees SET 
                        emp_type_id = %(emp_type_id)s,
                        first_name = %(first_name)s,
                        middle_name = %(middle_name)s,
                        last_name = %(last_name)s,
                        birth_date = %(birth_date)s,
                        address_1 = %(address_1)s,
                        address_2 = %(address_2)s,
                        city = %(city)s,
                        country = %(country)s,
                        zipcode = %(zipcode)s,
                        phone = %(phone)s,
                        email = %(email)s,
                        last_sign_in = %(last_sign_in)s,
                        date_modified = %(date_modified)s
                WHERE emp_id = %(emp_id)s
            '''

        query_params = {
            'sql': sql,
            'sql_params': emp_info,
            'fetchable': False
        }

        return utls.execute_query(query_params)


    @staticmethod
    def delete(emp_id):
        sql = '''DELETE FROM employees WHERE emp_id = %(emp_id)s'''

        query_params = {
            'sql': sql,
            'sql_params': {'emp_id': emp_id},
            'fetchable': False
        }

        return utls.execute_query(query_params)
