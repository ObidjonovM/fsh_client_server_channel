from .. import crud
from .. import model_utils as utls

class ProductPhotoTable:

    @staticmethod
    def insert(product_photo):
        return crud.insert('product_photo', product_photo)


    @staticmethod
    def get(photo_id):
        return crud.get('product_photo', {'photo_id' : photo_id})


    @staticmethod
    def get_multiple(photos_id):
        col_names = utls.get_column_names('product_photo')
        sql = 'SELECT * FROM product_photo WHERE photo_id IN '
        values = '('
        for photo_id in photos_id:
            values += str(photo_id) + ', '
        values = values[:-2] + ') '
        sql += values
        sql += 'AND active = TRUE'

        return crud.run_SQL(sql, col_names)


    @staticmethod
    def get_by_product_id(product_id):
        col_names = utls.get_column_names('product_photo')
        sql = f'SELECT * FROM product_photo WHERE product_id = {product_id} '
        sql += 'AND active = TRUE'
        result = crud.run_SQL(sql, col_names)
        
        return result
            

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
    def update(product_photo):
        return crud.update('product_photo', product_photo, 'photo_id')


    @staticmethod
    def update_main_photo(product_photo):
        sql = 'UPDATE product_photo SET main_photo = (CASE photo_id '
        when = ''
        photo_id =''
        for i in range(len(product_photo['main_photo'])):
            when += f"WHEN {product_photo['photos_id'][i]} THEN {product_photo['main_photo'][i]} "
            photo_id += str(product_photo['photos_id'][i]) + ', '
        photo_id = photo_id[:-2]
        sql += when + f'ELSE main_photo END), '
        sql += f"modify_emp_id = {product_photo['modify_emp_id']}, "
        sql += f"date_modified = '{product_photo['date_modified']}' "
        sql += f'WHERE photo_id IN({photo_id}) '
        sql += 'AND active = TRUE'

        return crud.run_SQL(sql, None, False, None, False)


    @staticmethod
    def delete(photo_id):
        return crud.delete('product_photo', {'photo_id' : photo_id})


    @staticmethod
    def delete_by_product_id(product_id):
        return crud.delete('product_photo', {'product_id' : product_id})