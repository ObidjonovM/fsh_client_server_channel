from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ProductC, ClientC
from .. import view_utils as utls

socket = Blueprint('socket', __name__, url_prefix='/socket')


@socket.route('/<ser_num>', methods=['GET', 'POST'])
def get_my_product(ser_num):
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'GET':
		my_product = ProductC.get_my_product(
				session['client']['id'],
				ser_num
				)
		if len(my_product['data']) > 0:
			return render_template(
				utls.url_join(['clients', 'socket.html']),
				my_product = my_product
			)

		return redirect(url_for('clients.my_products.get_my_products'))

	if request.method == 'POST':
		ProductC.update({
			'serial_num' : ser_num,
			'description' : request.form['desc']
		})

		return redirect(request.url)


@socket.route('/logs/<ser_num>', methods=['POST'])
def get_logs(ser_num):
	if request.method == 'POST':
		result = ProductC.get_all_states_in_range(
								ser_num,
								request.form['product_id'],
								request.form['start_date'],
								request.form['end_date']
							)
		return result


@socket.route('/info/<ser_num>', methods=['POST'])
def my_product_info(ser_num):
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ClientC.check_password(
					session['client']['id'],
					request.json['password']
		)
	if (result):
		return ProductC.my_product_info(
            		session['client']['id'],
                    ser_num
            	)

	return {
        'success' : False,
        'data' : {}
    }


@socket.route('/action', methods=['POST'])
def enter_action():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.enter_requested_action(request.json)

		return result


@socket.route('/get_current_state', methods=['POST'])
def get_current_state():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.get_current_state(
			request.json['ser_num'],
			request.json['product_id']
		)

		return result


@socket.route('/delete/<ser_num>', methods=['POST'])
def delete_product(ser_num):
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ClientC.check_password(
			session['client']['id'],
			request.form['password']
			)

		if (result):
			ProductC.update({
				'serial_num' : ser_num,
				'description' : None,
				'client_id' : None
			})

			return redirect(url_for('clients.my_products.get_my_products'))
		my_product = ProductC.get_my_product(
				session['client']['id'],
				ser_num
				)
		if len(my_product['data']) > 0:
			return render_template(
				utls.url_join(['clients', 'socket.html']),
				my_product = my_product
				)

		return redirect(url_for('clients.my_products.get_my_products'))