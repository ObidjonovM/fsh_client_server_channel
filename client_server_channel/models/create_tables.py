import psycopg2

conn = psycopg2.connect('dbname=timur_dev user=timur_dev password=Fido402')

cur = conn.cursor()

#creating employee_type table
cur.execute('''
CREATE TABLE IF NOT EXISTS employee_type (
	emp_type_id SERIAL PRIMARY KEY,
	emp_type_name VARCHAR(50) UNIQUE NOT NULL,
	description VARCHAR(200),
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL);
''')


#creating employees table
cur.execute('''
CREATE TABLE IF NOT EXISTS employees (
	emp_id SERIAL PRIMARY KEY,
	emp_type_id INT NOT NULL, 
	first_name VARCHAR(50) NOT NULL,
	middle_name VARCHAR(50),
	last_name VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL,
	address_1 VARCHAR(50) NOT NULL,
	address_2 VARCHAR(50),
	city VARCHAR(50) NOT NULL,
	country VARCHAR(50) NOT NULL,
	zipcode VARCHAR(20) NOT NULL,
	phone VARCHAR(20) NOT NULL,
	email VARCHAR(50),
	last_sign_in TIMESTAMP,
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL,

	FOREIGN KEY(emp_type_id)
	REFERENCES employee_type(emp_type_id));
''')


# creating category table
cur.execute('''
CREATE TABLE IF NOT EXISTS categories (
	category_id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        description VARCHAR(200),
        parent_cat_id INT NOT NULL CHECK(parent_cat_id >= 0),
        leaf_cat BOOLEAN NOT NULL,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id)); ''')


#creating product_info table
cur.execute('''
CREATE TABLE IF NOT EXISTS product_info (
	product_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL,
	model VARCHAR(50) NOT NULL,
	category_id INT NOT NULL CHECK(category_id > 0),
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL,

	FOREIGN KEY(category_id)
	REFERENCES categories(category_id));
''')


#creating dealers table
cur.execute('''
CREATE TABLE IF NOT EXISTS dealers (
	dealer_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL,
	address_1 VARCHAR(50) NOT NULL,
	address_2 VARCHAR(50),
	city VARCHAR(50) NOT NULL,
	country VARCHAR(50) NOT NULL,
	zipcode VARCHAR(20) NOT NULL,
	phone VARCHAR(20) NOT NULL,
	email VARCHAR(50),
	website VARCHAR(50),
	geo_location VARCHAR(50),
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL);
''')


# creating subscriptions table
cur.execute('''
CREATE TABLE IF NOT EXISTS subscriptions (
	subs_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL,
	description VARCHAR(200),
	monthly_fee NUMERIC(12,2) NOT NULL CHECK(monthly_fee >= 0),
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL);
''')


#creating clients table
cur.execute('''
CREATE TABLE IF NOT EXISTS clients (
	client_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	middle_name VARCHAR(50),
	last_name VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL,
	address_1 VARCHAR(50) NOT NULL,
	address_2 VARCHAR(50),
	city VARCHAR(50) NOT NULL,
	country VARCHAR(50) NOT NULL,
	zipcode VARCHAR(20) NOT NULL,
	phone VARCHAR(20) NOT NULL,
	email VARCHAR(50),
	subs_id INT NOT NULL CHECK (subs_id > 0),
	last_signin TIMESTAMP,
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL,

	FOREIGN KEY(subs_id)
	REFERENCES subscriptions(subs_id));
''')


#creating firmwares table
cur.execute('''
CREATE TABLE IF NOT EXISTS firmwares (
	fw_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
        model VARCHAR(10) NOT NULL,
        version VARCHAR(10) NOT NULL,
        description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL);
''')


#creating products table 
cur.execute('''
CREATE TABLE IF NOT EXISTS products (
	serial_num VARCHAR(12) PRIMARY KEY,
	mac_address MACADDR UNIQUE,
	product_id INT CHECK (product_id > 0) NOT NULL,
	default_login VARCHAR(30) UNIQUE NOT NULL,
	default_password VARCHAR(30) UNIQUE NOT NULL,
	login VARCHAR(30) UNIQUE,
	password VARCHAR(30) UNIQUE,
	dealer_id INT CHECK (dealer_id > 0),
	client_id INT CHECK (client_id > 0),
	manufactured_date DATE NOT NULL,
        firmware_id INT NOT NULL CHECK (firmware_id > 0),
	resp_emp_id INT NOT NULL CHECK (resp_emp_id > 0),
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL,

	FOREIGN KEY(product_id)
	REFERENCES product_info(product_id),
	FOREIGN KEY(dealer_id)
	REFERENCES dealers(dealer_id),
	FOREIGN KEY(client_id)
	REFERENCES clients(client_id),
        FOREIGN KEY(firmware_id)
	REFERENCES firmwares(fw_id),
	FOREIGN KEY(resp_emp_id)
	REFERENCES employees(emp_id)); 
''')


conn.commit()

cur.close()

conn.close()
