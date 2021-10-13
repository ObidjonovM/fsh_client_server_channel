from .. import crud
from .. import model_utils as utls


class EmployeeStatusTable:

    @staticmethod
    def insert(status_info):
        return crud.insert('employee_status', status_info)


    @staticmethod
    def get(status_id):
        return crud.get('employee_status', {'status_id' : status_id})


    @staticmethod
    def get_all():
        col_names = utls.get_column_names('employee_status')
        sql = 'SELECT * FROM employee_status WHERE active = TRUE AND status_id != 1 ORDER BY status_id'

        return crud.run_SQL(sql, col_names)


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('employee_status', 'status_id', 'status')


    @staticmethod
    def get_names_by_ids(status_ids):
        result = crud.get_columns_by_ids(
            'employee_status',
            ['status_id', 'status'],
            'status_id',
            status_ids
        )

        if len(result['data']) > 0:
            names_ids = {}
            data = result['data']
            data_len = len(data['status_id'])
            for i in range(data_len):
                names_ids[data['status_id'][i]] = data['status'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(status_info):
        return crud.update('employee_status', status_info, 'status_id')


    @staticmethod
    def delete(status_id):
        return crud.delete('employee_status', {'status_id' : status_id})