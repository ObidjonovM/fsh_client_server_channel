import psycopg2
from datetime import datetime, date
from werkzeug.security import generate_password_hash


super_user_password = 'FidoBiznes402'
conn = psycopg2.connect('dbname=your_db user=your_login password=your_password')

cur = conn.cursor()

#creating employee_type table
cur.execute('''
CREATE TABLE IF NOT EXISTS employee_type (
	emp_type_id INT PRIMARY KEY CHECK (emp_type_id > 0),
	emp_type_name VARCHAR(50) UNIQUE NOT NULL,
	description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
    active BOOLEAN NOT NULL);
''')


#adding SUPERUSER type to employee_type table
now = datetime.now()
cur.execute('''
DO
$do$

BEGIN
    IF NOT EXISTS (SELECT emp_type_id FROM employee_type) THEN
	INSERT INTO employee_type(
		emp_type_id, emp_type_name, description, 
		date_added, add_emp_id, date_modified, 
        modify_emp_id, active
	)
	VALUES (
		1, 'SUPERUSER', 
		'SUPERUSER type created at the DB initialization', 
		%s, 1, %s, 1, TRUE
	);
    END IF;
END;

$do$
''', (now, now))



#creating employee_status table
cur.execute('''
CREATE TABLE IF NOT EXISTS employee_status (
	status_id INT PRIMARY KEY CHECK (status_id > 0),
        status VARCHAR(30) UNIQUE NOT NULL,
        description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
    active BOOLEAN NOT NULL);
''')


#adding SUPERUSER status to employee_status table
now = datetime.now()
cur.execute('''
DO
$do$

BEGIN
    IF NOT EXISTS (SELECT status_id FROM employee_status) THEN
        INSERT INTO employee_status(
                status_id, status, description,
                date_added, add_emp_id, date_modified, 
                modify_emp_id, active
        )
        VALUES (
                1, 'SUPERUSER',
                'SUPERUSER status created at the DB initialization',
                %s, 1, %s, 1, TRUE
        );
    END IF;
END;

$do$
''', (now, now))


#creating departments table
cur.execute('''
CREATE TABLE IF NOT EXISTS departments (
	dept_id INT PRIMARY KEY CHECK (dept_id > 0),
	name VARCHAR(100) NOT NULL UNIQUE,
	description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
    active BOOLEAN NOT NULL);
''')


#adding SUPERUSER type to departments table
now = datetime.now()
cur.execute('''
DO
$do$

BEGIN
    IF NOT EXISTS (SELECT dept_id FROM departments) THEN
        INSERT INTO departments(
                dept_id, name, description,
                date_added, add_emp_id, date_modified, 
                modify_emp_id, active
        )
        VALUES (
                1, 'SUPERUSER',
                'SUPERUSER department created at the DB initialization',
                %s, 1, %s, 1, TRUE
        );
    END IF;
END;

$do$
''', (now, now))



#creating employees table
cur.execute('''
CREATE TABLE IF NOT EXISTS employees (
	emp_id INT PRIMARY KEY CHECK (emp_id > 0),
	dept_id INT NOT NULL CHECK (dept_id > 0),
        emp_type_id INT NOT NULL CHECK (emp_type_id > 0), 
	first_name VARCHAR(50) NOT NULL,
	middle_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL,
	address_1 VARCHAR(50) NOT NULL,
	address_2 VARCHAR(50),
	city VARCHAR(50) NOT NULL,
	country VARCHAR(50) NOT NULL,
	zipcode VARCHAR(20),
	phone VARCHAR(20) UNIQUE NOT NULL,
        home_phone VARCHAR(20),
	email VARCHAR(50) UNIQUE,
	username VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR NOT NULL,
        emp_status_id INT NOT NULL CHECK (emp_status_id > 0),
	last_sign_in TIMESTAMP,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK (add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK (modify_emp_id > 0),
	active BOOLEAN NOT NULL,	

        UNIQUE (first_name, middle_name, last_name, birth_date, address_1),
        FOREIGN KEY (dept_id)
	REFERENCES departments(dept_id),
	FOREIGN KEY(emp_type_id)
	REFERENCES employee_type(emp_type_id),
        FOREIGN KEY(emp_status_id)
	REFERENCES employee_status(status_id));
''')


# adding SUPERUSER to employees table
now = datetime.now()
today = date.today()
pwd_hash = generate_password_hash(super_user_password)
cur.execute('''
DO
$do$

BEGIN
	IF NOT EXISTS (SELECT emp_id FROM employees) THEN
	    INSERT INTO employees(
		emp_id, dept_id, emp_type_id, 
		first_name, middle_name, last_name,
		birth_date, address_1, city, 
		country, phone, username, 
		password, emp_status_id, date_added, 
		add_emp_id, date_modified, 
		modify_emp_id, active
	    )
	    VALUES (
		1, 1, 1,
		'SUPERUSER', 'SUPERUSER', 'SUPERUSER',
		%s, '8/2 Bunyodkor Avenue', 'Tashkent',
		'Uzbekistan', '+998712779886', 'superuser',
		%s, 1, %s,
		1, %s, 1, TRUE
	    );
	END IF;
END;
$do$
''', (today, pwd_hash, now, now))


# creating category table
cur.execute('''
CREATE TABLE IF NOT EXISTS categories (
	category_id INT PRIMARY KEY CHECK (category_id > 0),
        name VARCHAR(50) UNIQUE NOT NULL,
        description VARCHAR(200),
        parent_cat_id INT NOT NULL CHECK(parent_cat_id >= 0),
        leaf_cat BOOLEAN NOT NULL,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id)); 
''')


now = datetime.now()
cur.execute('''
DO
$do$

BEGIN
    IF NOT EXISTS (SELECT category_id FROM categories) THEN
        INSERT INTO categories(
            category_id, name, description, parent_cat_id, leaf_cat, 
            date_added, add_emp_id, date_modified, 
			modify_emp_id, active
        )
        VALUES (
            1, 'root', '\"root\" category created during DB initialization',
            1, FALSE, %s, 1, %s, 1, TRUE
        );
    END IF;
END;

$do$
''', (now, now))


#creating product_info table
cur.execute('''
CREATE TABLE IF NOT EXISTS product_info (
	product_id INT PRIMARY KEY CHECK (product_id > 0),
	name VARCHAR(50) UNIQUE NOT NULL,
	model VARCHAR(50) NOT NULL,
	category_id INT NOT NULL CHECK(category_id > 0),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,

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
	dealer_id INT PRIMARY KEY CHECK (dealer_id > 0),
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
	active BOOLEAN NOT NULL,

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));

''')


# creating subscriptions table
cur.execute('''
CREATE TABLE IF NOT EXISTS subscriptions (
	subs_id INT PRIMARY KEY CHECK (subs_id > 0),
	name VARCHAR(50) UNIQUE NOT NULL,
	description VARCHAR(200),
	monthly_fee NUMERIC(12,2) NOT NULL CHECK(monthly_fee >= 0),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,	

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


now = datetime.now()
cur.execute('''
DO
$do$

BEGIN
    IF NOT EXISTS (SELECT subs_id FROM subscriptions) THEN
        INSERT INTO subscriptions(
            subs_id, name, description, monthly_fee,
            date_added, add_emp_id, date_modified, 
			modify_emp_id, active
        )
        VALUES (
            1, 'basic', '\"basic\" subscription created during DB initialization',
            0, %s, 1, %s, 1, TRUE
        );
    END IF;
END;

$do$
''', (now, now))


#creating clients table
cur.execute('''
CREATE TABLE IF NOT EXISTS clients (
	client_id INT PRIMARY KEY CHECK (client_id > 0),
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
	password VARCHAR NOT NULL,
	subs_id INT NOT NULL CHECK (subs_id > 0),
	last_signin TIMESTAMP,
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL,
	active BOOLEAN NOT NULL,	

	FOREIGN KEY(subs_id)
	REFERENCES subscriptions(subs_id));
''')


#creating firmwares table
cur.execute('''
CREATE TABLE IF NOT EXISTS firmwares (
	fw_id INT PRIMARY KEY CHECK (fw_id > 0),
	name VARCHAR(30) NOT NULL,
        model VARCHAR(10) NOT NULL,
        version VARCHAR(10) NOT NULL,
        description VARCHAR(200),
        author_id INT CHECK (author_id > 0) NOT NULL,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,	

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
	status_id INT PRIMARY KEY CHECK (status_id > 0),
        status VARCHAR(30) UNIQUE,
        description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
    active BOOLEAN NOT NULL,
     
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
	ap_login VARCHAR(30) UNIQUE NOT NULL,
	ap_password VARCHAR(30) UNIQUE NOT NULL,
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
	active BOOLEAN NOT NULL,	

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
	curr_id INT PRIMARY KEY CHECK (curr_id > 0),
	currency VARCHAR(20) UNIQUE NOT NULL,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,	

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating units table
cur.execute('''
CREATE TABLE IF NOT EXISTS units (
	unit_id INT PRIMARY KEY CHECK (unit_id > 0),
        unit VARCHAR(30) NOT NULL UNIQUE,
        description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,	

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating suppliers table
cur.execute('''
CREATE TABLE IF NOT EXISTS suppliers (
	supplier_id INT PRIMARY KEY CHECK (supplier_id > 0),
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
	active BOOLEAN NOT NULL,

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating carriers table
cur.execute('''
CREATE TABLE IF NOT EXISTS carriers (
	carrier_id INT PRIMARY KEY CHECK (carrier_id > 0),
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
	active BOOLEAN NOT NULL,

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating shipping_types table
cur.execute('''
CREATE TABLE IF NOT EXISTS shipping_types (
        shipping_type_id INT PRIMARY KEY CHECK (shipping_type_id > 0),
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
	active BOOLEAN NOT NULL,

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
	status_id INT PRIMARY KEY CHECK (status_id > 0),
	status VARCHAR(30) NOT NULL,
	carrier_id INT CHECK (carrier_id > 0) NOT NULL,
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,

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
	sp_type_id INT PRIMARY KEY CHECK (sp_type_id > 0),
	name VARCHAR(50) NOT NULL,
	brand VARCHAR(50),
	model VARCHAR(50),
	version VARCHAR(50),
	description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,

	UNIQUE(name, brand, model, version),
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating sp_logistics
cur.execute('''
CREATE TABLE IF NOT EXISTS sp_logistics (
	shipment_id INT PRIMARY KEY CHECK (shipment_id > 0),
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
	active BOOLEAN NOT NULL,

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
	status_id INT PRIMARY KEY CHECK (status_id > 0),
	name VARCHAR(50) UNIQUE NOT NULL,
	description VARCHAR(200),
        date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,	

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


cur.execute('''
CREATE TABLE IF NOT EXISTS sp_orders (
	sp_order_id INT PRIMARY KEY CHECK (sp_order_id > 0),
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
	active BOOLEAN NOT NULL,	

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


#creating sp_order_details table
cur.execute('''
CREATE TABLE IF NOT EXISTS sp_order_details (
	detail_id INT PRIMARY KEY CHECK (detail_id > 0),
	type_id INT NOT NULL CHECK (type_id > 0),
	price_per_unit NUMERIC(12,2) NOT NULL CHECK(price_per_unit > 0),
	curr_id INT NOT NULL CHECK (curr_id > 0),
	amount NUMERIC(12,2) NOT NULL,
	unit_id INT NOT NULL CHECK (unit_id > 0),
	order_id INT NOT NULL CHECK (order_id > 0),
	date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,	

	FOREIGN KEY (type_id)
	REFERENCES sp_types(sp_type_id),
	FOREIGN KEY (curr_id)
	REFERENCES currencies(curr_id),
	FOREIGN KEY (unit_id)
	REFERENCES units(unit_id),
	FOREIGN KEY (order_id)
	REFERENCES sp_orders(sp_order_id),
	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creatomg sp_statuses table
cur.execute('''
CREATE TABLE IF NOT EXISTS sp_statuses (
	status_id INT PRIMARY KEY CHECK (status_id > 0),
	status VARCHAR(30) NOT NULL UNIQUE,
	description VARCHAR(200),
	date_added TIMESTAMP NOT NULL,
        add_emp_id INT NOT NULL CHECK(add_emp_id > 0),
	date_modified TIMESTAMP NOT NULL,
	modify_emp_id INT NOT NULL CHECK(modify_emp_id > 0),
	active BOOLEAN NOT NULL,	

	FOREIGN KEY (add_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (modify_emp_id)
	REFERENCES employees(emp_id));
''')


#creating sp_warehouse
cur.execute('''
CREATE TABLE IF NOT EXISTS sp_warehouse (
	sp_id INT PRIMARY KEY CHECK (sp_id > 0),
	type_id INT NOT NULL CHECK (type_id > 0),
	order_id INT NOT NULL CHECK (order_id > 0),
	status_id INT NOT NULL CHECK (status_id > 0),
	date_accepted TIMESTAMP NOT NULL,
	acc_emp_id INT NOT NULL CHECK (acc_emp_id > 0),
	date_used TIMESTAMP,
	used_emp_id INT CHECK (used_emp_id > 0),
	pr_serial_num VARCHAR(12) UNIQUE,
	active BOOLEAN NOT NULL,	

	FOREIGN KEY (type_id)
	REFERENCES sp_types(sp_type_id),
	FOREIGN KEY (order_id)
	REFERENCES sp_orders(sp_order_id),
	FOREIGN KEY (status_id)
	REFERENCES sp_statuses(status_id),
	FOREIGN KEY (acc_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (used_emp_id)
	REFERENCES employees(emp_id),
	FOREIGN KEY (pr_serial_num)
	REFERENCES products(serial_num));
''')


#creating error_logs table
cur.execute('''
CREATE TABLE IF NOT EXISTS error_logs (
	log_id INT PRIMARY KEY CHECK (log_id > 0),
        call_path TEXT NOT NULL,
        function_name VARCHAR(50) NOT NULL,
        line_number INT NOT NULL CHECK (line_number > 0),
        error_name VARCHAR(50) NOT NULL,
        description TEXT NOT NULL,
        date_added TIMESTAMP NOT NULL,
		active BOOLEAN NOT NULL);
''')


#creating tables_info table
cur.execute('''
CREATE TABLE IF NOT EXISTS tables_info (
        table_id INT PRIMARY KEY CHECK (table_id > 0),
        name VARCHAR(50) NOT NULL UNIQUE,
        description VARCHAR(200),
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL,
	active BOOLEAN NOT NULL);
''')


#creating access_rights table
cur.execute('''
CREATE TABLE IF NOT EXISTS access_rights (
	rec_id INT PRIMARY KEY CHECK (rec_id > 0),
	table_id INT NOT NULL CHECK (table_id > 0),
	dept_id INT NOT NULL CHECK (dept_id > 0),
	emp_type_id INT NOT NULL CHECK (emp_type_id > 0),
	date_added TIMESTAMP NOT NULL,
	date_modified TIMESTAMP NOT NULL,
	active BOOLEAN NOT NULL,	

	FOREIGN KEY (table_id)
	REFERENCES tables_info(table_id),
	FOREIGN KEY (dept_id)
	REFERENCES departments(dept_id),
	FOREIGN KEY (emp_type_id)
	REFERENCES employee_type);
''')


conn.commit()

cur.close()

conn.close()
