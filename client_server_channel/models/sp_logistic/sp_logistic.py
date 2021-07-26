from .. import crud


class SpLogisticTable:

    @staticmethod
    def insert(sp_logistic_info):
        return crud.insert('sp_logistics', sp_logistic_info)


    @staticmethod
    def get(shipment_id):
        return crud.get('sp_logistics', {'shipment_id' : shipment_id})


    @staticmethod
    def get_all():
        return crud.get_all('sp_logistics')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('sp_logistics', 'shipment_id', 'tr_number')


    @staticmethod
    def get_names_by_ids(sp_logistics_ids):
        result = crud.get_columns_by_ids(
            'sp_logistics',
            ['shipment_id', 'tr_number'],
            'shipment_id',
            sp_logistics_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['shipment_id'])
            for i in range(data_len):
                names_ids[data['shipment_id'][i]] = data['tr_number'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(sp_logistic_info):
        return crud.update('sp_logistics', sp_logistic_info, 'shipment_id')


    @staticmethod
    def delete(shipment_id):
        return crud.delete('sp_logistics', {'shipment_id' : shipment_id})