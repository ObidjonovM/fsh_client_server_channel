from .. import crud


class SpOrderTable:

    @staticmethod
    def insert(sp_order_info):
        return crud.insert('sp_orders', sp_order_info)


    @staticmethod
    def get(sp_order_id):
        return crud.get('sp_orders', {'sp_order_id' : sp_order_id})


    @staticmethod
    def get_all():
        return crud.get_all('sp_orders')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('sp_orders', 'sp_order_id')


    @staticmethod
    def get_names_by_ids(sp_orders_ids):
        result = crud.get_columns_by_ids(
            'sp_orders',
            ['sp_order_id'],
            'sp_order_id',
            sp_orders_ids
        )

        if result['data'] != []:
            names_ids={}
            data = result['data']
            data_len = len(data['sp_order_id'])
            for i in range(data_len):
                names_ids[data['sp_order_id'][i]]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(sp_order_info):
        return crud.update('sp_orders', sp_order_info, 'sp_order_id')


    @staticmethod
    def delete(sp_order_id):
        return crud.delete('sp_orders', {'sp_order_id' : sp_order_id})