from client_server_channel.models import ClientTable
from .. import control_utils as utls
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash


class ClientC:

    @staticmethod
    def add(client_info):
        now = datetime.now()
        client_info['username'] = f"{client_info['first_name'].lower()}.{client_info['last_name'].lower()}"
        client_info['password'] = generate_password_hash('123')
        client_info['subs_id'] = 1
        client_info['date_added'] = now
        client_info['date_modified'] = now
        add_result = ClientTable.insert(client_info)

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }


    @staticmethod
    def get(client_id):
        get_result = ClientTable.get(client_id)

        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = ClientTable.get_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all', 'crud_logs')
        }


    @staticmethod
    def get_ids_names():
        ids_names = ClientTable.get_ids_names()

        return {
            'success' : ids_names['success'],
            'data' : ids_names['data'],
            'log_code' : utls.record_log(ids_names, 'get_ids_names', 'crud_logs')
        }


    @staticmethod
    def get_names_by_ids(clients_ids):
        names_ids = ClientTable.get_fullnames(clients_ids)

        return {
            'success' : names_ids['success'],
            'data' : names_ids['data'],
            'log_code' : utls.record_log(names_ids, 'get_names_by_ids', 'crud_logs')
        }


    @staticmethod
    def update(client_info):
        get_result = ClientTable.get(client_info['client_id'])
        log_code = utls.record_log(get_result, 'update', 'crud_logs')
        if get_result['data'] != []:
            client_info['date_modified'] = datetime.now()
            client_info['subs_id'] = 1
            update_result = ClientTable.update(client_info)
            return {
                'success' : update_result['success'],
                'log_code' : utls.record_log(update_result, 'update', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }


    @staticmethod
    def delete(client_id):
        get_result = ClientTable.get(client_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_logs')
        if get_result['data'] != []:
            delete_result = ClientTable.delete(client_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }

        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'
        }


    @staticmethod
    def login(clientname, password, new_password):

        login_result = ClientTable.login(clientname)
        result = {
            'success' : login_result['success'],
            'log_code' : utls.record_log(login_result, 'client_login', 'crud_logs')
        }

        if login_result['success']:
            result['user_exists'] = login_result['data'] != []
            result['wrong_password'] = False

            if result['user_exists']:
                result['wrong_password'] = not check_password_hash(
                    login_result['data']['password'],
                    password
                )

                if not result['wrong_password']:
                    if new_password:
                        ClientTable.change_password(
                            login_result['data'],
                            generate_password_hash(new_password)
                        )

                    ClientTable.update_last_signin(login_result['data'], datetime.now())
                    result['wrong_password'] = False
                    result['client_id'] = login_result['data']['client_id']
                    result['first_name'] = login_result['data']['first_name']

        return result