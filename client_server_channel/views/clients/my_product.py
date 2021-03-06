from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ProductC, ClientC
from .. import view_utils as utls

my_product = Blueprint('my_product', __name__, url_prefix='/my_product')


@my_product.route('/<ser_num>', methods=['GET', 'POST'])
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
				utls.url_join(['clients', 'my_product.html']),
				my_product = my_product
			)

		return redirect(url_for('clients.my_products.get_my_products'))

	if request.method == 'POST':
		ProductC.update({
			'serial_num' : ser_num,
			'description' : request.form['desc']
		})

		return redirect(request.url)


@my_product.route('/logs/<ser_num>', methods=['POST'])
def get_logs(ser_num):
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		if request.json['device_type'] == '5':
			result = ProductC.requested_actions_in_range(
								ser_num,
								request.json['prefix'],
								request.json['start_date'],
								request.json['end_date']
							)
		else:
			result = ProductC.get_all_states_in_range(
									ser_num,
									request.json['prefix'],
									request.json['start_date'],
									request.json['end_date']
								)
		return result


@my_product.route('/get_measurements/<ser_num>', methods=['POST'])
def get_measurements(ser_num):
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.get_all_measurements_date_range(
							ser_num,
							request.json['prefix'],
							request.json['start_date'],
							request.json['end_date']
						)
		return result


@my_product.route('/get_gas_values/<ser_num>', methods=['POST'])
def get_gas_values(ser_num):
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':

		result = ProductC.get_gas_values(
							ser_num,
							request.json['prefix'],
							request.json['start_date'],
							request.json['end_date']
						)
		return result


@my_product.route('/info/<ser_num>', methods=['POST'])
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


@my_product.route('/action', methods=['POST'])
def enter_action():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		if request.json['prefix'] == 'socket3x':
			return ProductC.enter_requested_actions(request.json)

		result = ProductC.enter_requested_action(
			request.json['serial_num'],
			request.json['action_requested'],
			request.json['prefix']
			)

		return result


@my_product.route('/get_current_state', methods=['POST'])
def get_current_state():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		get_result = ProductC.get(request.json['ser_num'])
		if request.json['device_type'] == '5':
			result = ProductC.last_requested_action(
				request.json['ser_num'],
				request.json['prefix']
			)
			del result['action_requested']
			del result['requested_time']
			if result['action_taken'] == 'YES':
				result['state_change_time'] = result['action_time']
			else:
				result['state_change_time'] = get_result['data']['state_change_time']
		else:
			result = ProductC.get_current_state(
				request.json['ser_num'],
				request.json['prefix']
			)
		result['prev_state_time'] = get_result['data']['state_change_time']

		return result


@my_product.route('/get_last_measurement', methods=['POST'])
def get_last_measurement():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.get_last_measurement(
			request.json['ser_num'],
			request.json['prefix']
		)

		return result


@my_product.route('/last_request_time', methods=['POST'])
def last_request_time():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.last_request_time(
			request.json['ser_num'],
			request.json['prefix']
		)

		return result


@my_product.route('/last_gas_value', methods=['POST'])
def last_gas_value():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.last_gas_value(
			request.json['ser_num'],
			request.json['prefix']
		)

		return result


@my_product.route('/delete/<ser_num>', methods=['POST'])
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
				utls.url_join(['clients', 'my_product.html']),
				my_product = my_product
				)

		return redirect(url_for('clients.my_products.get_my_products'))