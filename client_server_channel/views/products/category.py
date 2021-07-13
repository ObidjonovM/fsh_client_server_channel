from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import CategoriesC
from .. import view_utils as utls

category = Blueprint('category', __name__, url_prefix='/category')


@category.route('/add', methods=['GET', 'POST'])
def add():
	ids_names = CategoriesC.get_ids_names()
	if request.method == 'GET':

		return render_template(
			utls.url_join(['products', 'category', 'add.html']),
			ids_names = ids_names
		)

	if request.method == 'POST':
		params = request.form
		result = CategoriesC.add({
			'name' : params['name'],
			'description' : params['desc'],
			'parent_cat_id' : params['parent_id'],
		})

		if result['success']:
			return redirect(url_for('products.category.all'))

		return result


@category.route('/get/<int:cat_id>')
def get(cat_id):
	cat_info = CategoriesC.get(cat_id)
	
	if len(cat_info['data']) > 0:
		
		return render_template(
			utls.url_join(['products', 'category', 'get.html']),
			cat_info = cat_info,
			id_name = CategoriesC.get(cat_info['data']['parent_cat_id'])
		)

	return redirect(url_for('products.category.all'))


@category.route('/all')
def all():
	cats_info = CategoriesC.get_all()
	
	return render_template(
		utls.url_join(['products', 'category', 'all.html']),
		cats_info = cats_info,
		names_by_ids = CategoriesC.get_names_by_ids(cats_info['data']['parent_cat_id'])
	)


@category.route('/update/<int:cat_id>', methods=['GET', 'POST'])
def update(cat_id):
	if request.method == 'GET':
		cat_info = CategoriesC.get(cat_id)
	
		if len(cat_info['data']) > 0:
			return render_template(
				utls.url_join(['products', 'category', 'update.html']),
				cat_info = cat_info,
				ids_names = CategoriesC.get_ids_names()
			)

		return redirect(url_for('products.category.all'))

	if request.method == 'POST':
		params = request.form
		result = CategoriesC.update({
			'description' : params['desc'],
			'parent_cat_id' : params['parent_id'],
			'category_id' : cat_id
		})

		if result['success']:
			return redirect(url_for('products.category.all'))

		return result


@category.route('/delete/<int:cat_id>', methods=['DELETE'])
def delete_category(cat_id):
	return CategoriesC.delete(cat_id)