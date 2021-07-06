from client_server_channel.models import EmployeesTable
from .. import control_utils as utls
from datetime import datetime


class EmployeeC:

    @staticmethod
    def add(emp_info):
        now = datetime.now()
        emp_info['date_added'] = now
        emp_info['date_modified'] = now
        add_result = EmployeesTable.insert(emp_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(emp_id):
        get_result = EmployeesTable.get(emp_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = EmployeesTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(emp_ids):
        name_ids = EmployeesTable.get_fullnames(emp_ids)

        return {
            'success' : name_ids['success'],
            'data' : name_ids['data'],
            'log_code' : utls.record_log(name_ids, 'get_names_by_ids', 'crud_logs')
        }



    @staticmethod
    def update(type_info):
        get_result = EmployeesTable.get(type_info['emp_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            type_info['date_modified'] = datetime.now()
            update_result = EmployeesTable.update(type_info)
            return {
                'success' : update_result['success'],
                'log_code' : utls.record_log(update_result, 'update', 'crud_logs')
            }

        else:
            return {
                'success' : False,
                'log_code' : log_code,
                'comment' : 'DOES NOT EXIST'
            }


    @staticmethod
    def delete(emp_id):
        get_result = EmployeesTable.get(emp_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = EmployeesTable.delete(emp_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }

