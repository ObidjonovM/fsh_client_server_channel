from .. import crud


class TrackingStatusTable:

    @staticmethod
    def insert(track_status_info):
        return crud.insert('tracking_statuses', track_status_info)


    @staticmethod
    def get(status_id):
        return crud.get('tracking_statuses', {'status_id' : status_id})


    @staticmethod
    def get_all():
        return crud.get_all('tracking_statuses')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('tracking_statuses', 'status_id', 'status')


    @staticmethod
    def get_names_by_ids(tracking_statuses_ids):
        result = crud.get_columns_by_ids(
            'tracking_statuses',
            ['status_id', 'status'],
            'status_id',
            tracking_statuses_ids
        )

        if result['data'] != []:
            names_ids={}
            data = result['data']
            data_len = len(data['status_id'])
            for i in range(data_len):
                names_ids[data['status_id'][i]] = data['status'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(track_status_info):
        return crud.update('tracking_statuses', track_status_info, 'status_id')


    @staticmethod
    def delete(status_id):
        return crud.delete('tracking_statuses', {'status_id' : status_id})