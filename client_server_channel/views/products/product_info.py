from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import ProductInfoC, CategoriesC
from .. import view_utils as utls

product_info = Blueprint('product_info', __name__, url_prefix='/info')


@product_info.route('/add', methods=['GET', 'POST'])
def add():
	ids_names = CategoriesC.get_ids_names()
	if request.method == 'GET':

		return render_template(
			utls.url_join(['products', 'product_info', 'add.html']),
			ids_names = ids_names
		)

	if request.method == 'POST':
		params = request.form
		result = ProductInfoC.add({
			'name' : params['name'],
			'model' : params['model'],
			'category_id' : params['cat_id'],
		})

		if result['success']:
			return redirect(url_for('products.product_info.all'))

		return result


@product_info.route('/get/<int:product_id>')
def get(product_id):
	product_info = ProductInfoC.get(product_id)
	
	if len(product_info['data']) > 0:
		
		return render_template(
			utls.url_join(['products', 'product_info', 'get.html']),
			product_info = product_info,
			id_name = CategoriesC.get(product_info['data']['category_id'])
		)

	return redirect(url_for('products.product_info.all'))


@product_info.route('/all')
def all():
    products_info = ProductInfoC.get_all()
    if len(products_info['data']) > 0:
        names_by_ids = CategoriesC.get_names_by_ids(products_info['data']['category_id'])
    else:
        names_by_ids = ''

    return render_template(
        utls.url_join(['products', 'product_info', 'all.html']),
        products_info = products_info,
        names_by_ids = names_by_ids
        )


@product_info.route('/delete/<int:product_id>', methods=['DELETE'])
def delete(product_id):
	return ProductInfoC.delete(product_id)