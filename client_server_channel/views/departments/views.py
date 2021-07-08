from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import DepartmentsC, EmployeeC
from .. import view_utils as utls


departments = Blueprint('departments', __name__, url_prefix='/departments')


@departments.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template(
            utls.url_join(['departments', 'add.html'])
        )

    if request.method == 'POST':
        result = DepartmentsC.add(
            request.form['name'],
            request.form['desc']
        )

        if result['success']:
            return redirect(url_for('departments.get_all'))

        return result


@departments.route('/get/<int:dept_id>')
def get(dept_id):
    dept_info = DepartmentsC.get(dept_id)

    if dept_info['data'] != []:

        return render_template(
            utls.url_join(['departments', 'get.html']),
            dept_info = dept_info
        )

    return redirect(url_for('departments.get_all'))


@departments.route('/get_all')
def get_all():
    departments = DepartmentsC.get_all()

    if departments['success']:

        return render_template(
            utls.url_join(['departments', 'get_all.html']),
            departments = departments
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@departments.route('/update/<int:dept_id>', methods=['GET', 'POST'])
def update(dept_id):
    if request.method == 'GET':
        dept_info = DepartmentsC.get(dept_id)

        if len(dept_info['data']) > 0:

            return render_template(
                utls.url_join(['departments', 'update.html']),  
                dept_info = dept_info
            )

        return redirect(url_for('departments.get_all'))

    if request.method == 'POST':
        result = DepartmentsC.update({
            'description' : request.form['desc'],
            'dept_id' : dept_id
        })

        if result['success']:
            return redirect(url_for('departments.get_all'))

        return result


@departments.route('/delete/<int:dept_id>', methods=['DELETE'])
def delete(dept_id):
    return DepartmentsC.delete(dept_id)