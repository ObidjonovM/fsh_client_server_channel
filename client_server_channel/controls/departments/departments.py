from client_server_channel.models import DepartmentsTable
from .. import control_utils as utls
from datetime import datetime


class DepartmentsC:

    @staticmethod
    def add(name, desc):
        now = datetime.now()
        add_result = DepartmentsTable.insert({
            'name' : name,
            'description' : desc,
            'date_added' : now,
            'add_emp_id' : 1,
            'date_modified' : now,
            'modify_emp_id' : 1
        })

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(dept_id):
        get_result = DepartmentsTable.get(dept_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = DepartmentsTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = DepartmentsTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(depts_ids):
        names_ids = DepartmentsTable.get_names_by_ids(depts_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(dept_info):
        get_result = DepartmentsTable.get(dept_info['dept_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            dept_info['date_modified'] = datetime.now()
            dept_info['modify_emp_id'] = 1
            update_result = DepartmentsTable.update(dept_info)
            return {
                'success' : update_result['success'],
                'log_code' : utls.record_log(update_result, 'update', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }


    @staticmethod
    def delete(dept_id):
        get_result = DepartmentsTable.get(dept_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = DepartmentsTable.delete(dept_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }

