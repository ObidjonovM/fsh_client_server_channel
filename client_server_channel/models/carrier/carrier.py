from .. import crud


class CarrierTable:

    @staticmethod
    def insert(carr_info):
        return crud.insert('carriers', carr_info)


    @staticmethod
    def get(carrier_id):
        return crud.get('carriers', {'carrier_id' : carrier_id})


    @staticmethod
    def get_all():
        return crud.get_all('carriers')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('carriers', 'carrier_id', 'name')


    @staticmethod
    def get_names_by_ids(carriers_ids):
        result = crud.get_columns_by_ids(
            'carriers',
            ['carrier_id', 'name'],
            'carrier_id',
            carriers_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['carrier_id'])
            for i in range(data_len):
                names_ids[data['carrier_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(carr_info):
        return crud.update('carriers', carr_info, 'carrier_id')


    @staticmethod
    def delete(carrier_id):
        return crud.delete('carriers', {'carrier_id' : carrier_id})