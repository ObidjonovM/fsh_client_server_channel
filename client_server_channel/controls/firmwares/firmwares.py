from client_server_channel.models import FirmwaresTable
from .. import control_utils as utls
from datetime import datetime


class FirmwaresC:

    @staticmethod
    def add(firm_info):
        now = datetime.now()
        firm_info['date_added'] = now
        firm_info['add_emp_id'] = 1
        firm_info['date_modified'] = now
        firm_info['modify_emp_id'] = 1
        add_result = FirmwaresTable.insert(firm_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(firm_id):
        get_result = FirmwaresTable.get(firm_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_log')
        }


    @staticmethod
    def get_all():
        get_all_result = FirmwaresTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = FirmwaresTable.get_ids_names()
        
        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(fws_ids):
        names_ids = FirmwaresTable.get_names_by_ids(fws_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(firm_info):
        get_result = FirmwaresTable.get(firm_info['fw_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        
        if get_result['data'] != []:
            firm_info['date_modified'] = datetime.now()
            update_result = FirmwaresTable.update(firm_info)
            
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
    def delete(firm_id):
        get_result = FirmwaresTable.get(firm_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        
        if get_result['data'] != []:
            delete_result = FirmwaresTable.delete(firm_id)
            
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }
