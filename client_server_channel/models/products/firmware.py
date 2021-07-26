from .. import crud


class FirmwareTable:

    @staticmethod
    def insert(firm_info):
        return crud.insert('firmwares', firm_info)


    @staticmethod
    def get(firm_id):
        return crud.get('firmwares', {'fw_id' : firm_id})


    @staticmethod
    def get_all():
        return crud.get_all('firmwares')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('firmwares', 'fw_id', 'name')


    @staticmethod
    def get_names_by_ids(fws_ids):
        result = crud.get_columns_by_ids(
            'firmwares',
            ['fw_id', 'name'],
            'fw_id',
            fws_ids
        )

        if len(result['data']) > 0:
            names_ids = {}
            data = result['data']
            data_len = len(data['fw_id'])
            for i in range(data_len):
                names_ids[data['fw_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result

    @staticmethod
    def update(firm_info):
        return crud.update('firmwares', firm_info, 'fw_id')


    @staticmethod
    def delete(firm_id):
        return crud.delete('firmwares', {'fw_id' : firm_id})
