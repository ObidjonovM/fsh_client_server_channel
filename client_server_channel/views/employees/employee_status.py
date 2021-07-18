from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import EmployeeStatusC
from .. import view_utils as utls


employee_status = Blueprint('employee_status', __name__, url_prefix='/status')


@employee_status.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(utls.url_join(['employees','employee_status','add.html']))

    if request.method == 'POST':
        result = EmployeeStatusC.add({
            'status' : request.form['status'],
            'description' : request.form['desc'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
            })
        if result['success']:
            return redirect(url_for('employees.employee_status.all'))

        return result


@employee_status.route('get/<int:status_id>')
def get(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    status_info=EmployeeStatusC.get(status_id)
    if status_info['data'] == []:
        return redirect(
            url_for('employees.employee_status.all')
        )

    return render_template(
        utls.url_join(['employees', 'employee_status', 'get.html']),
        status_info = status_info
    )


@employee_status.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))
    
    return render_template(
        utls.url_join(['employees', 'employee_status', 'all.html']),
        status_all = EmployeeStatusC.get_all()
    )


@employee_status.route('/update/<int:status_id>', methods=['GET', 'POST'])
def update(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        status_info = EmployeeStatusC.get(status_id)
        if len(status_info['data']) > 0:
            return render_template(
                utls.url_join(['employees', 'employee_status', 'update.html']),
                status_info = status_info['data']
            )

        return redirect(url_for('employees.employee_status.all'))

    if request.method == 'POST':
        result = EmployeeStatusC.update({
            'description' : request.form['desc'],
            'modify_emp_id' : session['employee']['id'],
            'status_id' : status_id
        })
        if result['success']:
            return redirect(url_for('employees.employee_status.all'))

        return result


@employee_status.route('/delete/<int:status_id>', methods=['DELETE'])
def delete(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))
    
    if request.method == 'DELETE':
        return EmployeeStatusC.delete(status_id)  
