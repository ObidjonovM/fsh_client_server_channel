from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import (EmployeeC, EmployeeTypeC, 
                                    EmployeeStatusC, DepartmentsC)
from .. import view_utils as utls
from .employee_type import employee_type
from .employee_status import employee_status


employees = Blueprint('employees', __name__, url_prefix='/employees')
employees.register_blueprint(employee_type)
employees.register_blueprint(employee_status)


@employees.route('/login', methods=['GET','POST'])
def login():
    if 'username' in session:
        return redirect(url_for('core.index'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['employees', 'login.html']), 
            user_exists = True, 
            wrong_password = False
        )

    if request.method == 'POST':
        result = EmployeeC.login(
            request.form['username'],
            request.form['password']
        )

        if not result['success']:
            return redirect(url_for('core.index'))

        if result['user_exists'] and not result['wrong_password']:
            session['username'] = request.form['username']
            session['employee'] = {}
            session['employee']['id'] = result['emp_id']
            session['employee']['dept_id'] = result['dept_id']
            session['employee']['type_id'] = result['emp_type_id']
            session['employee']['status_id'] = result['emp_status_id']
        
            return redirect(url_for('employees.account'))
        
        return render_template(
            utls.url_join(['employees', 'login.html']),
			user_exists = result['user_exists'],
			wrong_password = result['wrong_password']
        )


@employees.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        session.pop('employee')

    return redirect(url_for('core.index'))


@employees.route('/account')
def account():
    if not 'username' in session:
        return redirect(url_for('employees.login'))
	
    return render_template(utls.url_join(['employees','account.html']))


@employees.route('/admin')
def admin():
    if not 'username' in session:
        return redirect(url_for('employees.login'))
	
    return render_template(utls.url_join(['employees','admin.html']))


@employees.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['employees','add.html']),
            names_ids_type = EmployeeTypeC.get_ids_names()['data'],
            names_ids_status = EmployeeStatusC.get_ids_names()['data'],
            names_ids_departments = DepartmentsC.get_ids_names()['data']
        )

    if request.method == 'POST':
        params = request.form
        result = EmployeeC.add({
                    'dept_id' : params['dept_id'],
                    'emp_type_id' : params['type_id'],
                    'first_name' : params['first_name'],
                    'middle_name' : params['middle_name'],
                    'last_name' : params['last_name'],
                    'birth_date' : params['birth_date'],
                    'address_1' : params['address_1'],
                    'address_2' : params['address_2'],
                    'city' : params['city'],
                    'country' : params['country'],
                    'zipcode' : params['zipcode'],
                    'phone' : params['phone'],
                    'home_phone' : params['home_phone'],
                    'email' : params['email'],
                    'emp_status_id' : params['status_id']
        })
        if result['success']:
            return redirect(url_for('employees.all'))

        return result


@employees.route('/get/<int:emp_id>')
def get(emp_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    emp_info=EmployeeC.get(emp_id)
    if len(emp_info['data']) > 0:
        return render_template(
            utls.url_join(['employees','get.html']),
            emp_info=emp_info,
            name_id_type = EmployeeTypeC.get(
                emp_info['data']['emp_type_id']),
            name_id_status = EmployeeStatusC.get(
                emp_info['data']['emp_status_id']),
            name_id_departments = DepartmentsC.get(
                emp_info['data']['dept_id'])
        )

    return redirect(url_for('employees.all'))


@employees.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))
    
    employees=EmployeeC.get_all()

    return render_template(
        utls.url_join(['employees','all.html']),
        employees=employees,
        names_ids_type = EmployeeTypeC.get_names_by_ids(
            employees['data']['emp_type_id']),
        names_ids_status = EmployeeStatusC.get_names_by_ids(
            employees['data']['emp_status_id']),
        names_ids_departments = DepartmentsC.get_names_by_ids(
            employees['data']['dept_id'])
    )


@employees.route('/update/<int:emp_id>', methods=['GET', 'POST'])
def update(emp_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        emp_info = EmployeeC.get(emp_id)
        if len(emp_info['data']) > 0:
            return render_template(
                utls.url_join(['employees','update.html']),
                emp_info=emp_info['data'],
                names_ids_type = EmployeeTypeC.get_ids_names()['data'],
                names_ids_status = EmployeeStatusC.get_ids_names()['data'],
                names_ids_departments = DepartmentsC.get_ids_names()['data']
            )

        return redirect(url_for('employees.all'))

    if request.method == 'POST':
        params = request.form
        result = EmployeeC.update({
                    'dept_id' : params['dept_id'],
				    'emp_type_id' : params['type_id'],
                    'first_name' : params['first_name'],
                    'middle_name' : params['middle_name'],
                    'last_name' : params['last_name'],
                    'birth_date' : params['birth_date'],
                    'address_1' : params['address_1'],
                    'address_2' : params['address_2'],
                    'city' : params['city'],
                    'country' : params['country'],
                    'zipcode' : params['zipcode'],
                    'phone' : params['phone'],
                    'home_phone' : params['home_phone'],
                    'email' : params['email'],
                    'emp_status_id' : params['status_id'],
				    'emp_id' : emp_id
		})
        if result['success']:
            return redirect(url_for('employees.all'))

        return result


@employees.route('/delete/<int:emp_id>', methods=['DELETE'])
def delete(emp_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'DELETE':
        return EmployeeC.delete(emp_id)
