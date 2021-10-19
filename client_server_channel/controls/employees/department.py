from client_server_channel.models import DepartmentTable
from .. import control_utils as utls
from datetime import datetime


class DepartmentC:

    @staticmethod
    def add(dept_info):
        now = datetime.now()
        dept_info['date_added'] = now,
        dept_info['date_modified'] = now,
        add_result = DepartmentTable.insert(dept_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(dept_id):
        if str(dept_id) != '1':
            get_result = DepartmentTable.get(dept_id)

            return {
                'success' : get_result['success'],
                'data' : get_result['data'],
                'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
            }

        return {
            'success' : False,
            'data' : {}
        }


    @staticmethod
    def get_all():
        get_all_result = DepartmentTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = DepartmentTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(depts_ids):
        names_ids = DepartmentTable.get_names_by_ids(depts_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(dept_info):
        if str(dept_info['dept_id']) != '1':
            get_result = DepartmentTable.get(dept_info['dept_id'])
            log_code = utls.record_log(get_result, 'update', 'crud_logs')
            if get_result['data'] != []:
                dept_info['date_modified'] = datetime.now()
                update_result = DepartmentTable.update(dept_info)
                return {
                    'success' : update_result['success'],
                    'log_code' : utls.record_log(update_result, 'update', 'crud_logs')
                }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'НЕ СУЩЕСТВУЕТ'
        }


    @staticmethod
    def delete(dept_id):
        if str(dept_id) != '1':
            get_result = DepartmentTable.get(dept_id)
            log_code = utls.record_log(get_result, 'delete', 'crud_logs')
            if get_result['data'] != []:
                delete_result = DepartmentTable.delete(dept_id)
                return {
                    'success' : delete_result['success'],
                    'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
                }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'НЕ СУЩЕСТВУЕТ'
        }

