from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import TrackingStatusC, CarrierC
from .. import view_utils as utls


tracking_status = Blueprint('tracking_status', __name__, url_prefix='/tracking_status')


@tracking_status.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['tracking_status', 'add.html']),
            carriers_ids = CarrierC.get_ids_names()
        )

    if request.method == 'POST':
        params = request.form
        result = TrackingStatusC.add({
            'status' : params['status'],
            'carrier_id' : params['carrier_id'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('tracking_status.all'))

        return result


@tracking_status.route('/get/<int:status_id>')
def get(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    tracking_status_info = TrackingStatusC.get(status_id)

    if len(tracking_status_info['data']) > 0:

        return render_template(
            utls.url_join(['tracking_status', 'get.html']),
            tracking_status_info = tracking_status_info,
            carrier_name = CarrierC.get(tracking_status_info['data']['carrier_id'])
        )

    return redirect(url_for('tracking_status.all'))


@tracking_status.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    tracking_statuses = TrackingStatusC.get_all()

    if tracking_statuses['success']:
        if len(tracking_statuses['data']) > 0:
            return render_template(
                utls.url_join(['tracking_status', 'all.html']),
                tracking_statuses = tracking_statuses,
                carriers_ids = CarrierC.get_names_by_ids(tracking_statuses['data']['carrier_id'])
            )

    return redirect(url_for('core.index'))            # TODO later!!!!


@tracking_status.route('/update/<int:status_id>', methods=['GET', 'POST'])
def update(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        tracking_status_info = TrackingStatusC.get(status_id)

        if len(tracking_status_info['data']) > 0:

            return render_template(
                utls.url_join(['tracking_status', 'update.html']),  
                tracking_status_info = tracking_status_info,
                carriers_ids = CarrierC.get_ids_names()
            )

        return redirect(url_for('tracking_status.all'))

    if request.method == 'POST':
        params = request.form
        result = TrackingStatusC.update({
            'carrier_id' : params['carrier_id'],
            'modify_emp_id' : session['employee']['id'],
            'status_id' : status_id
        })

        if result['success']:
            return redirect(url_for('tracking_status.all'))

        return result


@tracking_status.route('/delete/<int:status_id>', methods=['DELETE'])
def delete(status_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return TrackingStatusC.delete(status_id)