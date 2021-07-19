from client_server_channel.models import ProductStatusTable
from .. import control_utils as utls
from datetime import datetime


class ProductStatusC:

    @staticmethod
    def add(status_info):
        now = datetime.now()
        status_info['date_added'] = now
        status_info['add_emp_id'] = 1
        status_info['date_modified'] = now
        status_info['modify_emp_id'] = 1
        add_result = ProductStatusTable.insert(status_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(status_id):
        get_result = ProductStatusTable.get(status_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = ProductStatusTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = ProductStatusTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(dealers_ids):
        names_ids = ProductStatusTable.get_names_by_ids(dealers_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(status_info):
        get_result = ProductStatusTable.get(status_info['status_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            status_info['date_modified'] = datetime.now()
            status_info['modify_emp_id'] = 1
            update_result = ProductStatusTable.update(status_info)
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
    def delete(status_id):
        get_result = ProductStatusTable.get(status_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = ProductStatusTable.delete(status_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }
