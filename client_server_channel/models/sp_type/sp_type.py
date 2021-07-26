from .. import crud


class SpTypeTable:

    @staticmethod
    def insert(sp_type_info):
        return crud.insert('sp_types', sp_type_info)


    @staticmethod
    def get(sp_type_id):
        return crud.get('sp_types', {'sp_type_id' : sp_type_id})


    @staticmethod
    def get_all():
        return crud.get_all('sp_types')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('sp_types', 'sp_type_id', 'name')


    @staticmethod
    def get_names_by_ids(sp_types_ids):
        result = crud.get_columns_by_ids(
            'sp_types',
            ['sp_type_id', 'name'],
            'sp_type_id',
            sp_types_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['sp_type_id'])
            for i in range(data_len):
                names_ids[data['sp_type_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(sp_type_info):
        return crud.update('sp_types', sp_type_info, 'sp_type_id')


    @staticmethod
    def delete(sp_type_id):
        return crud.delete('sp_types', {'sp_type_id' : sp_type_id})