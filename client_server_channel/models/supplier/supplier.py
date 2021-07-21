from .. import crud


class SupplierTable:

    @staticmethod
    def insert(supp_info):
        return crud.insert('suppliers', supp_info)


    @staticmethod
    def get(supplier_id):
        return crud.get('suppliers', {'supplier_id' : supplier_id})


    @staticmethod
    def get_all():
        return crud.get_all('suppliers')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('suppliers', 'supplier_id', 'name')


    @staticmethod
    def get_names_by_ids(suppliers_ids):
        result = crud.get_columns_by_ids(
            'suppliers',
            ['supplier_id', 'name'],
            'supplier_id',
            suppliers_ids
        )

        if result['data'] != []:
            names_ids={}
            data = result['data']
            data_len = len(data['supplier_id'])
            for i in range(data_len):
                names_ids[data['supplier_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(supp_info):
        return crud.update('suppliers', supp_info, 'supplier_id')


    @staticmethod
    def delete(supplier_id):
        return crud.delete('suppliers', {'supplier_id' : supplier_id})