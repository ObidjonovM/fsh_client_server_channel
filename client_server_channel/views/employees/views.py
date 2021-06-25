from flask import Blueprint, render_template, request, redirect, url_for
from .. import view_utils as utls
from client_server_channel.controls import EmployeeTypeC

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


@employees.route('/add_type', methods=['GET','POST'])
def add_type():

    if request.method == 'GET':
        return render_template(utls.url_join(['employees','add_type.html']))

    if request.method == 'POST':
        result = EmployeeTypeC.add(request.form['type_name'], request.form['desc'])
        return result


@employees.route('/get_type/<int:type_id>')
def get_type(type_id):
    type_info = EmployeeTypeC.get(type_id)
    return render_template(utls.url_join(['employees','get_type.html']), type_info=type_info)


@employees.route('/get_types')
def get_types():
    types = EmployeeTypeC.get_all()
    return render_template(utls.url_join(['employees','get_types.html']), types=types)


@employees.route('/update_type/<int:type_id>', methods=['GET', 'POST'])
def update_type(type_id):
    if request.method == 'GET':
        type_info = EmployeeTypeC.get(type_id)
        if len(type_info['data']) > 0:
            return render_template(utls.url_join(['employees','update_type.html']), type_info=type_info['data'])
        else:
            return(redirect(url_for('employees.get_types')))

    if request.method == 'POST':
        result = EmployeeTypeC.update({
				    'description' : request.form['desc'],
				    'emp_type_id' : type_id
				     })
        return result


@employees.route('/delete_type/<int:type_id>', methods=['DELETE'])
def delete_type(type_id):
    if request.method == 'DELETE':
        return EmployeeTypeC.delete(type_id)
        
        


        
