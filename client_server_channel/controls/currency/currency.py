from client_server_channel.models import CurrencyTable
from .. import control_utils as utls
from datetime import datetime


class CurrencyC:

    @staticmethod
    def add(curr_info):
        now = datetime.now()
        curr_info['date_added'] = now,
        curr_info['date_modified'] = now,
        add_result = CurrencyTable.insert(curr_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(curr_id):
        get_result = CurrencyTable.get(curr_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = CurrencyTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = CurrencyTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(currs_ids):
        names_ids = CurrencyTable.get_names_by_ids(currs_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def delete(curr_id):
        get_result = CurrencyTable.get(curr_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = CurrencyTable.delete(curr_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'НЕ СУЩЕСТВУЕТ'
        }

