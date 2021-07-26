from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import (SpWarehouseC, SpTypeC, SpOrderC,
                                            SpStatusC, EmployeeC, ProductC)
from .. import view_utils as utls


sp_warehouse = Blueprint('sp_warehouse', __name__, url_prefix='/sp_warehouse')


@sp_warehouse.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['sp_warehouse', 'add.html']),
            types_ids = SpTypeC.get_ids_names(),
            orders_ids = SpOrderC.get_ids_names(),
            statuses_ids = SpStatusC.get_ids_names(),
            employees_ids = EmployeeC.get_ids_names(),
            products_ids = ProductC.get_ids_names()
        )

    if request.method == 'POST':
        params = request.form
        result = SpWarehouseC.add({
            'type_id' : params['type_id'],
            'order_id' : params['order_id'],
            'status_id' : params['status_id'],
            'acc_emp_id' : params['acc_emp_id'],
            'used_emp_id' : params['used_emp_id'],
            'pr_serial_num' : params['pr_serial_num']
        })

        if result['success']:
            return redirect(url_for('sp_warehouse.all'))

        return result


@sp_warehouse.route('/get/<int:sp_id>')
def get(sp_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_warehouse_info = SpWarehouseC.get(sp_id)

    if sp_warehouse_info['data'] != []:

        return render_template(
            utls.url_join(['sp_warehouse', 'get.html']),
            sp_warehouse_info = sp_warehouse_info,
            type_name = SpTypeC.get(sp_warehouse_info['data']['type_id']),
            order_name = SpOrderC.get(sp_warehouse_info['data']['order_id']),
            status_name = SpStatusC.get(sp_warehouse_info['data']['status_id']),
            employee_name = EmployeeC.get(sp_warehouse_info['data']['acc_emp_id']),
            product_name = ProductC.get(sp_warehouse_info['data']['pr_serial_num'])
        )

    return redirect(url_for('sp_warehouse.all'))


@sp_warehouse.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    sp_warehouses = SpWarehouseC.get_all()

    if sp_warehouses['success']:
        if len(sp_warehouses['data']) > 0:
            return render_template(
                utls.url_join(['sp_warehouse', 'all.html']),
                sp_warehouses = sp_warehouses,
                types_ids = SpTypeC.get_names_by_ids(sp_warehouses['data']['type_id']),
                orders_ids = SpOrderC.get_names_by_ids(sp_warehouses['data']['order_id']),
                statuses_ids = SpStatusC.get_names_by_ids(sp_warehouses['data']['status_id']),
                employees_ids = EmployeeC.get_names_by_ids(sp_warehouses['data']['acc_emp_id']),
                products_ids = ProductC.get_names_by_ids(sp_warehouses['data']['pr_serial_num'])
            )

        return render_template(utls.url_join(['sp_warehouse', 'all.html']))

    return redirect(url_for('core.index'))            # TODO later!!!!


@sp_warehouse.route('/update/<int:sp_id>', methods=['GET', 'POST'])
def update(sp_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        sp_warehouse_info = SpWarehouseC.get(sp_id)

        if len(sp_warehouse_info['data']) > 0:

            return render_template(
                utls.url_join(['sp_warehouse', 'update.html']),  
                sp_warehouse_info = sp_warehouse_info,
                type_name = SpTypeC.get(sp_warehouse_info['data']['type_id']),
                order_name = SpOrderC.get(sp_warehouse_info['data']['order_id']),
                statuses_ids = SpStatusC.get_ids_names(),
                employee_name = EmployeeC.get(sp_warehouse_info['data']['acc_emp_id']),
                employees_ids = EmployeeC.get_ids_names(),
                products_ids = ProductC.get_ids_names()
            )

        return redirect(url_for('sp_warehouse.all'))

    if request.method == 'POST':
        params = request.form
        result = SpWarehouseC.update({
            'status_id' : params['status_id'],
            'used_emp_id' : params['used_emp_id'],
            'pr_serial_num' : params['pr_serial_num'],
            'sp_id' : sp_id
        })

        if result['success']:
            return redirect(url_for('sp_warehouse.all'))

        return result


@sp_warehouse.route('/delete/<int:sp_id>', methods=['DELETE'])
def delete(sp_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return SpWarehouseC.delete(sp_id)