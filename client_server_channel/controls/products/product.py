from client_server_channel.models import ProductTable
from .product_photo import ProductPhotoC
from .. import control_utils as utls
from datetime import datetime
import requests as reqs
import json
from client_server_channel.config import hd_server


class ProductC:

    @staticmethod
    def add(product_info):
        now = datetime.now()
        ap_login_res = ProductTable.generate_ap_login()
        if len(ap_login_res['data']) > 0:
            login = 'FidoElectronics' + str(ap_login_res['data']['ap_login'][0] + 1)
            product_info['ap_login'] = login
            product_info['ap_password'] = ProductTable.generate_ap_password(8)
            product_info['serial_num'] = ProductTable.generate_serial(
                product_info['product_id']
            )
            product_info['default_login'] = ProductTable.generate_login(8)
            product_info['default_password'] = ProductTable.generate_password(8)
            product_info['date_added'] = now
            product_info['date_modified'] = now
            add_result = ProductTable.insert(product_info)

            return {
                'success' : add_result['success'],
                'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
            }

        return {
            'success' : ap_login_res['success'],
            'log_code' : utls.record_log(ap_login_res, 'add', 'crud_logs')
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
    def update(product_info, add_client = False):
        get_result = ProductTable.get(product_info['serial_num'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            product_info['date_modified'] = datetime.now()
            if get_result['data']['client_id'] != None and add_client == True:
                return {
                    'success' : False,
                    'log_code' : 0,
                    'comment' : '<h1>Продукт продан!</h1>'
                }

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


    @staticmethod
    def get_my_product(client_id, serial_num):
        get_product = ProductTable.get_my_product(client_id, serial_num)
        if len(get_product['data']) > 0:
            get_product['data']['photo'] = utls.byte_to_base64(
                get_product['data']['format'],
                get_product['data']['photo']
                )
            del get_product['data']['format']

        return {
            'success' : get_product['success'],
            'data' : get_product['data'],
            'log_code' : utls.record_log(get_product, 'get', 'crud_logs')
        }


    @staticmethod
    def get_my_products(client_id):
        result = ProductTable.get_my_products(client_id)

        headers = {'Content-Type': 'application/json; charset=utf8'}
        ss_ser_num = {'serial_num' : []}
        sg_ser_num = {'serial_num' : []}

        if len(result['data']) > 0:
            result['data']['photo'] = utls.byte_to_base64(
                result['data']['format'],
                result['data']['photo']
            )
            for i in range(len(result['data']['product_id'])):

                if result['data']['product_id'][i] == 1:
                    ss_ser_num['serial_num'].append(result['data']['serial_num'][i])

                if result['data']['product_id'][i] == 2:
                    sg_ser_num['serial_num'].append(result['data']['serial_num'][i])

        ss_params = json.dumps(ss_ser_num)
        sg_params = json.dumps(sg_ser_num)

        ss_resp = reqs.post(
            hd_server + '/ss_get_status',
            data = ss_params,
            headers = headers
            )

        sg_resp = reqs.post(
            hd_server + '/sg_get_status',
            data = sg_params,
            headers = headers
            )

        return {
            'success' : result['success'],
            'data' : result['data'],
            'ss_action' : ss_resp.json()['data'],
            'sg_action' : sg_resp.json()['data'],
            'log_code' : utls.record_log(result, 'get_my_products', 'crud_logs')
        }


    @staticmethod
    def get_logs(ser_num, product_id, start_date, end_date):
        headers = {'Content-Type': 'application/json; charset=utf8'}

        if str(product_id) == '1':
            ss_params = json.dumps({'serial_num' : ser_num,
                                    'start_date' : start_date,
                                    'end_date' : end_date
            })

            ss_resp = reqs.post(
                hd_server + '/ss_get_logs',
                data = ss_params,
                headers = headers
                )
            
            return {
                'action' : ss_resp.json()['data']
            }

        if str(product_id) == '2':
            sg_params = json.dumps({'serial_num' : ser_num,
                                    'start_date' : start_date,
                                    'end_date' : end_date
            })

            sg_resp = reqs.post(
                hd_server + '/sg_get_logs',
                data = sg_params,
                headers = headers
                )

            return {
                'action' : sg_resp.json()['data']
            }


    @staticmethod
    def turn_on(ser_num):
        headers = {'Content-Type': 'application/json; charset=utf8'}

        resp = reqs.post(
            hd_server + '/turn_on',
            data = json.dumps(ser_num),
            headers=headers
        )

        return resp.json()


    @staticmethod
    def turn_off(ser_num):
        headers = {'Content-Type': 'application/json; charset=utf8'}

        resp = reqs.post(
            hd_server + '/turn_off',
            data = json.dumps(ser_num),
            headers=headers
        )

        return resp.json()