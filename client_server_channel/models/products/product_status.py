from .. import crud


class ProductStatusTable:

    @staticmethod
    def insert(status_info):
        return crud.insert('product_status', status_info)


    @staticmethod
    def get(status_id):
        return crud.get('product_status', {'status_id' : status_id})


    @staticmethod
    def get_all():
        return crud.get_all('product_status')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('product_status', 'status_id', 'status')


    @staticmethod
    def get_names_by_ids(status_ids):
        result = crud.get_columns_by_ids(
            'product_status',
            ['status_id', 'status'],
            'status_id',
            status_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['status_id'])
            for i in range(data_len):
                names_ids[data['status_id'][i]] = data['status'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(status_info):
        return crud.update('product_status', status_info, 'status_id')


    @staticmethod
    def delete(status_id):
        return crud.delete('product_status', {'status_id' : status_id})