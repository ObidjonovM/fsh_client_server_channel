from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import SpOrderStatusC
from .. import view_utils as utls


sp_order_status = Blueprint('sp_order_status', __name__, url_prefix='/sp_order_status')


@sp_order_status.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['sp_order_status', 'add.html'])
        )

    if request.method == 'POST':
        params = request.form
        result = SpOrderStatusC.add({
            'name' : params['name'],
            'description' : params['desc'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('sp_order_status.all'))

        return result


@sp_order_status.route('/get/<int:status_id>')
def get(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_order_status_info = SpOrderStatusC.get(status_id)

    if len(sp_order_status_info['data']) > 0:

        return render_template(
            utls.url_join(['sp_order_status', 'get.html']),
            sp_order_status_info = sp_order_status_info
        )

    return redirect(url_for('sp_order_status.all'))


@sp_order_status.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_order_statuses = SpOrderStatusC.get_all()

    if sp_order_statuses['success']:
        if len(sp_order_statuses['data']) > 0:
            return render_template(
                utls.url_join(['sp_order_status', 'all.html']),
                sp_order_statuses = sp_order_statuses
            )

    return redirect(url_for('core.index'))            # TODO later!!!!


@sp_order_status.route('/update/<int:status_id>', methods=['GET', 'POST'])
def update(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        sp_order_status_info = SpOrderStatusC.get(status_id)

        if len(sp_order_status_info['data']) > 0:

            return render_template(
                utls.url_join(['sp_order_status', 'update.html']),  
                sp_order_status_info = sp_order_status_info,
            )

        return redirect(url_for('sp_order_status.all'))

    if request.method == 'POST':
        params = request.form
        result = SpOrderStatusC.update({
            'description' : params['desc'],
            'modify_emp_id' : session['employee']['id'],
            'status_id' : status_id
        })

        if result['success']:
            return redirect(url_for('sp_order_status.all'))

        return result


@sp_order_status.route('/delete/<int:status_id>', methods=['DELETE'])
def delete(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return SpOrderStatusC.delete(status_id)