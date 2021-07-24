from .. import crud


class SpOrderDetailTable:

    @staticmethod
    def insert(sp_order_det_info):
        return crud.insert('sp_order_details', sp_order_det_info)


    @staticmethod
    def get(detail_id):
        return crud.get('sp_order_details', {'detail_id' : detail_id})


    @staticmethod
    def get_all():
        return crud.get_all('sp_order_details')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('sp_order_details', 'detail_id', 'amount')


    @staticmethod
    def get_names_by_ids(sp_order_details_ids):
        result = crud.get_columns_by_ids(
            'sp_order_details',
            ['detail_id', 'amount'],
            'detail_id',
            sp_order_details_ids
        )

        if result['data'] != []:
            names_ids={}
            data = result['data']
            data_len = len(data['detail_id'])
            for i in range(data_len):
                names_ids[data['detail_id'][i]] = data['amount'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(sp_order_det_info):
        return crud.update('sp_order_details', sp_order_det_info, 'detail_id')


    @staticmethod
    def delete(detail_id):
        return crud.delete('sp_order_details', {'detail_id' : detail_id})