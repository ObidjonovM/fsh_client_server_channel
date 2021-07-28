from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import CategoriesC
from .. import view_utils as utls

category = Blueprint('category', __name__, url_prefix='/category')


@category.route('/add', methods=['GET', 'POST'])
def add():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

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
			'add_emp_id' : session['employee']['id'],
			'modify_emp_id' : session['employee']['id']
		})

		if result['success']:
			return redirect(url_for('products.category.all'))

		return result


@category.route('/get/<int:cat_id>')
def get(cat_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

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
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	cats_info = CategoriesC.get_all()
	
	if cats_info['success']:
		if len(cats_info['data']) > 0:
			return render_template(
				utls.url_join(['products', 'category', 'all.html']),
				cats_info = cats_info,
				names_by_ids = CategoriesC.get_names_by_ids(cats_info['data']['parent_cat_id'])
			)

		return render_template(
			utls.url_join(['products', 'category', 'all.html'],
				cats_info = cats_info
			)
		)

	return redirect(url_for('core.index'))            # TODO later!!!!


@category.route('/update/<int:cat_id>', methods=['GET', 'POST'])
def update(cat_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	if request.method == 'GET':
		cat_info = CategoriesC.get(cat_id)

		if len(cat_info['data']) > 0:
			return render_template(
				utls.url_join(['products', 'category', 'update.html']),
				cat_info = cat_info,
				ids_names = CategoriesC.get_other_pairs(
					cat_info['data']['category_id'])
			)

		return redirect(url_for('products.category.all'))

	if request.method == 'POST':
		params = request.form
		result = CategoriesC.update({
			'description' : params['desc'],
			'parent_cat_id' : params['parent_id'],
			'modify_emp_id' : session['employee']['id'],
			'category_id' : cat_id
		})

		if result['success']:
			return redirect(url_for('products.category.all'))

		return result


@category.route('/delete/<int:cat_id>', methods=['DELETE'])
def delete_category(cat_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	return CategoriesC.delete(cat_id)