from flask import Blueprint, render_template
from .. import view_utils as utls
from .subscription import subscription

clients = Blueprint('clients', __name__, url_prefix='/clients')
clients.register_blueprint(subscription)


@clients.route('/login')
def login():
        return render_template(utls.url_join(['clients', 'login.html']))
 

@clients.route('/logout')
def logout():
	return 'logout page'


@clients.route('/register')
def register():
	return render_template(utls.url_join(['clients','register.html']))


@clients.route('/account')
def account():
	return render_template(utls.url_join(['clients','account.html']))
