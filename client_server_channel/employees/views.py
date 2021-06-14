from flask import Blueprint, render_template
from os.path import join


employees = Blueprint('employees', __name__, url_prefix='/employees')


@employees.route('/login')
def login():
	return render_template(join('employees', 'login.html'))


@employees.route('/logout')
def logout():
	return 'employee log out page'


@employees.route('/account')
def account():
	return render_template(join('employees','account.html'))


@employees.route('/admin')
def admin():
	return render_template(join('employees','admin.html'))
