from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ClientC
from .. import view_utils as utls
from .subscription import subscription


clients = Blueprint('clients', __name__, url_prefix='/clients')
clients.register_blueprint(subscription)


@clients.route('/login', methods=['GET', 'POST'])
def login():
	if 'clientname' in session:
		return redirect(url_for('clients.account'))

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
				session['clients'] = {}
				session['clients']['id'] = result['client_id']

				return redirect(url_for('clients.account'))

		return render_template(
			utls.url_join(['clients', 'login.html'])
		)


@clients.route('/change_password', methods=['GET', 'POST'])
def change_password():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

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
		session.pop('clients')

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
			'email' : params['email']
		})

		if result['success']:
			return redirect(url_for('clients.login'))

		return result


@clients.route('/account')
def account():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	return render_template(utls.url_join(['clients','account.html']))


@clients.route('/get')
def get():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	client_info = ClientC.get(session['clients']['id'])
	
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
		client_info = ClientC.get(session['clients']['id'])

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
			'subs_id' : params['subs_id'],
			'client_id' : session['clients']['id']
		})

		if result['success']:
			return redirect(url_for('clients.account'))

		return result


@clients.route('/delete', methods=['DELETE'])
def delete():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	return ClientC.delete(session['clients']['id'])
