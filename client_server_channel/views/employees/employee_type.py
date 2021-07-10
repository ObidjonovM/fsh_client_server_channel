from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import EmployeeTypeC
from .. import view_utils as utls

employee_type = Blueprint('employee_type', __name__)


@employee_type.route('/add_type', methods=['GET','POST'])
def add_type():

    if request.method == 'GET':
        return render_template(utls.url_join(['employees','add_type.html']))

    if request.method == 'POST':
        result = EmployeeTypeC.add(request.form['type_name'], request.form['desc'])
        if result['success']:
            return redirect(url_for('employees.employee_type.get_types'))
        
        return result


@employee_type.route('/get_type/<int:type_id>')
def get_type(type_id):
        type_info=EmployeeTypeC.get(type_id)
        if type_info['data'] == []:
            return redirect(
                url_for('employees.employee_type.get_types')
            )

        return render_template(
            utls.url_join(['employees','get_type.html']),
            type_info=type_info
        )


@employee_type.route('/get_types')
def get_types():
    return render_template(
        utls.url_join(['employees','get_types.html']), 
        types=EmployeeTypeC.get_all()
    )


@employee_type.route('/update_type/<int:type_id>', methods=['GET', 'POST'])
def update_type(type_id):
    if request.method == 'GET':
        type_info = EmployeeTypeC.get(type_id)
        if len(type_info['data']) > 0:
            return render_template(
                utls.url_join(['employees','update_type.html']),
                type_info=type_info['data']
            )
        
        return redirect(url_for('employees.employee_type.get_types'))

    if request.method == 'POST':
        result = EmployeeTypeC.update({
				    'description' : request.form['desc'],
				    'emp_type_id' : type_id
				     })
        if result['success']:
            return redirect(url_for('employees.employee_type.get_types'))
        
        return result


@employee_type.route('/delete_type/<int:type_id>', methods=['DELETE'])
def delete_type(type_id):
    if request.method == 'DELETE':
        return EmployeeTypeC.delete(type_id)


@employee_type.route('/type_exists', methods=['POST'])
def type_exists():
    try:
        return EmployeeTypeC.type_exists(
            request.form['type_name']
        )
    except:
        return {
            'error' : 'Invalid input'
        }
