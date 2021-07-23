from flask import Blueprint, render_template, request, url_for, redirect, session
from client_server_channel.controls import (ProductC, ProductInfoC, 
						DealerC, ClientC, FirmwareC, ProductStatusC)
from .. import view_utils as utls
from .category import category
from .product_info import product_info
from .dealer import dealer
from .status import status
from .firmware import firmware


products = Blueprint('products', __name__, url_prefix='/products')
products.register_blueprint(category)
products.register_blueprint(product_info)
products.register_blueprint(dealer)
products.register_blueprint(status)
products.register_blueprint(firmware)


@products.route('/products')
def product_list():
	return render_template(utls.url_join(['products','products.html']))


@products.route('/product/<int:pid>')
def product_page(pid):
	return render_template(utls.url_join(['products','product.html']))


@products.route('/add', methods=['GET', 'POST'])
def add():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	if request.method == 'GET':

		return render_template(
			utls.url_join(['products', 'add.html']),
			products_ids = ProductInfoC.get_ids_names(),
			dealers_ids = DealerC.get_ids_names(),
			clients_ids = ClientC.get_ids_names(),
			firmwares_ids = FirmwareC.get_ids_names(),
			status_ids = ProductStatusC.get_ids_names()
		)

	if request.method == 'POST':
		params = request.form
		result = ProductC.add({
			'product_id' : params['product_id'],
			'dealer_id' : params['dealer_id'],
			'client_id' : params['client_id'],
			'manufactured_date' : params['manufactured_date'],
			'firmware_id' : params['fw_id'],
			'status_id' : params['status_id'],
			'resp_emp_id' : session['employee']['id'],
			'add_emp_id' : session['employee']['id'],
			'modify_emp_id' : session['employee']['id']
		})

		if result['success']:
			return redirect(url_for('products.all'))

		return result


@products.route('/get/<serial_num>')
def get(serial_num):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	product_info = ProductC.get(serial_num)
	
	if len(product_info['data']) > 0:
		
		return render_template(
			utls.url_join(['products', 'get.html']),
			product_info = product_info,
			product_name = ProductInfoC.get(product_info['data']['product_id']),
			dealer_name = DealerC.get(product_info['data']['dealer_id']),
			client_name = ClientC.get(product_info['data']['client_id']),
			firmware_name = FirmwareC.get(product_info['data']['firmware_id']),
			status_name = ProductStatusC.get(product_info['data']['status_id'])
		)

	return redirect(url_for('products.all'))


@products.route('/all')
def all():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	products_info = ProductC.get_all()
	if products_info['success']:

		if len(products_info['data']) > 0:
		
			return render_template(
				utls.url_join(['products', 'all.html']),
				products_info = products_info,
				products_by_ids = ProductInfoC.get_names_by_ids(products_info['data']['product_id']),
				dealers_by_ids = DealerC.get_names_by_ids(products_info['data']['dealer_id']),
				clients_by_ids = ClientC.get_names_by_ids(products_info['data']['client_id']),
				firmwares_by_ids = FirmwareC.get_names_by_ids(products_info['data']['firmware_id']),
				status_by_ids = ProductStatusC.get_names_by_ids(products_info['data']['status_id'])
			)

		return render_template(utls.url_join(['products', 'all.html']))

	return redirect(url_for('core.index'))


@products.route('/update/<serial_num>', methods=['GET', 'POST'])
def update(serial_num):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	if request.method == 'GET':
		product_info = ProductC.get(serial_num)
	
		if len(product_info['data']) > 0:
			return render_template(
				utls.url_join(['products', 'update.html']),
				product_info = product_info,
				dealers_ids = DealerC.get_ids_names(),
				status_ids = ProductStatusC.get_ids_names(),
				product_name = ProductInfoC.get(product_info['data']['product_id']),
				clients_ids = ClientC.get(product_info['data']['client_id']),
				firmwares_ids = FirmwareC.get(product_info['data']['firmware_id']),
				resp_emp_id = session['employee']['id']
			)

		return redirect(url_for('products.all'))

	if request.method == 'POST':
		params = request.form
		result = ProductC.update({
			'dealer_id' : params['dealer_id'],
			'resp_emp_id' : session['employee']['id'],
			'status_id' : params['status_id'],
			'modify_emp_id' : session['employee']['id'],
			'serial_num' : serial_num
		})

		if result['success']:
			return redirect(url_for('products.all'))

		return result


@products.route('/delete/<serial_num>', methods=['DELETE'])
def delete(serial_num):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	return ProductC.delete(serial_num)