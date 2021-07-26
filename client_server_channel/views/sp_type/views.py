from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import SpTypeC
from .. import view_utils as utls


sp_type = Blueprint('sp_type', __name__, url_prefix='/sp_type')


@sp_type.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['sp_type', 'add.html'])
        )

    if request.method == 'POST':
        params = request.form
        result = SpTypeC.add({
            'name' : params['name'],
            'brand' : params['brand'],
            'model' : params['model'],
            'version' : params['version'],
            'description' : params['desc'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('sp_type.all'))

        return result


@sp_type.route('/get/<int:sp_type_id>')
def get(sp_type_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_type_info = SpTypeC.get(sp_type_id)

    if len(sp_type_info['data']) > 0:

        return render_template(
            utls.url_join(['sp_type', 'get.html']),
            sp_type_info = sp_type_info
        )

    return redirect(url_for('sp_type.all'))


@sp_type.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_types = SpTypeC.get_all()

    if sp_types['success']:
        if len(sp_types['data']) > 0:
            return render_template(
                utls.url_join(['sp_type', 'all.html']),
                sp_types = sp_types
            )

    return redirect(url_for('core.index'))            # TODO later!!!!


@sp_type.route('/update/<int:sp_type_id>', methods=['GET', 'POST'])
def update(sp_type_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        sp_type_info = SpTypeC.get(sp_type_id)

        if len(sp_type_info['data']) > 0:

            return render_template(
                utls.url_join(['sp_type', 'update.html']),  
                sp_type_info = sp_type_info,
            )

        return redirect(url_for('sp_type.all'))

    if request.method == 'POST':
        params = request.form
        result = SpTypeC.update({
            'description' : params['desc'],
            'modify_emp_id' : session['employee']['id'],
            'sp_type_id' : sp_type_id
        })

        if result['success']:
            return redirect(url_for('sp_type.all'))

        return result


@sp_type.route('/delete/<int:sp_type_id>', methods=['DELETE'])
def delete(sp_type_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return SpTypeC.delete(sp_type_id)