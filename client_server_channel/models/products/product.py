from .. import crud
import secrets
from datetime import date


# login va parol generatsiya qilish uchun
def generate_token(tkn_len):
    if tkn_len % 2 == 0:
        return secrets.token_hex(tkn_len // 2)

    return secrets.token_hex((tkn_len + 1) // 2)[:-1]


class ProductTable:

    #serial number generator
    @staticmethod
    def generate_serial(type_id):
        ser_num = (
                    str(type_id).zfill(4) + 
                    str(date.today().year)[2:] + 
                    secrets.token_hex(3)
                    )

        while crud.record_exists('products', {'serial_num' : ser_num}):
            ser_num = (
                    str(type_id).zfill(4) + 
                    str(date.today().year)[2:] + 
                    secrets.token_hex(3)
                    )
        
        return ser_num


    @staticmethod
    def generate_login(lgn_len):
        login = generate_token(lgn_len)
        while crud.record_exists('products', {'default_login' : login}):
            login = generate_token(lgn_len)
        
        return login


    @staticmethod
    def generate_password(pwd_len):
        password = generate_token(pwd_len)
        while crud.record_exists('products', {'default_password' : password}):
            password = generate_token(pwd_len)

        return password


    @staticmethod
    def insert(product_info):
        return crud.insert('products', product_info)


    @staticmethod
    def get(serial_num):
        return crud.get('products', {'serial_num' : serial_num})


    @staticmethod
    def get_all():
        return crud.get_all('products')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('products', 'serial_num', 'mac_address')


    @staticmethod
    def get_names_by_ids(products_ids):
        result = crud.get_columns_by_ids(
            'products',
            ['serial_num', 'mac_address'],
            'serial_num',
            products_ids
        )

        if result['data'] != []:
            names_ids={}
            data = result['data']
            data_len = len(data['serial_num'])
            for i in range(data_len):
                names_ids[data['serial_num'][i]] = data['mac_address'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(product_info):
        return crud.update('products', product_info, 'serial_num')


    @staticmethod
    def delete(serial_num):
        return crud.delete('products', {'serial_num' : serial_num})