from .. import crud
from .. import model_utils as utls


class EmployeesTable:

    @staticmethod
    def insert(emp_info):
        return crud.insert('employees', emp_info)


    @staticmethod
    def get(emp_id):
        return crud.get('employees', {'emp_id' : emp_id})


    @staticmethod
    def get_all():
        col_names = utls.get_column_names('employees')
        sql = 'SELECT * FROM employees WHERE active = TRUE AND emp_id != 1 ORDER BY emp_id'

        return crud.run_SQL(sql, col_names)


    @staticmethod
    def get_ids_names():
        sql = 'SELECT emp_id, last_name, first_name, middle_name FROM employees '
        sql += 'WHERE active = TRUE AND emp_id != 1 ORDER BY emp_id'
        
        return crud.run_SQL(sql, ['emp_id', 'last_name', 'first_name', 'middle_name'])


    @staticmethod
    def get_fullnames(emp_ids):
        result = crud.get_columns_by_ids(
            'employees', 
            ['emp_id', 'first_name', 'middle_name', 'last_name'], 
            'emp_id', emp_ids
        )

        if len(result['data']) > 0:
            names_ids = {}
            data = result['data']
            data_len = len(data['emp_id'])
            for i in range(data_len):
                names_ids[data['emp_id'][i]] = f"{data['last_name'][i]} {data['first_name'][i]} {data['middle_name'][i]}"

            result['data'] = names_ids
        
        return result


    @staticmethod
    def update(emp_info):
        return crud.update('employees', emp_info, 'emp_id')


    @staticmethod
    def delete(emp_id):
        return crud.delete('employees', {'emp_id' : emp_id})


    @staticmethod
    def login(username, password):
        return crud.get_records('employees', {'username' : username})


    @staticmethod
    def update_lastsignin(emp_info, signin_time):
        emp_info['last_sign_in'] = signin_time
        return crud.update('employees', emp_info, 'emp_id')        


    @staticmethod
    def change_password(emp_info, new_password):
        emp_info['password'] = new_password
        return crud.update('employees', emp_info, 'emp_id')