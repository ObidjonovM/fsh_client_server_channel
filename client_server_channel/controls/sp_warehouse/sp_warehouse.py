from client_server_channel.models import SpWarehouseTable
from .. import control_utils as utls
from datetime import datetime
from datetime import date


class SpWarehouseC:

    @staticmethod
    def add(sp_warehouse_info):
        now = datetime.now()
        sp_warehouse_info['date_accepted'] = now,
        if sp_warehouse_info['used_emp_id']:
            sp_warehouse_info['date_used'] = now,

        add_result = SpWarehouseTable.insert(sp_warehouse_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(sp_id):
        get_result = SpWarehouseTable.get(sp_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = SpWarehouseTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def update(sp_warehouse_info):
        get_result = SpWarehouseTable.get(sp_warehouse_info['sp_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            if str(sp_warehouse_info['used_emp_id']) != str(get_result['data']['used_emp_id']):
                sp_warehouse_info['date_used'] = datetime.now()
                
            update_result = SpWarehouseTable.update(sp_warehouse_info)
            
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
    def delete(sp_id):
        get_result = SpWarehouseTable.get(sp_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = SpWarehouseTable.delete(sp_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'НЕ СУЩЕСТВУЕТ'
        }

