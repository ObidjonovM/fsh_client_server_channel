from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import (SpOrderDetailC, CurrencyC, SpOrderC, 
                                            UnitC, SpTypeC)
from .. import view_utils as utls


sp_order_detail = Blueprint('sp_order_detail', __name__, url_prefix='/sp_order_detail')


@sp_order_detail.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['sp_order_detail', 'add.html']),
            types_ids = SpTypeC.get_ids_names(),
            currencies_ids = CurrencyC.get_ids_names(),
            units_ids = UnitC.get_ids_names(),
            orders_ids = SpOrderC.get_ids_names()
        )

    if request.method == 'POST':
        params = request.form
        result = SpOrderDetailC.add({
            'type_id' : params['type_id'],
            'price_per_unit' : params['price_per_unit'],
            'curr_id' : params['curr_id'],
            'amount' : params['amount'],
            'unit_id' : params['unit_id'],
            'order_id' : params['order_id'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('sp_order_detail.all'))

        return result


@sp_order_detail.route('/get/<int:detail_id>')
def get(detail_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    detail_info = SpOrderDetailC.get(detail_id)

    if len(detail_info['data']) > 0:

        return render_template(
            utls.url_join(['sp_order_detail', 'get.html']),
            detail_info = detail_info,
            type_name = SpTypeC.get(detail_info['data']['type_id']),
            currency_name = CurrencyC.get(detail_info['data']['curr_id']),
            unit_name = UnitC.get(detail_info['data']['unit_id']),
            order_name = SpOrderC.get(detail_info['data']['order_id'])
        )

    return redirect(url_for('sp_order_detail.all'))


@sp_order_detail.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_order_details = SpOrderDetailC.get_all()

    if sp_order_details['success']:
        if len(sp_order_details['data']) > 0:
            return render_template(
                utls.url_join(['sp_order_detail', 'all.html']),
                sp_order_details = sp_order_details,
                types_ids = SpTypeC.get_names_by_ids(sp_order_details['data']['type_id']),
                currencies_ids = CurrencyC.get_names_by_ids(sp_order_details['data']['curr_id']),
                units_ids = UnitC.get_names_by_ids(sp_order_details['data']['unit_id']),
                orders_ids = SpOrderC.get_names_by_ids(sp_order_details['data']['order_id']),
            )

        return render_template(utls.url_join(['sp_order_detail', 'all.html']))

    return redirect(url_for('core.index'))            # TODO later!!!!


@sp_order_detail.route('/delete/<int:detail_id>', methods=['DELETE'])
def delete(detail_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return SpOrderDetailC.delete(detail_id)