from client_server_channel.models import ProductPhotoTable
from .. import control_utils as utls
from datetime import datetime
import io
import base64
from PIL import Image


def resize_photos(photos):
    result = {}
    star = photos.find("data:image/")
    end = photos.find(";base64")
    format_img = photos[star + 11:end]
    base64_str = "'" + photos[end + 8:]  + "'"
    buffer = io.BytesIO()
    img_byte = base64.b64decode(base64_str)
    img = Image.open(io.BytesIO(img_byte))
    small_img = img.resize((379, 304))  # x, y
    small_img.save(buffer, format=format_img)
    small_img_byte = buffer.getvalue()
    img.save(buffer, format=format_img)

    result['org'] = img_byte
    result['small'] = small_img_byte
    result['format'] = format_img

    return result


class ProductPhotoC:

    @staticmethod
    def add(product_photo):
        now = datetime.now()
        for i in range(len(product_photo['main_photo'])):
            resize_result = resize_photos(
                product_photo['other_photos'][i]
                )

            add_result = ProductPhotoTable.insert({
                'main_photo' : product_photo['main_photo'][i],
                'product_id' : product_photo['product_id'],
                'photo_format' : resize_result['format'],
                'original_photo' : resize_result['org'],
                'small_photo' : resize_result['small'],
                'date_added' : now,
                'add_emp_id' : product_photo['add_emp_id'],
                'date_modified' : now,
                'modify_emp_id' : product_photo['modify_emp_id']
            })
            if not add_result['success']:
                return {
                    'success' : False,
                    'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
                }

        return {
            'success' : add_result['success'],
            'data' : add_result['data'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(photo_id):
        get_result = ProductPhotoTable.get(photo_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_by_product_id(product_id):
        get_result = ProductPhotoTable.get_by_product_id(product_id)
        if len(get_result['data']) > 0:
            get_result['data']['original_photo'] = utls.byte_to_base64(
                get_result['data']['photo_format'],
                get_result['data']['original_photo']
                )

            get_result['data']['small_photo'] = utls.byte_to_base64(
                get_result['data']['photo_format'],
                get_result['data']['small_photo']
                )

            del get_result['data']['photo_format']

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get_by_product_id', 'crud_logs')
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
    def update_main_photo(product_photo):
        get_result = ProductPhotoTable.get_multiple(product_photo['photos_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        product_photo['date_modified'] = datetime.now()
        if len(product_photo['photos_id']) == len(product_photo['main_photo']):
            if len(get_result['data']) > 0:
                if len(get_result['data']['photo_id']) == len(product_photo['photos_id']):

                    update_info = ProductPhotoTable.update_main_photo(product_photo)

                    return {
                        'success' : update_info['success'],
                        'log_code' : utls.record_log(update_info, 'update', 'crud_logs')
                    }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'НЕ СУЩЕСТВУЕТ'
        }


    @staticmethod
    def delete(photo_id):
        get_result = ProductPhotoTable.get(photo_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            if get_result['data']['main_photo'] == False:
                delete_result = ProductPhotoTable.delete(photo_id)
                return {
                    'success' : delete_result['success'],
                    'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
                }

            return {
                'success' : False,
                'log_code' : log_code,
                'comment' : 'Нельзя удалить основную фотографию!'
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'НЕ СУЩЕСТВУЕТ'
        }

