from client_server_channel.models import ProductPhotoTable
from .. import control_utils as utls
from datetime import datetime


class ProductPhotoC:

    @staticmethod
    def add(product_photo):
        now = datetime.now()
        product_photo['date_added'] = now
        product_photo['date_modified'] = now
        add_result = ProductPhotoTable.insert(product_photo)
        
        return {
            'success' : add_result['success'],
            'data' : add_result['data'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(photo_id):
        get_result = ProductPhotoTable.get(photo_id)
        get_result['data']['photo_byte'] = utls.byte_to_base64(
            [get_result['data']['name']],
            [get_result['data']['photo_byte']]
        )

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = ProductPhotoTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = ProductPhotoTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(products_ids):
        names_ids = ProductPhotoTable.get_names_by_ids(products_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def delete(photo_id):
        get_result = ProductPhotoTable.get(photo_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = ProductPhotoTable.delete(photo_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }

