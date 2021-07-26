from .. import crud


class DealerTable:

    @staticmethod
    def insert(dealer_info):
        return crud.insert('dealers', dealer_info)


    @staticmethod
    def get(dealer_id):
        return crud.get('dealers', {'dealer_id' : dealer_id})


    @staticmethod
    def get_all():
        return crud.get_all('dealers')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('dealers', 'dealer_id', 'name')


    @staticmethod
    def get_names_by_ids(dealers_ids):
        result = crud.get_columns_by_ids(
            'dealers',
            ['dealer_id', 'name'],
            'dealer_id',
            dealers_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['dealer_id'])
            for i in range(data_len):
                names_ids[data['dealer_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(dealer_info):
        return crud.update('dealers', dealer_info, 'dealer_id')


    @staticmethod
    def delete(dealer_id):
        return crud.delete('dealers', {'dealer_id' : dealer_id})