from client_server_channel.models import SpOrderStatusTable
from .. import control_utils as utls
from datetime import datetime
from datetime import date


class SpOrderStatusC:

    @staticmethod
    def add(sp_order_status_info):
        now = datetime.now()
        sp_order_status_info['date_added'] = now
        sp_order_status_info['date_modified'] = now
        add_result = SpOrderStatusTable.insert(sp_order_status_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(status_id):
        get_result = SpOrderStatusTable.get(status_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = SpOrderStatusTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = SpOrderStatusTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(sp_order_status_ids):
        names_ids = SpOrderStatusTable.get_names_by_ids(sp_order_status_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(sp_order_status_info):
        get_result = SpOrderStatusTable.get(sp_order_status_info['status_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            sp_order_status_info['date_modified'] = datetime.now()
            update_result = SpOrderStatusTable.update(sp_order_status_info)
            
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
        get_result = SpOrderStatusTable.get(status_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = SpOrderStatusTable.delete(status_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }

