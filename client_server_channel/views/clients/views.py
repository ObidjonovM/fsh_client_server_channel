from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ClientC, SubscriptionC
from .. import view_utils as utls
from .subscription import subscription


clients = Blueprint('clients', __name__, url_prefix='/clients')
clients.register_blueprint(subscription)


@clients.route('/login')
def login():
        return render_template(utls.url_join(['clients', 'login.html']))
 

@clients.route('/logout')
def logout():
	return 'logout page'


@clients.route('/register')
def register():
	return render_template(utls.url_join(['clients','register.html']))


@clients.route('/account')
def account():
	return render_template(utls.url_join(['clients','account.html']))


@clients.route('/add', methods=['GET', 'POST'])
def add():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	if request.method == 'GET':
		names_ids = SubscriptionC.get_ids_names()
		if names_ids['success']:
			return render_template(
				utls.url_join(['clients', 'add.html']),
				names_ids = names_ids
			)

		return redirect(url_for('clients.all'))

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
			'email' : params['email'],
			'subs_id' : params['subs_id']
		})

		if result['success']:
			return redirect(url_for('clients.all'))

		return result


@clients.route('/get/<int:client_id>')
def get(client_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	client_info = ClientC.get(client_id)
	
	if len(client_info['data']) > 0:
		name_id = SubscriptionC.get(client_info['data']['subs_id'])
		
		return render_template(
			utls.url_join(['clients', 'get.html']),
			client_info = client_info,
			name_id = name_id
		)

	return redirect(url_for('clients.all'))


@clients.route('/all')
def all():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	clients_info = ClientC.get_all()
	if len(clients_info['data']) > 0:
		names_by_ids = SubscriptionC.get_names_by_ids(clients_info['data']['subs_id'])
	else:
		names_by_ids = ''
	
	return render_template(
		utls.url_join(['clients', 'all.html']),
		clients_info = clients_info,
		names_by_ids = names_by_ids
	)


@clients.route('/update/<int:client_id>', methods=['GET', 'POST'])
def update(client_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	if request.method == 'GET':
		client_info = ClientC.get(client_id)
		names_ids = SubscriptionC.get_ids_names()
		if names_ids['success']:
			if len(client_info['data']) > 0:
				return render_template(
					utls.url_join(['clients', 'update.html']),
					client_info = client_info,
					names_ids = names_ids
				)

		return redirect(url_for('clients.all'))

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
			'client_id' : client_id
		})

		if result['success']:
			return redirect(url_for('clients.all'))

		return result


@clients.route('/delete/<int:client_id>', methods=['DELETE'])
def delete(client_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	return ClientC.delete(client_id)
