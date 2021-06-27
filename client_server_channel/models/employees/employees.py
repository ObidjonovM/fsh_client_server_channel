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
    def update(emp_info):
        return crud.update('employees', emp_info, 'emp_id')


    @staticmethod
    def delete(emp_id):
        return crud.delete('employees', {'emp_id' : emp_id})


