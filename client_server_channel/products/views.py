from flask import Blueprint, render_template
from os.path import join

products = Blueprint('products', __name__)


@products.route('/products')
def product_list():
	return render_template(join('products','products.html'))


@products.route('/product/<int:pid>')
def product_page(pid):
	return render_template(join('products','product.html'))
