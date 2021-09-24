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
    def generate_ap_login():
        sql = 'SELECT COUNT(ap_login) FROM products'
        result = crud.run_SQL(sql, ['ap_login'])

        return result


    @staticmethod
    def generate_ap_password(pwd_len):
        ap_password = generate_token(pwd_len)
        while crud.record_exists('products', {'ap_password' : ap_password}):
            ap_password = generate_token(pwd_len)

        return ap_password


    @staticmethod
    def insert(product_info):
        return crud.insert('products', product_info, False)


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

        if len(result['data']) > 0:
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


    @staticmethod
    def get_my_products(client_id):
        sql = 'SELECT p.serial_num, p.product_id, pp.small_photo, '
        sql += 'pp.photo_format, p.mac_address, p.default_login, p.default_password, '
        sql += 'p.ap_login, p.ap_password, p.manufactured_date, p.description FROM '
        sql += 'products p, product_photo pp WHERE pp.main_photo = TRUE '
        sql += f'AND p.active = TRUE AND pp.active = TRUE AND p.client_id = {client_id} '
        sql += 'AND p.product_id = pp.product_id ORDER BY p.serial_num'

        return crud.run_SQL(sql, ['serial_num', 'product_id', 'photo', 'format', 
                                'mac_address', 'default_login', 'default_password',
                                'ap_login', 'ap_password', 'manufactured_date', 'description'])


    @staticmethod
    def get_my_product(client_id, ser_num):
        sql = 'SELECT p.serial_num, p.product_id, pp.small_photo, '
        sql += 'pp.photo_format, p.mac_address, p.default_login, p.default_password, '
        sql += 'p.ap_login, p.ap_password, p.manufactured_date, p.description FROM '
        sql += 'products p, product_photo pp WHERE pp.main_photo = TRUE AND '
        sql += f"p.product_id = pp.product_id AND p.client_id = {client_id} AND "
        sql += f"p.serial_num = '{ser_num}' AND p.active = TRUE "
        sql += 'AND pp.active = TRUE ORDER BY p.serial_num'

        return crud.run_SQL(sql, ['serial_num', 'product_id', 'photo', 'format',
                                'mac_address', 'default_login', 'default_password',
                                'ap_login', 'ap_password', 'manufactured_date', 'description'])