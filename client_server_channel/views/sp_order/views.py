from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import (SpOrderC, CurrencyC, SupplierC, 
                                            SpOrderStatusC, SpLogisticC, EmployeeC)
from .. import view_utils as utls


sp_order = Blueprint('sp_order', __name__, url_prefix='/sp_order')

@sp_order.route('/')
def sp_order_page():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return render_template(
        utls.url_join(['sp_order', 'sp_order.html'])
    )

@sp_order.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['sp_order', 'add.html']),
            currencies_ids = CurrencyC.get_ids_names(),
            suppliers_ids = SupplierC.get_ids_names(),
            order_statuses_ids = SpOrderStatusC.get_ids_names(),
            ord_emp_id = EmployeeC.get_ids_names()
        )

    if request.method == 'POST':
        params = request.form
        result = SpOrderC.add({
            'issued_order_id' : params['issued_order_id'],
            'total_cost' : params['total_cost'],
            'curr_id' : params['curr_id'],
            'supplier_id' : params['supplier_id'],
            'exp_dispatch_date' : params['exp_dispatch_date'],
            'order_status_id' : params['order_status_id'],
            'shipment_id' : params['shipment_id'],
            'order_date' : params['order_date'],
            'ord_emp_id' : params['ord_emp_id'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('sp_order.all'))

        return result


@sp_order.route('/get/<int:sp_order_id>')
def get(sp_order_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_order_info = SpOrderC.get(sp_order_id)

    if len(sp_order_info['data']) > 0:

        return render_template(
            utls.url_join(['sp_order', 'get.html']),
            sp_order_info = sp_order_info,
            currency_name = CurrencyC.get(sp_order_info['data']['curr_id']),
            supplier_name = SupplierC.get(sp_order_info['data']['supplier_id']),
            order_status = SpOrderStatusC.get(sp_order_info['data']['order_status_id']),
            employee_name = EmployeeC.get(sp_order_info['data']['ord_emp_id'])
        )

    return redirect(url_for('sp_order.all'))


@sp_order.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_orders = SpOrderC.get_all()

    if sp_orders['success']:
        if len(sp_orders['data']) > 0:
            return render_template(
                utls.url_join(['sp_order', 'all.html']),
                sp_orders = sp_orders,
                currencies_ids = CurrencyC.get_names_by_ids(sp_orders['data']['curr_id']),
                suppliers_ids = SupplierC.get_names_by_ids(sp_orders['data']['supplier_id']),
                order_statuses_ids = SpOrderStatusC.get_names_by_ids(sp_orders['data']['order_status_id']),
                employees_ids = EmployeeC.get_names_by_ids(sp_orders['data']['ord_emp_id'])
            )

        return render_template(utls.url_join(['sp_order', 'all.html']),
            sp_orders = sp_orders
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@sp_order.route('/update/<int:sp_order_id>', methods=['GET', 'POST'])
def update(sp_order_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        sp_order_info = SpOrderC.get(sp_order_id)

        if len(sp_order_info['data']) > 0:

            return render_template(
                utls.url_join(['sp_order', 'update.html']),  
                sp_order_info = sp_order_info,
                order_statuses_ids = SpOrderStatusC.get_ids_names(),
                currency_name = CurrencyC.get(sp_order_info['data']['curr_id']),
                supplier_name = SupplierC.get(sp_order_info['data']['supplier_id']),
                employee_name = EmployeeC.get(sp_order_info['data']['ord_emp_id'])
            )

        return redirect(url_for('sp_order.all'))

    if request.method == 'POST':
        params = request.form
        result = SpOrderC.update({
            'order_status_id' : params['order_status_id'],
            'modify_emp_id' : session['employee']['id'],
            'sp_order_id' : sp_order_id
        })

        if result['success']:
            return redirect(url_for('sp_order.all'))

        return result


@sp_order.route('/delete/<int:sp_order_id>', methods=['DELETE'])
def delete(sp_order_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return SpOrderC.delete(sp_order_id)