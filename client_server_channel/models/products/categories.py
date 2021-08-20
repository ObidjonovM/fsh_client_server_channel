from .. import crud
from .. import model_utils as utls


class CategoriesTable:

    @staticmethod
    def insert(cat_info):
        return crud.insert('categories', cat_info)


    @staticmethod
    def get(cat_id):
        return crud.get('categories', {'category_id' : cat_id})


    @staticmethod
    def get_all():
        sql = 'SELECT category_id, name, parent_cat_id FROM categories'
        sql += ' WHERE category_id != 1 ORDER BY category_id'

        result = crud.run_SQL(sql, ['category_id', 'name', 'parent_cat_id'])

        return result


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('categories', 'category_id', 'name')




    @staticmethod
    def get_parent_cat():
        sql = 'SELECT category_id, name FROM categories'
        sql += ' WHERE active = TRUE AND leaf_cat = FALSE'

        result = crud.run_SQL(sql, ['category_id', 'name'])

        return result


    @staticmethod
    def get_leaf_cat():
        sql = 'SELECT a.category_id, a.name FROM categories a'
        sql += ' LEFT JOIN categories b ON a.category_id = b.parent_cat_id'
        sql += ' WHERE a.active = TRUE AND b.parent_cat_id is null'
        
        result = crud.run_SQL(sql, ['category_id', 'name'])

        return result


    @staticmethod
    def get_par_leaf():
        return crud.get_columns_by_col_names('categories', ['parent_cat_id'])


    @staticmethod
    def get_first_par_cat():
        sql = 'SELECT category_id, name FROM categories WHERE'
        sql += ' parent_cat_id = 1 AND category_id != 1'
        sql += ' AND active = TRUE ORDER BY category_id'

        result = crud.run_SQL(sql, ['category_id', 'name'])

        return result


    @staticmethod
    def get_product_by_cat_id(cat_id):
        sql = 'SELECT pi.product_id, pi.name, pi.photo_id, pp.name, pp.photo_byte FROM'
        sql += ' product_info pi , product_photo pp WHERE pi.photo_id = pp.photo_id AND'
        sql += f' category_id = {cat_id} AND pi.active = TRUE'
        sql += ' ORDER BY category_id'

        result = crud.run_SQL(sql, ['product_id', 'product_name', 'photo_id', 'photo_name', 'photo'])

        return result


    @staticmethod
    def get_other_pairs(cat_id):
        return crud.get_other_pairs(
            'categories', 'category_id', 'name', cat_id)


    @staticmethod
    def get_names_by_ids(cats_ids):
        result = crud.get_columns_by_ids(
            'categories',
            ['category_id', 'name'],
            'category_id',
            cats_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['category_id'])
            for i in range(data_len):
                names_ids[data['category_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(cat_info):
        return crud.update('categories', cat_info, 'category_id')


    @staticmethod
    def delete(cat_id):
        return crud.delete('categories', {'category_id' : cat_id})