from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ClientC, ProductC
from .. import view_utils as utls
from .subscription import subscription


clients = Blueprint('clients', __name__, url_prefix='/clients')
clients.register_blueprint(subscription)


@clients.route('/login', methods=['GET', 'POST'])
def login():
	if 'clientname' in session:
		return redirect(url_for('core.index'))

	if request.method == 'GET':
		return render_template(
			utls.url_join(['clients', 'login.html'])
		)

	if request.method == 'POST':
		result = ClientC.login(
			request.form['clientname'],
			request.form['password'],
			None
		)

		if result['success']:
			if result['user_exists'] and not result['wrong_password']:
				session['clientname'] = request.form['clientname']
				session['client'] = {}
				session['client']['id'] = result['client_id']
				session['client']['first_name'] = result['first_name']

				return redirect(url_for('core.index'))

		return render_template(
			utls.url_join(['clients', 'login.html'])
		)


@clients.route('/change_password', methods=['GET', 'POST'])
def change_password():

	if request.method == 'GET':
		return render_template(
			utls.url_join(['clients', 'change_password.html'])
		)

	if request.method == 'POST':
		result = ClientC.login(
			request.form['clientname'],
			request.form['password'],
			request.form['new_password']
		)

		if result['success']:
			if result['user_exists'] and not result['wrong_password']:
				return redirect(url_for('clients.account'))

		return render_template(
			utls.url_join(['clients', 'change_password.html'])
		)
 

@clients.route('/logout')
def logout():
	if 'clientname' in session:
		session.pop('clientname')
		session.pop('client')

	return redirect(url_for('core.index'))


@clients.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':

		return render_template(
			utls.url_join(['clients','register.html'])
		)

	if request.method == 'POST':
		params = request.form
		result = ClientC.add({
			'first_name' : params['first_name'],
			'last_name' : params['last_name'],
			'birth_date' : params['birth_date'],
			'address_1' : params['address_1'],
			'city' : params['city'],
			'country' : params['country'],
			'zipcode' : params['zipcode'],
			'phone' : params['phone'],
			'username' : params['username'],
			'password' : params['password']
		})

		if result['success']:
			return redirect(url_for('clients.login'))

		return result


@clients.route('/account')
def account():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	return render_template(utls.url_join(['clients','account.html']),
		first_name = session['client']['first_name']
	)


@clients.route('/my_products', methods=['GET', 'POST'])
def my_products():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'GET':
		return render_template(
			utls.url_join(['clients', 'my_products.html']),
			my_products = ProductC.get_my_products(session['client']['id'])
		)

	if request.method == 'POST':
		result = ProductC.update({
			'serial_num' : request.form['ser_num'],
			'description' : request.form['desc'],
			'client_id' : session['client']['id']
		})

		if result['success']:
			return redirect(url_for('clients.my_products'))

		return result


@clients.route('/smart_socket/on', methods=['POST'])
def turn_on():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.turn_on(request.json)

		return result


@clients.route('/smart_socket/off', methods=['POST'])
def turn_off():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.turn_off(request.json)

		return result


@clients.route('/info/<ser_num>', methods=['GET', 'POST'])
def product_info(ser_num):
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'GET':
		return render_template(
			utls.url_join(['clients', 'product_info.html']),
			my_product = ProductC.get(ser_num)
		)

	if request.method == 'POST':
		result = ProductC.get_logs(ser_num,
								request.form['product_id'],
								request.form['start_date'],
								request.form['end_date']
							)
		return result


@clients.route('/get')
def get():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	client_info = ClientC.get(session['client']['id'])
	
	if len(client_info['data']) > 0:
		
		return render_template(
			utls.url_join(['clients', 'get.html']),
			client_info = client_info,
		)

	return redirect(url_for('clients.account'))


@clients.route('/update', methods=['GET', 'POST'])
def update():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'GET':
		client_info = ClientC.get(session['client']['id'])

		if len(client_info['data']) > 0:
			return render_template(
				utls.url_join(['clients', 'update.html']),
				client_info = client_info,
			)

		return redirect(url_for('clients.account'))

	if request.method == 'POST':
		params = request.form
		result = ClientC.update({
			'first_name' : params['first_name'],
			'middle_name' : params['middle_name'],
			'last_name' : params['last_name'],
			'birth_date' : params['birth_date'],
			'address_1' : params['address_1'],
			'address_2' : params['address_2'],
			'city' : params['city'],
			'country' : params['country'],
			'zipcode' : params['zipcode'],
			'phone' : params['phone'],
			'home_phone' : params['home_phone'],
			'email' : params['email'],
			'client_id' : session['client']['id']
		})

		if result['success']:
			return redirect(url_for('clients.account'))

		return result


@clients.route('/delete', methods=['DELETE'])
def delete():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	return ClientC.delete(session['client']['id'])
