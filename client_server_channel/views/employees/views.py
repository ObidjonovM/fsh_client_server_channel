from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import (EmployeeC, DepartmentsC,
                                            EmployeeStatusC, DepartmentsC)
from .. import view_utils as utls
from .employee_type import employee_type


employees = Blueprint('employees', __name__, url_prefix='/employees')
employees.register_blueprint(employee_type)


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


@employees.route('/add', methods=['GET', 'POST'])
def add():
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
            return redirect(url_for('employees.get_all'))
        
        return result


@employees.route('/get/<int:emp_id>')
def get(emp_id):
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
    
    return redirect(url_for('employees.get_all'))


@employees.route('/get_all')
def get_all():
    employees=EmployeeC.get_all()

    return render_template(
        utls.url_join(['employees','get_all.html']),
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
        
        return redirect(url_for('employees.get_all'))

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
            return redirect(url_for('employees.get_all'))

        return result


@employees.route('/delete/<int:emp_id>', methods=['DELETE'])
def delete(emp_id):
    if request.method == 'DELETE':
        return EmployeeC.delete(emp_id)


@employees.route('/add_status', methods=['GET', 'POST'])
def add_status():
    if request.method == 'GET':
        return render_template(utls.url_join(['employees','add_status.html']))

    if request.method == 'POST':
        result = EmployeeStatusC.add(request.form['status'], request.form['desc'])
        if result['success']:
            return redirect(url_for('employees.get_status_all'))

        return result


@employees.route('get_status/<int:status_id>')
def get_status(status_id):
    status_info=EmployeeStatusC.get(status_id)
    if status_info['data'] == []:
        return redirect(
            url_for('employees.get_status_all')
        )

    return render_template(
        utls.url_join(['employees', 'get_status.html']),
        status_info = status_info
    )


@employees.route('/get_status_all')
def get_status_all():
    return render_template(
        utls.url_join(['employees', 'get_status_all.html']),
        status_all = EmployeeStatusC.get_all()
    )


@employees.route('/update_status/<int:status_id>', methods=['GET', 'POST'])
def update_status(status_id):
    if request.method == 'GET':
        status_info = EmployeeStatusC.get(status_id)
        if len(status_info['data']) > 0:
            return render_template(
                utls.url_join(['employees', 'update_status.html']),
                status_info = status_info['data']
            )

        return redirect(url_for('employees.get_status_all'))

    if request.method == 'POST':
        result = EmployeeStatusC.update({
            'description' : request.form['desc'],
            'status_id' : status_id
        })
        if result['success']:
            return redirect(url_for('employees.get_status_all'))

        return result


@employees.route('/delete_status/<int:status_id>', methods=['DELETE'])
def delete_status(status_id):
    if request.method == 'DELETE':
        return EmployeeStatusC.delete(status_id)  
