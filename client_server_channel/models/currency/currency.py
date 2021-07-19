from .. import crud


class CurrencyTable:

    @staticmethod
    def insert(curr_info):
        return crud.insert('currencies', curr_info)


    @staticmethod
    def get(curr_id):
        return crud.get('currencies', {'curr_id' : curr_id})


    @staticmethod
    def get_all():
        return crud.get_all('currencies')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('currencies', 'curr_id', 'currency')


    @staticmethod
    def get_names_by_ids(currs_ids):
        result = crud.get_columns_by_ids(
            'currencies',
            ['curr_id', 'currency'],
            'curr_id',
            currs_ids
        )

        if result['data'] != []:
            names_ids={}
            data = result['data']
            data_len = len(data['curr_id'])
            for i in range(data_len):
                names_ids[data['curr_id'][i]] = data['currency'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def delete(curr_id):
        return crud.delete('currencies', {'curr_id' : curr_id})