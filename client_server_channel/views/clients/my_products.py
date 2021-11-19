from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ProductC
import json
from .. import view_utils as utls
from .my_product import my_product

my_products = Blueprint('my_products', __name__, url_prefix='/my_products')
my_products.register_blueprint(my_product)


@my_products.route('/', methods=['GET', 'POST'])
def get_my_products(): 
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
		}, True)

		if result['success']:
			return redirect(url_for('clients.my_products.get_my_products'))

		return json.dumps(result, ensure_ascii=False)


@my_products.route('/get_current_states', methods=['POST'])
def get_current_states():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.get_current_states(
			request.json['ser_nums'],
			request.json['prefixs']
		)

		return result


@my_products.route('/setup_info')
def setup_info():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	return render_template(
		utls.url_join(['clients', 'setup_info.html'])
	)


@my_products.route('/update_prev_state', methods=['POST'])
def update_prev_state():
	if not 'clientname' in session:
		return redirect(url_for('clients.login'))

	if request.method == 'POST':
		result = ProductC.update({
			'serial_num': request.json['ser_num'],
			'state_change_time': utls.parse_time(request.json['state_time'])
		})

		return result