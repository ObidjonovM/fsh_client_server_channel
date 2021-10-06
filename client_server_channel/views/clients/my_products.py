from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ProductC
import json
from .. import view_utils as utls
from .socket import socket

my_products = Blueprint('my_products', __name__, url_prefix='/my_products')
my_products.register_blueprint(socket)


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