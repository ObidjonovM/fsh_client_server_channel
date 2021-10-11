from client_server_channel.models import ProductTable
from .product_photo import ProductPhotoC
from .. import control_utils as utls
from datetime import datetime
import requests as reqs
import json
from client_server_channel.config import hd_server

HEADERS = {'Content-Type': 'application/json; charset=utf8'}

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
            if not product_info['mac_address']:
                product_info['mac_address'] = None
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
            'comment' : 'НЕ СУЩЕСТВУЕТ'
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
            'comment' : 'НЕ СУЩЕСТВУЕТ'
        }


    @staticmethod
    def my_product_info(client_id, ser_num):
        result = ProductTable.my_product_info(client_id, ser_num)

        return {
            'success' : result['success'],
            'data' : result['data'],
            'log_code' : utls.record_log(result, 'my_product_info', 'crud_logs')
        }


    @staticmethod
    def get_my_product(client_id, serial_num):
        get_product = ProductTable.get_my_product(client_id, serial_num)

        ser_num = {'serial_num' : ''}
        resp = {}

        if len(get_product['data']) > 0:
            get_product['data']['photo'] = utls.byte_to_base64(
                get_product['data']['format'],
                get_product['data']['photo']
                )
            del get_product['data']['format']

            ser_num['serial_num'] = get_product['data']['serial_num'][0]
            params = json.dumps(ser_num)

            if get_product['data']['product_id'][0] == 1:

                resp = reqs.post(
                    hd_server + '/socket/get_current_state',
                    data = params,
                    headers = HEADERS
                ).json()

            # if get_product['data']['product_id'][0] == 2:

            #     resp = reqs.post(
            #         hd_server + '/sg_get_status',
            #         data = params,
            #         headers = HEADERS
            #     ).json()

        return {
            'success' : get_product['success'],
            'data' : get_product['data'],
            'action' : resp,
            'log_code' : utls.record_log(get_product, 'get_my_product', 'crud_logs')
        }


    @staticmethod
    def get_my_products(client_id):
        result = ProductTable.get_my_products(client_id)

        if len(result['data']) > 0:
            result['data']['photo'] = utls.byte_to_base64(
                result['data']['format'],
                result['data']['photo']
            )
            del result['data']['format']
            
        return {
            'success' : result['success'],
            'data' : result['data'],
            'log_code' : utls.record_log(result, 'get_my_products', 'crud_logs')
        }


    @staticmethod
    def get_current_state(ser_num, product_id):
        serial_num = {'serial_num' : ''}
        resp = {}
        serial_num['serial_num'] = ser_num
        params = json.dumps(serial_num)

        if product_id == 1:

            resp = reqs.post(
                hd_server + '/socket/get_current_state',
                data = params,
                headers = HEADERS
            ).json()

        # if product_id == 2:

        #     resp = reqs.post(
        #         hd_server + '/gas/get_current_state',
        #         data = params,
        #         headers = HEADERS
        #     ).json()

        return resp


    @staticmethod
    def get_current_states(ser_num, product_id):
        ss_ser_nums = {'serial_nums' : []}
        sg_ser_nums = {'serial_nums' : []}
        ss_resp = {}
        sg_resp = {}

        for i in range(len(product_id)):

            if product_id[i] == 1:
                ss_ser_nums['serial_nums'].append(ser_num[i])

            # if product_id[i] == 2:
            #     sg_ser_nums['serial_nums'].append(ser_num[i])

        ss_params = json.dumps(ss_ser_nums)
        # sg_params = json.dumps(sg_ser_nums)

        ss_resp = reqs.post(
            hd_server + '/socket/get_current_states',
            data = ss_params,
            headers = HEADERS
            ).json()

        # sg_resp = reqs.post(
        #     hd_server + '/gas/get_current_states',
        #     data = sg_params,
        #     headers = HEADERS
        #     ).json()


        return {
            'ss_resp' : ss_resp,
            'sg_resp' : sg_resp
        }


    @staticmethod
    def get_all_states_in_range(ser_num, product_id, start_date, end_date):
        ss_params = {}
        sg_params = {}
        ss_resp = {}
        sg_resp = {}
        if str(product_id) == '1':
            ss_params = json.dumps({'serial_num' : ser_num,
                                    'start_date' : start_date,
                                    'end_date' : end_date
            })

            ss_resp = reqs.post(
                hd_server + '/socket/get_all_states_in_range',
                data = ss_params,
                headers = HEADERS
                ).json()
            
            return ss_resp

        if str(product_id) == '2':
            sg_params = json.dumps({'serial_num' : ser_num,
                                    'start_date' : start_date,
                                    'end_date' : end_date
            })

            # sg_resp = reqs.post(
            #     hd_server + '/sg_get_logs',
            #     data = sg_params,
            #     headers = HEADERS
            #     ).json()

            return sg_resp


    @staticmethod
    def last_request_time(ser_num):
        resp = {}
        resp = reqs.post(
            hd_server + '/socket/last_request_time',
            data = json.dumps(ser_num),
            headers=HEADERS
        ).json()

        return resp


    @staticmethod
    def enter_requested_action(params):
        resp = {}
        resp = reqs.post(
            hd_server + '/socket/enter_requested_action',
            data = json.dumps(params),
            headers=HEADERS
        ).json()

        return resp


    @staticmethod
    def last_requested_action(ser_num):
        resp = {}
        resp = reqs.post(
            hd_server + '/socket/last_requested_action',
            data = json.dumps(ser_num),
            headers=HEADERS
        ).json()

        return resp


    @staticmethod
    def requested_actions(ser_num):
        resp = {}
        resp = reqs.post(
            hd_server + '/socket/requested_actions',
            data = json.dumps(ser_num),
            headers=HEADERS
        ).json()

        return resp