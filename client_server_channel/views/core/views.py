from flask import Blueprint, render_template, request, redirect
from client_server_channel.controls import CategoriesC, ProductInfoC
from .. import view_utils as utls

core = Blueprint('core', __name__)

@core.route('/', methods = ['GET', 'POST'])
def index():

	if request.method == 'GET':
		return render_template(utls.url_join(['core', 'index.html']),
			get_products = ProductInfoC.get_all_info()
		)

	if request.method == 'POST':
		result = CategoriesC.get_sub_cat(request.json['cat_id'])
		if result['success']:
			return result

		return redirect(request.url)


@core.route('/about')
def about():
	return render_template(utls.url_join(['core', 'about.html']))


@core.route('/help')
def help():
	return render_template(utls.url_join(['core', 'help.html']))


@core.route('/contact')
def contact():
	return render_template(utls.url_join(['core', 'contact.html']))
