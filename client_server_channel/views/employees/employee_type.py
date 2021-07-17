from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import EmployeeTypeC
from .. import view_utils as utls

employee_type = Blueprint('employee_type', __name__, url_prefix = '/type')


@employee_type.route('/add', methods=['GET','POST'])
def add():
    if not 'username' in session:
         return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(utls.url_join(['employees','employee_type','add.html']))

    if request.method == 'POST':
        result = EmployeeTypeC.add(request.form['type_name'], request.form['desc'])
        if result['success']:
            return redirect(url_for('employees.employee_type.all'))
        
        return result


@employee_type.route('/get/<int:type_id>')
def get(type_id):
    if not 'username' in session:
         return redirect(url_for('employees.login'))

    type_info=EmployeeTypeC.get(type_id)
    if type_info['data'] == []:
        return redirect(
            url_for('employees.employee_type.all')
        )

    return render_template(
        utls.url_join(['employees','employee_type','get.html']),
        type_info=type_info
    )


@employee_type.route('/all')
def all():
    if not 'username' in session:
         return redirect(url_for('employees.login'))
    
    return render_template(
        utls.url_join(['employees','employee_type','all.html']), 
        types=EmployeeTypeC.get_all()
    )


@employee_type.route('/update/<int:type_id>', methods=['GET', 'POST'])
def update(type_id):
    if not 'username' in session:
         return redirect(url_for('employees.login'))

    if request.method == 'GET':
        type_info = EmployeeTypeC.get(type_id)
        if len(type_info['data']) > 0:
            return render_template(
                utls.url_join(['employees','employee_type','update.html']),
                type_info=type_info['data']
            )
        
        return redirect(url_for('employees.employee_type.get'))

    if request.method == 'POST':
        result = EmployeeTypeC.update({
				    'description' : request.form['desc'],
				    'emp_type_id' : type_id
				     })
        if result['success']:
            return redirect(url_for('employees.employee_type.all'))
        
        return result


@employee_type.route('/delete/<int:type_id>', methods=['DELETE'])
def delete(type_id):
    if not 'username' in session:
         return redirect(url_for('employees.login'))
    
    if request.method == 'DELETE':
        return EmployeeTypeC.delete(type_id)


@employee_type.route('/type_exists', methods=['POST'])
def type_exists():
    if not 'username' in session:
         return redirect(url_for('employees.login'))
    
    try:
        return EmployeeTypeC.type_exists(
            request.form['type_name']
        )
    except:
        return {
            'error' : 'Invalid input'
        }
