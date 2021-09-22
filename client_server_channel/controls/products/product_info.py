from client_server_channel.models import (ProductInfoTable, CategoriesTable,
                                        ProductPhotoTable)
from .. import control_utils as utls
from datetime import datetime
import io
import base64
from PIL import Image


class ProductInfoC:

    @staticmethod
    def add(product_info):
        cat_result = CategoriesTable.get(product_info['category_id'])
        if not len(cat_result['data']) > 0:
            
            return {
                'success' : False,
                'data' : cat_result['data'],
                'log_code' : utls.record_log(cat_result, 'add', 'crud_logs')
            }

        cat_result['data']['leaf_cat'] = True
        update_leaf_cat = CategoriesTable.update(cat_result['data'])

        if not update_leaf_cat['success']:

            return {
                'success' : False,
                'log_code' : utls.record_log(update_leaf_cat, 'add', 'crud_logs')
            }

        now = datetime.now()
        product_info['date_added'] = now
        product_info['date_modified'] = now
        add_result = ProductInfoTable.insert({
            'name' : product_info['name'],
            'model' : product_info['model'],
            'category_id' : product_info['category_id'],
            'date_added' : now,
            'add_emp_id' : product_info['add_emp_id'],
            'date_modified' : now,
            'modify_emp_id' : product_info['modify_emp_id']
        })

        for i in range(len(product_info['main_photo'])):

            star = product_info['other_photos'][i].find("data:image/")
            end = product_info['other_photos'][i].find(";base64")
            format_img = product_info['other_photos'][i][star + 11:end]
            base64_str = "'" + product_info['other_photos'][i][end + 8:]  + "'"
            buffer = io.BytesIO()
            imgdata = base64.b64decode(base64_str)
            img = Image.open(io.BytesIO(imgdata))
            small_img = img.resize((379, 304))  # x, y
            small_img.save(buffer, format=format_img)
            small_img_byte = buffer.getvalue()
            img.save(buffer, format=format_img)

            add_photo = ProductPhotoTable.insert({
                'product_id' : add_result['data']['product_id'],
                'photo_format' : format_img,
                'original_photo' : imgdata,
                'small_photo' : small_img_byte,
                'main_photo' : product_info['main_photo'][i],
                'add_emp_id' : product_info['add_emp_id'],
                'modify_emp_id' : product_info['modify_emp_id'],
                'date_added' : now,
                'date_modified' : now
            })

        if not add_photo['success']:

            return {
                'success' : False,
                'log_code' : utls.record_log(add_photo, 'add', 'crud_logs')
            }

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(product_id):
        get_result = ProductInfoTable.get(product_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = ProductInfoTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_all_info():
        get_all_result = ProductInfoTable.get_all_info()

        if len(get_all_result['data']) > 0:
            get_all_result['data']['photo'] = utls.byte_to_base64(
                get_all_result['data']['format'],
                get_all_result['data']['photo']
            )
            del get_all_result['data']['format']

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_all_info_by_prod_id(product_id):
        get_all_result = ProductInfoTable.get_all_info_by_prod_id(product_id)

        if len(get_all_result['data']) > 0:
            get_all_result['data']['sm_photo'] = utls.byte_to_base64(
                get_all_result['data']['format'],
                get_all_result['data']['sm_photo']
            )
            get_all_result['data']['org_photo'] = utls.byte_to_base64(
                get_all_result['data']['format'],
                get_all_result['data']['org_photo']
            )
            del get_all_result['data']['format']

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_products_by_cat_id(cat_id): 
        result = ProductInfoTable.get_products_by_cat_id(cat_id)

        return {
            'success' : result['success'],
            'data' : result['data'],
            'log_code' : utls.record_log(result, 'get_product_by_cat_id', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = ProductInfoTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(products_ids):
        names_ids = ProductInfoTable.get_names_by_ids(products_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def delete(product_id):
        get_result = ProductInfoTable.get(product_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = ProductInfoTable.delete(product_id)
            if delete_result['success']:
                delete_photo = ProductPhotoTable.delete(get_result['data']['photo_id'])
                if not delete_photo['success']:

                    return {
                        'success' : delete_photo['success'],
                        'log_code' : utls.record_log(delete_photo, 'delete', 'crud_logs')
                    }

            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }

