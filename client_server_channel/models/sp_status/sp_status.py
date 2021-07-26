from .. import crud


class SpStatusTable:

    @staticmethod
    def insert(sp_status_info):
        return crud.insert('sp_statuses', sp_status_info)


    @staticmethod
    def get(status_id):
        return crud.get('sp_statuses', {'status_id' : status_id})


    @staticmethod
    def get_all():
        return crud.get_all('sp_statuses')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('sp_statuses', 'status_id', 'status')


    @staticmethod
    def get_names_by_ids(sp_statuses_ids):
        result = crud.get_columns_by_ids(
            'sp_statuses',
            ['status_id', 'status'],
            'status_id',
            sp_statuses_ids
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
    def update(sp_status_info):
        return crud.update('sp_statuses', sp_status_info, 'status_id')


    @staticmethod
    def delete(status_id):
        return crud.delete('sp_statuses', {'status_id' : status_id})