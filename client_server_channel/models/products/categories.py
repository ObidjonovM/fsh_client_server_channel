from .. import crud


class CategoriesTable:

    @staticmethod
    def insert(cat_info):
        return crud.insert('categories', cat_info)


    @staticmethod
    def get(cat_id):
        return crud.get('categories', {'category_id' : cat_id})


    @staticmethod
    def get_all():
        return crud.get_all('categories')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('categories', 'category_id', 'name')


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

        if result['data'] != []:
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