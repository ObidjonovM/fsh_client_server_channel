from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import EmployeeStatusC
from .. import view_utils as utls


employee_status = Blueprint('employee_status', __name__)


@employee_status.route('/add_status', methods=['GET', 'POST'])
def add_status():
    if request.method == 'GET':
        return render_template(utls.url_join(['employees','employee_status','add_status.html']))

    if request.method == 'POST':
        result = EmployeeStatusC.add(request.form['status'], request.form['desc'])
        if result['success']:
            return redirect(url_for('employees.employee_status.get_status_all'))

        return result


@employee_status.route('get_status/<int:status_id>')
def get_status(status_id):
    status_info=EmployeeStatusC.get(status_id)
    if status_info['data'] == []:
        return redirect(
            url_for('employees.employee_status.get_status_all')
        )

    return render_template(
        utls.url_join(['employees', 'employee_status', 'get_status.html']),
        status_info = status_info
    )


@employee_status.route('/get_status_all')
def get_status_all():
    return render_template(
        utls.url_join(['employees', 'employee_status', 'get_status_all.html']),
        status_all = EmployeeStatusC.get_all()
    )


@employee_status.route('/update_status/<int:status_id>', methods=['GET', 'POST'])
def update_status(status_id):
    if request.method == 'GET':
        status_info = EmployeeStatusC.get(status_id)
        if len(status_info['data']) > 0:
            return render_template(
                utls.url_join(['employees', 'employee_status', 'update_status.html']),
                status_info = status_info['data']
            )

        return redirect(url_for('employees.employee_status.get_status_all'))

    if request.method == 'POST':
        result = EmployeeStatusC.update({
            'description' : request.form['desc'],
            'status_id' : status_id
        })
        if result['success']:
            return redirect(url_for('employees.employee_status.get_status_all'))

        return result


@employee_status.route('/delete_status/<int:status_id>', methods=['DELETE'])
def delete_status(status_id):
    if request.method == 'DELETE':
        return EmployeeStatusC.delete(status_id)  
