from .. import crud


class ClientTable:

    @staticmethod
    def insert(client_info):
        return crud.insert('clients', client_info)


    @staticmethod
    def get(client_id):
        return crud.get('clients', {'client_id' : client_id})


    @staticmethod
    def get_all():
        return crud.get_all('clients')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_fullnames('clients', ['client_id', 'last_name', 'first_name', 'middle_name'])


    @staticmethod
    def get_fullnames(clients_ids):
        result = crud.get_columns_by_ids(
            'clients',
            ['client_id', 'first_name', 'middle_name', 'last_name'],
            'client_id',
            clients_ids
        )

        if len(result['data']) > 0:
            names_ids={}
            data = result['data']
            data_len = len(data['client_id'])
            for i in range(data_len):
                names_ids[data['client_id'][i]] = f"{data['last_name'][i]} {data['first_name'][i]} {data['middle_name'][i]}"

            result['data'] = names_ids

        return result


    @staticmethod
    def update(client_info):
        return crud.update('clients', client_info, 'client_id')


    @staticmethod
    def delete(client_id):
        return crud.delete('clients', {'client_id' : client_id})


    @staticmethod
    def login(clientname):
        return crud.get_records('clients', {'username' : clientname})


    @staticmethod
    def update_last_signin(client_info, signin_time):
        client_info['last_signin'] = signin_time
        return crud.update('clients', client_info, 'client_id')


    @staticmethod
    def change_password(client_info, new_password):
        client_info['password'] = new_password
        return crud.update('clients', client_info, 'client_id')