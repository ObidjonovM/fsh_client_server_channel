from .. import crud


class SpOrderStatusTable:

    @staticmethod
    def insert(sp_order_status_info):
        return crud.insert('sp_order_statuses', sp_order_status_info)


    @staticmethod
    def get(status_id):
        return crud.get('sp_order_statuses', {'status_id' : status_id})


    @staticmethod
    def get_all():
        return crud.get_all('sp_order_statuses')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('sp_order_statuses', 'status_id', 'name')


    @staticmethod
    def get_names_by_ids(sp_order_statuses_ids):
        result = crud.get_columns_by_ids(
            'sp_order_statuses',
            ['status_id', 'name'],
            'status_id',
            sp_order_statuses_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['status_id'])
            for i in range(data_len):
                names_ids[data['status_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(sp_order_status_info):
        return crud.update('sp_order_statuses', sp_order_status_info, 'status_id')


    @staticmethod
    def delete(status_id):
        return crud.delete('sp_order_statuses', {'status_id' : status_id})