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
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0));
''')


#creating employee_status table
cur.execute('''
CREATE TABLE IF NOT EXISTS employee_status (
	status_id SERIAL PRIMARY KEY,
        status VARCHAR(30) UNIQUE NOT NULL,
        description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0));
''')


#creating employees table
cur.execute('''
CREATE TABLE IF NOT EXISTS employees (
	emp_id SERIAL PRIMARY KEY,
	emp_type_id INT NOT NULL CHECK(emp_type_id > 0), 
	first_name VARCHAR(50) NOT NULL,
	middle_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL,
	address_1 VARCHAR(50) NOT NULL,
	address_2 VARCHAR(50),
	city VARCHAR(50) NOT NULL,
	country VARCHAR(50) NOT NULL,
	zipcode VARCHAR(20) NOT NULL,
	phone VARCHAR(20) UNIQUE NOT NULL,
        home_phone VARCHAR(20),
	email VARCHAR(50) UNIQUE,
	username VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR(50) NOT NULL,
        emp_status_id INT NOT NULL CHECK(emp_status_id > 0),
	last_sign_in TIMESTAMP,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

        UNIQUE (first_name, middle_name, last_name, birth_date),
	FOREIGN KEY(emp_type_id)
	REFERENCES employee_type(emp_type_id),
        FOREIGN KEY(emp_status_id)
	REFERENCES employee_status(status_id));
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
	REFERENCES employees(emp_id)); 
''')


#creating product_info table
cur.execute('''
CREATE TABLE IF NOT EXISTS product_info (
	product_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL,
	model VARCHAR(50) NOT NULL,
	category_id INT NOT NULL CHECK(category_id > 0),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY(category_id)
	REFERENCES categories(category_id),
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
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
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));

''')


# creating subscriptions table
cur.execute('''
CREATE TABLE IF NOT EXISTS subscriptions (
	subs_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL,
	description VARCHAR(200),
	monthly_fee NUMERIC(12,2) NOT NULL CHECK(monthly_fee >= 0),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
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
        home_phone VARCHAR(20),
	email VARCHAR(50),
	username VARCHAR(50) NOT NULL UNIQUE,
	password VARCHAR(50) NOT NULL,
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
        author_id INT CHECK (author_id > 0) NOT NULL,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	UNIQUE(name, model, version),        
        FOREIGN KEY(author_id)
        REFERENCES employees(emp_id),
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating product_status table
cur.execute('''
CREATE TABLE IF NOT EXISTS product_status (
	status_id SERIAL PRIMARY KEY,
        status VARCHAR(30) UNIQUE,
        description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
        
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
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
        status_id INT NOT NULL CHECK (status_id > 0),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY(product_id)
	REFERENCES product_info(product_id),
	FOREIGN KEY(dealer_id)
	REFERENCES dealers(dealer_id),
	FOREIGN KEY(client_id)
	REFERENCES clients(client_id),
        FOREIGN KEY(firmware_id)
	REFERENCES firmwares(fw_id),
	FOREIGN KEY(resp_emp_id)
	REFERENCES employees(emp_id),
        FOREIGN KEY (status_id)
        REFERENCES product_status(status_id), 
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating currency table
cur.execute('''
CREATE TABLE IF NOT EXISTS currencies (
	curr_id SERIAL PRIMARY KEY,
	currency VARCHAR(20) UNIQUE NOT NULL,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating units table
cur.execute('''
CREATE TABLE IF NOT EXISTS units (
	unit_id SERIAL PRIMARY KEY,
        unit VARCHAR(30) NOT NULL UNIQUE,
        description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating suppliers table
cur.execute('''
CREATE TABLE IF NOT EXISTS suppliers (
	supplier_id SERIAL PRIMARY KEY,
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
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating carriers table
cur.execute('''
CREATE TABLE IF NOT EXISTS carriers (
	carrier_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL,
	address_1 VARCHAR(50) NOT NULL,
	address_2 VARCHAR(50),
	city VARCHAR(50) NOT NULL,
	country VARCHAR(50) NOT NULL,
	zipcode VARCHAR(20) NOT NULL,
	phone VARCHAR(20) NOT NULL,
	email VARCHAR(50),
	website VARCHAR(50),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating shipping_types table
cur.execute('''
CREATE TABLE IF NOT EXISTS shipping_types (
        shipping_type_id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        price NUMERIC(12,2) NOT NULL,
        curr_id INT CHECK (curr_id > 0) NOT NULL,
        unit_id INT CHECK (unit_id > 0) NOT NULL,
        min_delivery_days INT CHECK (min_delivery_days > 0) NOT NULL,
        max_delivery_days INT CHECK (min_delivery_days <= max_delivery_days) NOT NULL,
        carrier_id INT CHECK (carrier_id > 0) NOT NULL,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY (curr_id)
	REFERENCES currencies(curr_id),
	FOREIGN KEY (unit_id)
	REFERENCES units(unit_id),
	FOREIGN KEY (carrier_id)
	REFERENCES carriers(carrier_id),
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));

''')


cur.execute('''
CREATE TABLE IF NOT EXISTS tracking_statuses (
	status_id SERIAL PRIMARY KEY,
	status VARCHAR(30) NOT NULL,
	carrier_id INT CHECK (carrier_id > 0) NOT NULL,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	UNIQUE(status, carrier_id),
	FOREIGN KEY (carrier_id)
	REFERENCES carriers(carrier_id),
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating sp_types table
cur.execute('''
CREATE TABLE IF NOT EXISTS sp_types (
	sp_type_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	brand VARCHAR(50),
	model VARCHAR(50),
	version VARCHAR(50),
	description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	UNIQUE(name, brand, model, version),
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating sp_logistics
cur.execute('''
CREATE TABLE IF NOT EXISTS sp_logistics (
	shipment_id SERIAL PRIMARY KEY,
	carrier_id INT NOT NULL CHECK (carrier_id > 0),
	total_cost NUMERIC(12,2) NOT NULL CHECK (total_cost > 0),
	curr_id INT NOT NULL CHECK (curr_id > 0),
	shipping_type_id INT NOT NULL CHECK (shipping_type_id > 0),
	tr_number VARCHAR(50) NOT NULL,
	tr_status_id INT NOT NULL CHECK (tr_status_id > 0),
	tr_status_change_date DATE NOT NULL,
	shipped_date DATE NOT NULL,
	delivered_date DATE NOT NULL,
	comment VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	UNIQUE(tr_number, shipped_date),
	FOREIGN KEY (carrier_id)
	REFERENCES carriers(carrier_id),
	FOREIGN KEY (curr_id)
        REFERENCES currencies(curr_id),
        FOREIGN KEY (shipping_type_id)
	REFERENCES shipping_types(shipping_type_id),
	FOREIGN KEY (tr_status_id)
	REFERENCES tracking_statuses(status_id),
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


cur.execute('''
CREATE TABLE IF NOT EXISTS sp_order_statuses (
	status_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL,
	description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


cur.execute('''
CREATE TABLE IF NOT EXISTS sp_orders (
	sp_order_id SERIAL PRIMARY KEY,
	issued_order_id VARCHAR(50) NOT NULL UNIQUE,
	total_cost NUMERIC (12,2) NOT NULL CHECK (total_cost > 0),
	curr_id INT NOT NULL CHECK (curr_id > 0),
	supplier_id INT	NOT NULL CHECK (supplier_id > 0),
	exp_dispatch_date DATE NOT NULL,
	order_status_id INT NOT NULL CHECK (order_status_id > 0),
	shipment_id INT NOT NULL CHECK (shipment_id > 0),
	order_date DATE NOT NULL,
	ord_emp_id INT NOT NULL CHECK (ord_emp_id > 0),
	date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	
	FOREIGN KEY (curr_id)
	REFERENCES currencies(curr_id),
	FOREIGN KEY (supplier_id)
	REFERENCES suppliers(supplier_id),
	FOREIGN KEY (order_status_id)
	REFERENCES sp_order_statuses(status_id),
	FOREIGN KEY (shipment_id)
	REFERENCES sp_logistics(shipment_id),
	FOREIGN KEY (ord_emp_id)
	REFERENCES employees(emp_id),  
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating error_logs table
cur.execute('''
CREATE TABLE IF NOT EXISTS error_logs (
	log_id SERIAL PRIMARY KEY,
        call_path TEXT NOT NULL,
        function_name VARCHAR(50) NOT NULL,
        line_number INT NOT NULL CHECK (line_number > 0),
        error_name VARCHAR(50) NOT NULL,
        description TEXT NOT NULL,
        date_added TIMESTAMP NOT NULL);
''')


conn.commit()

cur.close()

conn.close()
