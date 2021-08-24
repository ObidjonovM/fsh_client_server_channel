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
    def get_ids_names():
        return crud.get_ids_names('product_info', 'product_id', 'name')


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
    def delete(product_id):
        return crud.delete('product_info', {'product_id' : product_id})