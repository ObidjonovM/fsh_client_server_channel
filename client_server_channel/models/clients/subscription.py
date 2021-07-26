from .. import crud


class SubscriptionTable:

    @staticmethod
    def insert(subs_info):
        return crud.insert('subscriptions', subs_info)


    @staticmethod
    def get(subs_id):
        return crud.get('subscriptions', {'subs_id' : subs_id})


    @staticmethod
    def get_all():
        return crud.get_all('subscriptions')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('subscriptions', 'subs_id', 'name')


    @staticmethod
    def get_names_by_ids(subscriptions_ids):
        result = crud.get_columns_by_ids(
            'subscriptions',
            ['subs_id', 'name'],
            'subs_id',
            subscriptions_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['subs_id'])
            for i in range(data_len):
                names_ids[data['subs_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(subs_info):
        return crud.update('subscriptions', subs_info, 'subs_id')


    @staticmethod
    def delete(subs_id):
        return crud.delete('subscriptions', {'subs_id' : subs_id})