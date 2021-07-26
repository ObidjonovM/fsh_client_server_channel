from .. import crud


class ShippingTypeTable:

    @staticmethod
    def insert(shipp_type_info):
        return crud.insert('shipping_types', shipp_type_info)


    @staticmethod
    def get(shipping_type_id):
        return crud.get('shipping_types', {'shipping_type_id' : shipping_type_id})


    @staticmethod
    def get_all():
        return crud.get_all('shipping_types')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('shipping_types', 'shipping_type_id', 'name')


    @staticmethod
    def get_names_by_ids(shipping_types_ids):
        result = crud.get_columns_by_ids(
            'shipping_types',
            ['shipping_type_id', 'name'],
            'shipping_type_id',
            shipping_types_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['shipping_type_id'])
            for i in range(data_len):
                names_ids[data['shipping_type_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(shipp_type_info):
        return crud.update('shipping_types', shipp_type_info, 'shipping_type_id')


    @staticmethod
    def delete(shipping_type_id):
        return crud.delete('shipping_types', {'shipping_type_id' : shipping_type_id})