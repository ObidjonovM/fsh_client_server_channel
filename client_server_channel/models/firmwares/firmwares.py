from .. import crud


class FirmwaresTable:

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
    def update(firm_info):
        return crud.update('firmwares', firm_info, 'fw_id')


    @staticmethod
    def delete(firm_id):
        return crud.delete('firmwares', {'fw_id' : firm_id})
