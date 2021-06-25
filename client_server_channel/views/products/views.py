from flask import Blueprint, render_template
from .. import view_utils as utls


products = Blueprint('products', __name__)


@products.route('/products')
def product_list():
	return render_template(utls.url_join(['products','products.html']))


@products.route('/product/<int:pid>')
def product_page(pid):
	return render_template(utls.url_join(['products','product.html']))
