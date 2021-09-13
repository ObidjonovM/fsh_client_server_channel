from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ProductInfoC, CategoriesC, ProductPhotoC
from .. import view_utils as utls

product_info = Blueprint('product_info', __name__, url_prefix='/info')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(format):
    return format.lower() in ALLOWED_EXTENSIONS

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
		params = request.json
		if not params['other_photos']:
			return {
				'success' : False,
				'comment' : "Fayl tanlanmadi"
			}

		for file in params['other_photos']:
			star = file.find("data:image/")
			end = file.find(";base64")
			format_img = file[star + 11:end]

			if file and not allowed_file(format_img):
				return {
					'success' : False,
					'comment' : "Siz faqat png, jpg, jpeg, gif formatdagi fayllarni saqlashingiz mumkin"
				}

		result = ProductInfoC.add({
			'name' : params['name'],
			'model' : params['model'],
			'main_photo' : params['main_photo'],
			'other_photos' : params['other_photos'],
			'category_id' : params['cat_id'],
			'add_emp_id' : session['employee']['id'],
			'modify_emp_id' : session['employee']['id']
		})

		if result['success']:
			return {
				'success' : True,
				'comment' : ''
			}
		
		return {
			'success' : False,
			'comment' : 'Serverda xatolik'
		}



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
			product_photo = ProductPhotoC.get(product_id)
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


@product_info.route('/<int:cat_id>', methods=['POST'])
def product_cat(cat_id):

	if request.method == 'POST':
		result = ProductInfoC.get_products_by_cat_id(cat_id)

		return result

