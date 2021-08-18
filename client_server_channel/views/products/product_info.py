from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from client_server_channel.controls import ProductInfoC, CategoriesC, ProductPhotoC
from .. import view_utils as utls

product_info = Blueprint('product_info', __name__, url_prefix='/info')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@product_info.route('/add', methods=['GET', 'POST'])
def add():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	ids_names = CategoriesC.get_leaf_cat()
	if request.method == 'GET':

		return render_template(
			utls.url_join(['products', 'product_info', 'add.html']),
			ids_names = ids_names
		)

	if request.method == 'POST':
		params = request.form

		if 'foto' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['foto']
        
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)

		if file and allowed_file(file.filename):
			
			result = ProductInfoC.add({
				'name' : params['name'],
				'model' : params['model'],
				'foto' : request.files['foto'],
				'category_id' : params['cat_id'],
				'add_emp_id' : session['employee']['id'],
				'modify_emp_id' : session['employee']['id']
			})

			if result['success']:
				return redirect(url_for('products.product_info.all'))
		
		return redirect(request.url)



@product_info.route('/get/<int:product_id>')
def get(product_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	product_info = ProductInfoC.get(product_id)
	
	if len(product_info['data']) > 0:
		
		return render_template(
			utls.url_join(['products', 'product_info', 'get.html']),
			product_info = product_info,
			id_name = CategoriesC.get(product_info['data']['category_id']),
			product_photo = ProductPhotoC.get(product_info['data']['photo_id'])
		)

	return redirect(url_for('products.product_info.all'))


@product_info.route('/all')
def all():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	products_info = ProductInfoC.get_all()

	if products_info['success']:
		if len(products_info['data']) > 0:
			return render_template(
				utls.url_join(['products', 'product_info', 'all.html']),
				products_info = products_info,
				names_by_ids = CategoriesC.get_names_by_ids(products_info['data']['category_id'])
			)

		return render_template(
			utls.url_join(['products', 'product_info', 'all.html']),
				products_info = products_info
		)

	return redirect(url_for('core.index'))            # TODO later!!!!


@product_info.route('/delete/<int:product_id>', methods=['DELETE'])
def delete(product_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	return ProductInfoC.delete(product_id)