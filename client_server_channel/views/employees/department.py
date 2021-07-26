from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import DepartmentC
from .. import view_utils as utls


department = Blueprint('department', __name__, url_prefix='/department')


@department.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['employees', 'department', 'add.html'])
        )

    if request.method == 'POST':
        result = DepartmentC.add({
            'name' : request.form['name'],
            'description' : request.form['desc'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('employees.department.all'))

        return result


@department.route('/get/<int:dept_id>')
def get(dept_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    dept_info = DepartmentC.get(dept_id)

    if len(dept_info['data']) > 0:

        return render_template(
            utls.url_join(['employees', 'department', 'get.html']),
            dept_info = dept_info
        )

    return redirect(url_for('employees.department.all'))


@department.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    departments = DepartmentC.get_all()

    if departments['success']:

        return render_template(
            utls.url_join(['employees', 'department', 'all.html']),
            departments = departments
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@department.route('/update/<int:dept_id>', methods=['GET', 'POST'])
def update(dept_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        dept_info = DepartmentC.get(dept_id)

        if len(dept_info['data']) > 0:

            return render_template(
                utls.url_join(['employees', 'department', 'update.html']),  
                dept_info = dept_info
            )

        return redirect(url_for('employees.department.all'))

    if request.method == 'POST':
        result = DepartmentC.update({
            'description' : request.form['desc'],
            'modify_emp_id' : session['employee']['id'],
            'dept_id' : dept_id
        })

        if result['success']:
            return redirect(url_for('employees.department.all'))

        return result


@department.route('/delete/<int:dept_id>', methods=['DELETE'])
def delete(dept_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return DepartmentC.delete(dept_id)