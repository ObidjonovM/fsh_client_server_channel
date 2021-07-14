from .. import crud


class EmployeesTable:

    @staticmethod
    def insert(emp_info):
        return crud.insert('employees', emp_info)


    @staticmethod
    def get(emp_id):
        return crud.get('employees', {'emp_id' : emp_id})


    @staticmethod
    def get_all():
        return crud.get_all('employees')


    @staticmethod
    def get_fullnames(emp_ids):
        result = crud.get_columns_by_ids(
            'employees', 
            ['emp_id', 'first_name', 'middle_name', 'last_name'], 
            'emp_id', emp_ids
        )

        if result['data'] != []:
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
