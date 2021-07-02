from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import EmployeeTypeC, EmployeeC, EmployeeStatusC
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


@employees.route('/add_type', methods=['GET','POST'])
def add_type():

    if request.method == 'GET':
        return render_template(utls.url_join(['employees','add_type.html']))

    if request.method == 'POST':
        result = EmployeeTypeC.add(request.form['type_name'], request.form['desc'])
        if result['success']:
            return redirect(url_for('employees.get_types'))
        
        return result


@employees.route('/get_type/<int:type_id>')
def get_type(type_id):
        type_info=EmployeeTypeC.get(type_id)
        if type_info['data'] == []:
            return redirect(
                url_for('employees.get_types')
            )

        return render_template(
            utls.url_join(['employees','get_type.html']),
            type_info=type_info
        )


@employees.route('/get_types')
def get_types():
    return render_template(
        utls.url_join(['employees','get_types.html']), 
        types=EmployeeTypeC.get_all()
    )


@employees.route('/update_type/<int:type_id>', methods=['GET', 'POST'])
def update_type(type_id):
    if request.method == 'GET':
        type_info = EmployeeTypeC.get(type_id)
        if len(type_info['data']) > 0:
            return render_template(
                utls.url_join(['employees','update_type.html']), 
                type_info=type_info['data']
            )
        
        return redirect(url_for('employees.get_types'))

    if request.method == 'POST':
        result = EmployeeTypeC.update({
				    'description' : request.form['desc'],
				    'emp_type_id' : type_id
				     })
        if result['success']:
            return redirect(url_for('employees.get_types'))
        
        return result


@employees.route('/delete_type/<int:type_id>', methods=['DELETE'])
def delete_type(type_id):
    if request.method == 'DELETE':
        return EmployeeTypeC.delete(type_id)


@employees.route('/type_exists', methods=['POST'])
def type_exists():
    try:
        return EmployeeTypeC.type_exists(
            request.form['type_name']
        )
    except:
        return {
            'error' : 'Invalid input'
        }


@employees.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template(
            utls.url_join(['employees','add.html']),
            names_ids = EmployeeTypeC.get_ids_names()
        )

    if request.method == 'POST':
        params = request.form
        result = EmployeeC.add({
                    'emp_type_id' : params['emp_type_id'],
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
                    'email' : params['email'],
        })
        if result['success']:
            return redirect(url_for('employees.get_all'))
        
        return result


@employees.route('/get/<int:emp_id>')
def get(emp_id):
    return render_template(
        utls.url_join(['employees','get.html']), 
        emp_info=EmployeeC.get(emp_id)
    )


@employees.route('/get_all')
def get_all():
    return render_template(
        utls.url_join(['employees','get_all.html']), 
        employees=EmployeeC.get_all(),
        names_ids = EmployeeTypeC.get_ids_names()
    )


@employees.route('/update/<int:emp_id>', methods=['GET', 'POST'])
def update(emp_id):
    if request.method == 'GET':
        emp_info = EmployeeC.get(emp_id)
        if len(emp_info['data']) > 0:
            return render_template(
                utls.url_join(['employees','update.html']), 
                emp_info=emp_info['data']
            )
        
        return redirect(url_for('employees.get_all'))

    if request.method == 'POST':
        params = request.form
        result = EmployeeC.update({
				    'emp_type_id' : params['emp_type_id'],
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
                    'email' : params['email'],
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