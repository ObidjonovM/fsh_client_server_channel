from .. import crud
from .. import model_utils as utls


class ProductInfoTable:

    @staticmethod
    def insert(product_info):
        pk, val = crud.last_pk_value('product_info').popitem()
        sql = f'INSERT INTO product_info ({pk}, '
        values = f'VALUES ({val + 1}, '
        for key in product_info.keys():
            sql += key + ', '
            values += f'%({key})s, '

        sql += 'active) '
        values += 'TRUE)'
        sql = sql + values
        result = utls.send_to_db(sql, product_info, False)

        if result['success']:
            result['data'] = {'product_id' : val + 1}
        else:
            result['data'] = {}
        return result


    @staticmethod
    def get(product_id):
        return crud.get('product_info', {'product_id' : product_id})


    @staticmethod
    def get_all():
        return crud.get_all('product_info')


    @staticmethod
    def get_all_info():
        sql = 'SELECT pp.small_photo, pp.photo_format, pi.product_id, pi.name, pi.model FROM '
        sql += 'product_photo pp, product_info pi WHERE pp.main_photo = TRUE '
        sql += 'AND pp.product_id = pi.product_id AND pp.active = TRUE AND pi.active = TRUE'
        
        return crud.run_SQL(sql, ['photo', 'format', 'product_id', 'name', 'model'])


    @staticmethod
    def get_all_info_by_prod_id(product_id):
        sql = 'SELECT pp.small_photo, pp.original_photo, pp.photo_format, '
        sql += 'pp.main_photo, pi.name, pi.model, pi.description FROM '
        sql += 'product_photo pp, product_info pi WHERE pp.product_id = pi.product_id '
        sql += f'AND pi.product_id = {product_id} AND pp.active = TRUE AND pi.active = TRUE'
        
        return crud.run_SQL(sql, ['sm_photo', 'org_photo', 'format',
                                 'main_photo', 'name', 'model', 'description']
                                 )


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('product_info', 'product_id', 'name')


    @staticmethod
    def get_products_by_cat_id(cat_id):
        sql = 'SELECT pi.product_id, pi.name, pp.photo_id, pp.small_photo FROM '
        sql += 'product_info pi , product_photo pp WHERE pi.product_id = pp.product_id AND '
        sql += f'pi.category_id = {cat_id} AND pp.main_photo = TRUE AND pi.active = TRUE '
        sql += 'AND pp.active = TRUE ORDER BY pi.product_id'

        result = crud.run_SQL(sql, ['product_id', 'product_name', 'photo_id', 'photo'])

        return result


    @staticmethod
    def get_names_by_ids(products_ids):
        result = crud.get_columns_by_ids(
            'product_info',
            ['product_id', 'name'],
            'product_id',
            products_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['product_id'])
            for i in range(data_len):
                names_ids[data['product_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(product_info):
        return crud.update('product_info', product_info, 'product_id')


    @staticmethod
    def delete(product_id):
        return crud.delete('product_info', {'product_id' : product_id})