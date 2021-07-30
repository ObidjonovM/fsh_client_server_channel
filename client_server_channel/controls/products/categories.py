from client_server_channel.models import CategoriesTable
from .. import control_utils as utls
from datetime import datetime


class CategoriesC:

    @staticmethod
    def add(cat_info):
        now = datetime.now()
        cat_info['leaf_cat'] = False
        cat_info['date_added'] = now
        cat_info['date_modified'] = now
        add_result = CategoriesTable.insert(cat_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(cat_id):
        get_result = CategoriesTable.get(cat_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = CategoriesTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = CategoriesTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_parent_cat():
        ids_names = CategoriesTable.get_parent_cat()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_parent_cat', 'crud_logs')
        }


    @staticmethod
    def get_leaf_cat():
        ids_names = CategoriesTable.get_leaf_cat()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_leaf_cat', 'crud_logs')
        }


    @staticmethod
    def get_other_pairs(cat_id):
        ids_names = CategoriesTable.get_other_pairs(cat_id)

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(cats_ids):
        names_ids = CategoriesTable.get_names_by_ids(cats_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(cat_info):
        get_result = CategoriesTable.get(cat_info['category_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            cat_info['date_modified'] = datetime.now()
            update_result = CategoriesTable.update(cat_info)
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
    def delete(cat_id):
        get_result = CategoriesTable.get(cat_id)

        if get_result['data'] == []:
            return {
                'success' : False,
                'log_code' : utls.record_log(get_result, 'delete', 'crud_logs'),
                'comment' : 'DOES NOT EXIST'
            }

        res_par_leaf = CategoriesTable.get_par_leaf()

        if not len(res_par_leaf['data']) > 0:
            return {
                'success' : False,
                'log_code' : utls.record_log(res_par_leaf, 'delete', 'crud_logs')
            }

        if not cat_id in res_par_leaf['data']['parent_cat_id']:
            if get_result['data']['leaf_cat'] == False:
                delete_result = CategoriesTable.delete(cat_id)

                return {
                    'success' : delete_result['success'],
                    'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
                }

        return {
            'success' : False,
            'log_code' : -1010
        }

