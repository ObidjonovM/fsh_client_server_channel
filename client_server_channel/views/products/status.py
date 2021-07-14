from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import ProductStatusC
from .. import view_utils as utls

status = Blueprint('status', __name__, url_prefix='/status')


@status.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'GET':

		return render_template(
			utls.url_join(['products', 'status', 'add.html'])
		)

	if request.method == 'POST':
		params = request.form
		result = ProductStatusC.add({
			'status' : params['status'],
			'description' : params['desc']
		})

		if result['success']:
			return redirect(url_for('products.status.all'))

		return result


@status.route('/get/<int:status_id>')
def get(status_id):
	status_info = ProductStatusC.get(status_id)
	
	if len(status_info['data']) > 0:
		
		return render_template(
			utls.url_join(['products', 'status', 'get.html']),
			status_info = status_info
		)

	return redirect(url_for('products.status.all'))


@status.route('/all')
def all():
	status_info = ProductStatusC.get_all()
	
	return render_template(
		utls.url_join(['products', 'status', 'all.html']),
		status_info = status_info
	)


@status.route('/update/<int:status_id>', methods=['GET', 'POST'])
def update(status_id):
	if request.method == 'GET':
		status_info = ProductStatusC.get(status_id)
	
		if len(status_info['data']) > 0:
			return render_template(
				utls.url_join(['products', 'status', 'update.html']),
				status_info = status_info
			)

		return redirect(url_for('products.status.all'))

	if request.method == 'POST':
		params = request.form
		result = ProductStatusC.update({
			'status' : params['status'],
			'description' : params['desc'],
			'status_id' : status_id
		})

		if result['success']:
			return redirect(url_for('products.status.all'))

		return result


@status.route('/delete/<int:status_id>', methods=['DELETE'])
def delete(status_id):
	return ProductStatusC.delete(status_id)