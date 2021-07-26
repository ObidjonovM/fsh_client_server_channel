from .. import crud


class SpWarehouseTable:

    @staticmethod
    def insert(sp_warehouse_info):
        return crud.insert('sp_warehouse', sp_warehouse_info)


    @staticmethod
    def get(sp_id):
        return crud.get('sp_warehouse', {'sp_id' : sp_id})


    @staticmethod
    def get_all():
        return crud.get_all('sp_warehouse')


    @staticmethod
    def update(sp_warehouse_info):
        return crud.update('sp_warehouse', sp_warehouse_info, 'sp_id')


    @staticmethod
    def delete(sp_id):
        return crud.delete('sp_warehouse', {'sp_id' : sp_id})