from client_server_channel.models import ShippingTypeTable
from .. import control_utils as utls
from datetime import datetime


class ShippingTypeC:

    @staticmethod
    def add(shipp_type_info):
        now = datetime.now()
        shipp_type_info['date_added'] = now,
        shipp_type_info['date_modified'] = now,
        add_result = ShippingTypeTable.insert(shipp_type_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(shipping_type_id):
        get_result = ShippingTypeTable.get(shipping_type_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = ShippingTypeTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = ShippingTypeTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(shipp_types_ids):
        names_ids = ShippingTypeTable.get_names_by_ids(shipp_types_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(shipp_type_info):
        get_result = ShippingTypeTable.get(shipp_type_info['shipping_type_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            shipp_type_info['date_modified'] = datetime.now()
            update_result = ShippingTypeTable.update(shipp_type_info)
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
    def delete(shipping_type_id):
        get_result = ShippingTypeTable.get(shipping_type_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = ShippingTypeTable.delete(shipping_type_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'НЕ СУЩЕСТВУЕТ'
        }

