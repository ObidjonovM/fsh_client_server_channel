from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import DealerC
from .. import view_utils as utls

dealer = Blueprint('dealer', __name__, url_prefix='/dealer')


@dealer.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'GET':

		return render_template(
			utls.url_join(['products', 'dealer', 'add.html'])
		)

	if request.method == 'POST':
		params = request.form
		result = DealerC.add({
			'name' : params['name'],
			'address_1' : params['address_1'],
			'address_2' : params['address_2'],
			'city' : params['city'],
			'country' : params['country'],
			'zipcode' : params['zipcode'],
			'phone' : params['phone'],
			'email' : params['email'],
			'website' : params['website'],
			'geo_location' : params['geo_location'],
		})

		if result['success']:
			return redirect(url_for('products.dealer.all'))

		return result


@dealer.route('/get/<int:dealer_id>')
def get(dealer_id):
	dealer_info = DealerC.get(dealer_id)
	
	if len(dealer_info['data']) > 0:
		
		return render_template(
			utls.url_join(['products', 'dealer', 'get.html']),
			dealer_info = dealer_info
		)

	return redirect(url_for('products.dealer.all'))


@dealer.route('/all')
def all():
	dealers_info = DealerC.get_all()
	
	return render_template(
		utls.url_join(['products', 'dealer', 'all.html']),
		dealers_info = dealers_info
	)


@dealer.route('/update/<int:dealer_id>', methods=['GET', 'POST'])
def update(dealer_id):
	if request.method == 'GET':
		dealer_info = DealerC.get(dealer_id)
	
		if len(dealer_info['data']) > 0:
			return render_template(
				utls.url_join(['products', 'dealer', 'update.html']),
				dealer_info = dealer_info
			)

		return redirect(url_for('products.dealer.all'))

	if request.method == 'POST':
		params = request.form
		result = DealerC.update({
			'name' : params['name'],
			'address_1' : params['address_1'],
			'address_2' : params['address_2'],
			'city' : params['city'],
			'country' : params['country'],
			'zipcode' : params['zipcode'],
			'phone' : params['phone'],
			'email' : params['email'],
			'website' : params['website'],
			'geo_location' : params['geo_location'],
			'dealer_id' : dealer_id
		})

		if result['success']:
			return redirect(url_for('products.dealer.all'))

		return result


@dealer.route('/delete/<int:dealer_id>', methods=['DELETE'])
def delete(dealer_id):
	return DealerC.delete(dealer_id)