from .. import crud
from .. import model_utils as utls


class ProductPhotoTable:

    @staticmethod
    def insert(product_photo):
        pk, val = crud.last_pk_value('product_photo').popitem()
        sql = f'INSERT INTO product_photo ({pk}, '
        values = f'VALUES ({val + 1}, '
        for key in product_photo.keys():
            sql += key + ', '
            values += f'%({key})s, '

        sql += 'active) '
        values += 'TRUE)'
        sql = sql + values
        result = utls.send_to_db(sql, product_photo, False)

        if result['success']:
            result['data'] = {'photo_id' : val + 1}
        else:
            result['data'] = {}
        return result


    @staticmethod
    def get(photo_id):
        return crud.get('product_photo', {'photo_id' : photo_id})


    @staticmethod
    def get_all():
        return crud.get_all('product_photo')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('product_photo', 'photo_id', 'name')


    @staticmethod
    def get_names_by_ids(products_ids):
        result = crud.get_columns_by_ids(
            'product_photo',
            ['photo_id', 'name'],
            'photo_id',
            products_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['photo_id'])
            for i in range(data_len):
                names_ids[data['photo_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def delete(photo_id):
        return crud.delete('product_photo', {'photo_id' : photo_id})