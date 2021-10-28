from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import (SpLogisticC, CarrierC, CurrencyC,
                                            ShippingTypeC, TrackingStatusC)
from .. import view_utils as utls


sp_logistic = Blueprint('sp_logistic', __name__, url_prefix='/sp_logistic')


@sp_logistic.route('/')
def sp_logistic_page():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return render_template(
        utls.url_join(['sp_logistic', 'sp_logistic.html'])
    )

@sp_logistic.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['sp_logistic', 'add.html']),
            carriers_ids = CarrierC.get_ids_names(),
            currencies_ids = CurrencyC.get_ids_names(),
            shipping_types_ids = ShippingTypeC.get_ids_names(),
            tracking_statuses_ids = TrackingStatusC.get_columns_by_col_names()
        )

    if request.method == 'POST':
        params = request.form
        result = SpLogisticC.add({
            'carrier_id' : params['carrier_id'],
            'total_cost' : params['total_cost'],
            'curr_id' : params['curr_id'],
            'shipping_type_id' : params['shipping_type_id'],
            'tr_number' : params['tr_number'],
            'tr_status_id' : params['tr_status_id'],
            'shipped_date' : params['shipped_date'],
            'delivered_date' : params['delivered_date'],
            'comment' : params['comment'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('sp_logistic.all'))

        return result


@sp_logistic.route('/get/<int:shipment_id>')
def get(shipment_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_logistic_info = SpLogisticC.get(shipment_id)

    if len(sp_logistic_info['data']) > 0:

        return render_template(
            utls.url_join(['sp_logistic', 'get.html']),
            sp_logistic_info = sp_logistic_info,
            carrier_name = CarrierC.get(sp_logistic_info['data']['carrier_id']),
            currency_name = CurrencyC.get(sp_logistic_info['data']['curr_id']),
            shipping_type_name = ShippingTypeC.get(sp_logistic_info['data']['shipping_type_id']),
            tracking_status_name = TrackingStatusC.get(sp_logistic_info['data']['tr_status_id'])
        )

    return redirect(url_for('sp_logistic.all'))


@sp_logistic.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_logistics = SpLogisticC.get_all()

    if sp_logistics['success']:
        if len(sp_logistics['data']) > 0:
            return render_template(
                utls.url_join(['sp_logistic', 'all.html']),
                sp_logistics = sp_logistics,
                carriers_ids = CarrierC.get_names_by_ids(sp_logistics['data']['carrier_id']),
                currencies_ids = CurrencyC.get_names_by_ids(sp_logistics['data']['curr_id']),
                shipping_types_ids = ShippingTypeC.get_names_by_ids(sp_logistics['data']['shipping_type_id']),
                tracking_statuses_ids = TrackingStatusC.get_names_by_ids(sp_logistics['data']['tr_status_id'])
            )

        return render_template(utls.url_join(['sp_logistic', 'all.html']),
            sp_logistics = sp_logistics
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@sp_logistic.route('/update/<int:shipment_id>', methods=['GET', 'POST'])
def update(shipment_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        sp_logistic_info = SpLogisticC.get(shipment_id)

        if len(sp_logistic_info['data']) > 0:

            return render_template(
                utls.url_join(['sp_logistic', 'update.html']),  
                sp_logistic_info = sp_logistic_info,
                carrier_name = CarrierC.get(sp_logistic_info['data']['carrier_id']),
                currency_name = CurrencyC.get(sp_logistic_info['data']['curr_id']),
                shipping_type_name = ShippingTypeC.get(sp_logistic_info['data']['shipping_type_id']),
                tracking_statuses_ids = TrackingStatusC.get_columns_by_col_names()
            )

        return redirect(url_for('sp_logistic.all'))

    if request.method == 'POST':
        params = request.form
        result = SpLogisticC.update({
            'tr_status_id' : params['tr_status_id'],
            'delivered_date' : params['delivered_date'],
            'comment' : params['comment'],
            'modify_emp_id' : session['employee']['id'],
            'shipment_id' : shipment_id
        })

        if result['success']:
            return redirect(url_for('sp_logistic.all'))

        return result


@sp_logistic.route('/delete/<int:shipment_id>', methods=['DELETE'])
def delete(shipment_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return SpLogisticC.delete(shipment_id)