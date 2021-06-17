from flask import Blueprint, render_template
from .. import view_utils as utls

core = Blueprint('core', __name__)

@core.route('/')
def index():
	return render_template(utls.url_join(['core', 'index.html']))


@core.route('/about')
def about():
	return render_template(utls.url_join(['core', 'about.html']))


@core.route('/help')
def help():
	return render_template(utls.url_join(['core', 'help.html']))


@core.route('/contact')
def contact():
	return render_template(utls.url_join(['core', 'contact.html']))
