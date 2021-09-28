from client_server_channel.models import SpLogisticTable
from .. import control_utils as utls
from datetime import datetime
from datetime import date


class SpLogisticC:

    @staticmethod
    def add(sp_logistic_info):
        now = datetime.now()
        sp_logistic_info['tr_status_change_date'] = date.today(),
        sp_logistic_info['date_added'] = now,
        sp_logistic_info['date_modified'] = now,
        add_result = SpLogisticTable.insert(sp_logistic_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(shipment_id):
        get_result = SpLogisticTable.get(shipment_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = SpLogisticTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = SpLogisticTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(sp_logistics_ids):
        names_ids = SpLogisticTable.get_names_by_ids(sp_logistics_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(sp_logistic_info):
        get_result = SpLogisticTable.get(sp_logistic_info['shipment_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            sp_logistic_info['date_modified'] = datetime.now()

            if str(get_result['data']['tr_status_id']) != str(sp_logistic_info['tr_status_id']):
                sp_logistic_info['tr_status_change_date'] = date.today()

            update_result = SpLogisticTable.update(sp_logistic_info)
            
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
    def delete(shipment_id):
        get_result = SpLogisticTable.get(shipment_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = SpLogisticTable.delete(shipment_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'НЕ СУЩЕСТВУЕТ'
        }

