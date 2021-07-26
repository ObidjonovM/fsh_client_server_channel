from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import SpStatusC
from .. import view_utils as utls


sp_status = Blueprint('sp_status', __name__, url_prefix='/sp_status')


@sp_status.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['sp_status', 'add.html'])
        )

    if request.method == 'POST':
        params = request.form
        result = SpStatusC.add({
            'status' : params['status'],
            'description' : params['desc'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('sp_status.all'))

        return result


@sp_status.route('/get/<int:status_id>')
def get(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_status_info = SpStatusC.get(status_id)

    if len(sp_status_info['data']) > 0:

        return render_template(
            utls.url_join(['sp_status', 'get.html']),
            sp_status_info = sp_status_info
        )

    return redirect(url_for('sp_status.all'))


@sp_status.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_statuses = SpStatusC.get_all()

    if sp_statuses['success']:
        if len(sp_statuses['data']) > 0:
            return render_template(
                utls.url_join(['sp_status', 'all.html']),
                sp_statuses = sp_statuses
            )

        return render_template(
            utls.url_join(['sp_status', 'all.html'])
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@sp_status.route('/update/<int:status_id>', methods=['GET', 'POST'])
def update(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        sp_status_info = SpStatusC.get(status_id)

        if len(sp_status_info['data']) > 0:

            return render_template(
                utls.url_join(['sp_status', 'update.html']),  
                sp_status_info = sp_status_info,
            )

        return redirect(url_for('sp_status.all'))

    if request.method == 'POST':
        params = request.form
        result = SpStatusC.update({
            'description' : params['desc'],
            'modify_emp_id' : session['employee']['id'],
            'status_id' : status_id
        })

        if result['success']:
            return redirect(url_for('sp_status.all'))

        return result


@sp_status.route('/delete/<int:status_id>', methods=['DELETE'])
def delete(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return SpStatusC.delete(status_id)