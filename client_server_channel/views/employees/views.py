from flask import Blueprint, render_template
from .. import view_utils as utls


employees = Blueprint('employees', __name__, url_prefix='/employees')


@employees.route('/login')
def login():
	return render_template(utls.url_join(['employees', 'login.html']))


@employees.route('/logout')
def logout():
	return 'employee log out page'


@employees.route('/account')
def account():
	return render_template(utls.url_join(['employees','account.html']))


@employees.route('/admin')
def admin():
	return render_template(utls.url_join(['employees','admin.html']))
