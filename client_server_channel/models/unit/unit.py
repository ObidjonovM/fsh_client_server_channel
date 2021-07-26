from .. import crud


class UnitTable:

    @staticmethod
    def insert(unit_info):
        return crud.insert('units', unit_info)


    @staticmethod
    def get(unit_id):
        return crud.get('units', {'unit_id' : unit_id})


    @staticmethod
    def get_all():
        return crud.get_all('units')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('units', 'unit_id', 'unit')


    @staticmethod
    def get_names_by_ids(depts_ids):
        result = crud.get_columns_by_ids(
            'units',
            ['unit_id', 'unit'],
            'unit_id',
            depts_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['unit_id'])
            for i in range(data_len):
                names_ids[data['unit_id'][i]] = data['unit'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(unit_info):
        return crud.update('units', unit_info, 'unit_id')


    @staticmethod
    def delete(unit_id):
        return crud.delete('units', {'unit_id' : unit_id})