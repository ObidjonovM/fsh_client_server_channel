from flask import Blueprint, render_template
from client_server_channel.controls import CategoriesC
from .. import view_utils as utls

core = Blueprint('core', __name__)

@core.route('/')
def index():
	return render_template(utls.url_join(['core', 'index.html']),
		first_parent = CategoriesC.get_first_par_cat()
	)


@core.route('/category/<int:cat_id>')
def get_category(cat_id):
	return render_template(utls.url_join(['core', 'category.html']),
		sub_cat_product = CategoriesC.get_product_or_sub_cat(cat_id)
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
