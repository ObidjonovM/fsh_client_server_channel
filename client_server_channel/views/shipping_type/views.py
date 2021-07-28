from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import ShippingTypeC, CurrencyC, UnitC, CarrierC
from .. import view_utils as utls


shipping_type = Blueprint('shipping_type', __name__, url_prefix='/shipping_type')


@shipping_type.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['shipping_type', 'add.html']),
            currencies_ids = CurrencyC.get_ids_names(),
            units_ids = UnitC.get_ids_names(),
            carriers_ids = CarrierC.get_ids_names()
        )

    if request.method == 'POST':
        params = request.form
        result = ShippingTypeC.add({
            'name' : params['name'],
            'price' : params['price'],
            'curr_id' : params['curr_id'],
            'unit_id' : params['unit_id'],
            'min_delivery_days' : params['min_delivery_days'],
            'max_delivery_days' : params['max_delivery_days'],
            'carrier_id' : params['carrier_id'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('shipping_type.all'))

        return result


@shipping_type.route('/get/<int:shipping_type_id>')
def get(shipping_type_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    shipping_type_info = ShippingTypeC.get(shipping_type_id)

    if len(shipping_type_info['data']) > 0:

        return render_template(
            utls.url_join(['shipping_type', 'get.html']),
            shipping_type_info = shipping_type_info,
            currency_name = CurrencyC.get(shipping_type_info['data']['curr_id']),
            unit_name = UnitC.get(shipping_type_info['data']['unit_id']),
            carrier_name = CarrierC.get(shipping_type_info['data']['carrier_id'])
        )

    return redirect(url_for('shipping_type.all'))


@shipping_type.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    shipping_types = ShippingTypeC.get_all()

    if shipping_types['success']:
        if len(shipping_types['data']) > 0:
            return render_template(
                utls.url_join(['shipping_type', 'all.html']),
                shipping_types = shipping_types,
                currencies_ids = CurrencyC.get_names_by_ids(shipping_types['data']['curr_id']),
                units_ids = UnitC.get_names_by_ids(shipping_types['data']['unit_id']),
                carriers_ids = CarrierC.get_names_by_ids(shipping_types['data']['carrier_id'])
            )

        return render_template(
            utls.url_join(['shipping_type', 'all.html']),
            shipping_types = shipping_types
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@shipping_type.route('/update/<int:shipping_type_id>', methods=['GET', 'POST'])
def update(shipping_type_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        shipping_type_info = ShippingTypeC.get(shipping_type_id)

        if len(shipping_type_info['data']) > 0:

            return render_template(
                utls.url_join(['shipping_type', 'update.html']),  
                shipping_type_info = shipping_type_info,
                currencies_ids = CurrencyC.get_ids_names(),
                units_ids = UnitC.get_ids_names(),
                carriers_ids = CarrierC.get_ids_names()
            )

        return redirect(url_for('shipping_type.all'))

    if request.method == 'POST':
        params = request.form
        result = ShippingTypeC.update({
            'price' : params['price'],
            'curr_id' : params['curr_id'],
            'unit_id' : params['unit_id'],
            'min_delivery_days' : params['min_delivery_days'],
            'max_delivery_days' : params['max_delivery_days'],
            'carrier_id' : params['carrier_id'],
            'modify_emp_id' : session['employee']['id'],
            'shipping_type_id' : shipping_type_id
        })

        if result['success']:
            return redirect(url_for('shipping_type.all'))

        return result


@shipping_type.route('/delete/<int:shipping_type_id>', methods=['DELETE'])
def delete(shipping_type_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return ShippingTypeC.delete(shipping_type_id)