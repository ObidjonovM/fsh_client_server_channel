from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ClientC, SubscriptionC
import json
from .. import view_utils as utls
from .subscription import subscription
from .my_products import my_products


clients = Blueprint('clients', __name__, url_prefix='/clients')
clients.register_blueprint(subscription)
clients.register_blueprint(my_products)

@clients.route('/')
def clients_page():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	return render_template(
		utls.url_join(['clients', 'clients.html'])
	)

@clients.route('/login', methods=['GET', 'POST'])
def login():
	if 'clientname' in session:
		return redirect(url_for('core.index'))

	if request.method == 'GET':
		return render_template(
			utls.url_join(['clients', 'login.html']),
			user_exists = True,
			wrong_password = False
		)

	if request.method == 'POST':
		result = ClientC.login(
			request.form['clientname'],
			request.form['password']
		)

		if result['success']:
			if result['user_exists'] and not result['wrong_password']:
				session['clientname'] = request.form['clientname']
				session['client'] = {}
				session['client']['id'] = result['client_id']
				session['client']['first_name'] = result['first_name']

				return redirect(url_for('core.index'))

		return render_template(
			utls.url_join(['clients', 'login.html']),
			user_exists = result['user_exists'],
			wrong_password = result['wrong_password']
		)


@clients.route('/change_password', methods=['GET', 'POST'])
def change_password():

	if request.method == 'GET':
		return render_template(
			utls.url_join(['clients', 'change_password.html']),
			user_exists = True,
			wrong_password = False
		)

	if request.method == 'POST':
		result = ClientC.login(
			request.form['clientname'],
			request.form['password'],
			request.form['new_password']
		)

		if result['success']:
			if result['user_exists'] and not result['wrong_password']:
				return redirect(url_for('clients.login'))

		return render_template(
			utls.url_join(['clients', 'change_password.html']),
			user_exists = result['user_exists'],
			wrong_password = result['wrong_password']
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
			'phone' : params['phone'],
			'email' : params['email'],
			'username' : params['clientname'],
			'password' : params['password']
		})

		if result['success']:
			return redirect(url_for('clients.login'))

		return result


@clients.route('/user_exists', methods=['POST'])
def user_exists():
	if request.method == 'POST':
		result = ClientC.user_exists(request.json['name'])

		return result


@clients.route('/account')
def account():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	return render_template(utls.url_join(['clients','account.html']),
		first_name = session['client']['first_name']
	)


@clients.route('/get/<int:client_id>')
def get(client_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	client_info = ClientC.get(client_id)
	
	if len(client_info['data']) > 0:
		
		return render_template(
			utls.url_join(['clients', 'get.html']),
			client_info = client_info,
			name_sub_id = SubscriptionC.get(client_info['data']['subs_id'])
		)

	return redirect(url_for('clients.account'))


@clients.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))
    
    clients_info=ClientC.get_all()

    if clients_info['success']:
        if len(clients_info['data']) > 0:
            return render_template(
                utls.url_join(['clients','all.html']),
                clients_info=clients_info,
				names_ids_subs = SubscriptionC.get_names_by_ids(
                    clients_info['data']['subs_id']),
            )

        return render_template(
            utls.url_join(['clients','all.html']),
                clients_info = clients_info
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


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
