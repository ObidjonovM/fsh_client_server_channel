from client_server_channel.models.products.categories import CategoriesTable
from flask import Blueprint, render_template
from client_server_channel.controls import CategoriesC
from .. import view_utils as utls

core = Blueprint('core', __name__)

@core.route('/')
def index():
	return render_template(utls.url_join(['core', 'index.html']),
		all_cat = CategoriesTable.get_all()
	)


@core.route('/category/<int:cat_id>')
def get_category(cat_id):
	return render_template(utls.url_join(['core', 'category.html']),
		product_by_cat_id = CategoriesC.get_product_by_cat_id(cat_id)
	)


@core.route('/about')
def about():
	return render_template(utls.url_join(['core', 'about.html']))


@core.route('/help')
def help():
	return render_template(utls.url_join(['core', 'help.html']))


@core.route('/contact')
def contact():
	return render_template(utls.url_join(['core', 'contact.html']))
