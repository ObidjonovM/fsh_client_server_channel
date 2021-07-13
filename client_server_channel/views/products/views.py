from flask import Blueprint, render_template, request, url_for, redirect
from .. import view_utils as utls
from .category import category
from .product_info import product_info
from .dealer import dealer


products = Blueprint('products', __name__, url_prefix='/products')
products.register_blueprint(category)
products.register_blueprint(product_info)
products.register_blueprint(dealer)


@products.route('/products')
def product_list():
	return render_template(utls.url_join(['products','products.html']))


@products.route('/product/<int:pid>')
def product_page(pid):
	return render_template(utls.url_join(['products','product.html']))
