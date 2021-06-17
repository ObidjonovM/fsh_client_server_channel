from flask import Blueprint, render_template
from os.path import join


clients = Blueprint('clients', __name__)


@clients.route('/login')
def login():
	return render_template(join('clients','login.html'))


@clients.route('/logout')
def logout():
	return 'logout page'


@clients.route('/register')
def register():
	return render_template(join('clients','register.html'))


@clients.route('/account')
def account():
	return render_template(join('clients','account.html'))
