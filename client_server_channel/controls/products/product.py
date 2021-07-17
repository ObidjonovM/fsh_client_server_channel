from client_server_channel.models import ProductTable
from .. import control_utils as utls
from datetime import datetime


class ProductC:

    @staticmethod
    def add(product_info):
        now = datetime.now()
        product_info['serial_num'] = ProductTable.generate_serial(
            product_info['product_id']
        )
        product_info['default_login'] = ProductTable.generate_login(8)
        product_info['default_password'] = ProductTable.generate_password(8)
        product_info['resp_emp_id'] = 1
        product_info['date_added'] = now
        product_info['add_emp_id'] = 1
        product_info['date_modified'] = now
        product_info['modify_emp_id'] = 1
        add_result = ProductTable.insert(product_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(serial_num):
        get_result = ProductTable.get(serial_num)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = ProductTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = ProductTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(serial_num_mac_add):
        names_ids = ProductTable.get_names_by_ids(serial_num_mac_add)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(product_info):
        get_result = ProductTable.get(product_info['serial_num'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            product_info['date_modified'] = datetime.now()
            product_info['modify_emp_id'] = 1
            update_result = ProductTable.update(product_info)
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
    def delete(serial_num):
        get_result = ProductTable.get(serial_num)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = ProductTable.delete(serial_num)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }


    
