from .. import crud


class EmployeesTypeTable:

    @staticmethod
    def insert_type(type_info):
        return crud.insert('employee_type', type_info)


    @staticmethod
    def get_type_info(type_id):
        return crud.get('employee_type', {'emp_type_id' : type_id})


    @staticmethod
    def get_type_info_all():
        return crud.get_all('employee_type')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('employee_type', 'emp_type_id', 'emp_type_name')


    @staticmethod
    def update_type_info(type_info):
        return crud.update('employee_type', type_info, 'emp_type_id')


    @staticmethod
    def delete_type(type_id):
        return crud.delete('employee_type', {'emp_type_id' : type_id})
