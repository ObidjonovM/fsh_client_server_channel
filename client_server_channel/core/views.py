from flask import Blueprint, render_template
from os.path import join


core = Blueprint('core', __name__)

@core.route('/')
def index():
	return render_template(join('core', 'index.html'))


@core.route('/about')
def about():
	return render_template(join('core', 'about.html'))


@core.route('/help')
def help():
	return render_template(join('core', 'help.html'))


@core.route('/contact')
def contact():
	return render_template(join('core', 'contact.html'))
