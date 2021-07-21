from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import SupplierC
from .. import view_utils as utls


supplier = Blueprint('supplier', __name__, url_prefix='/supplier')


@supplier.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['supplier', 'add.html'])
        )

    if request.method == 'POST':
        params = request.form
        result = SupplierC.add({
            'name' : params['name'],
            'address_1' : params['address_1'],
            'address_2' : params['address_2'],
            'city' : params['city'],
            'country' : params['country'],
            'zipcode' : params['zipcode'],
            'phone' : params['phone'],
            'email' : params['email'],
            'website' : params['website'],
            'geo_location' : params['geo_location'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('supplier.all'))

        return result


@supplier.route('/get/<int:supplier_id>')
def get(supplier_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    supplier_info = SupplierC.get(supplier_id)

    if supplier_info['data'] != []:

        return render_template(
            utls.url_join(['supplier', 'get.html']),
            supplier_info = supplier_info
        )

    return redirect(url_for('supplier.all'))


@supplier.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    suppliers = SupplierC.get_all()

    if suppliers['success']:

        return render_template(
            utls.url_join(['supplier', 'all.html']),
            suppliers = suppliers
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@supplier.route('/update/<int:supplier_id>', methods=['GET', 'POST'])
def update(supplier_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        supplier_info = SupplierC.get(supplier_id)

        if len(supplier_info['data']) > 0:

            return render_template(
                utls.url_join(['supplier', 'update.html']),  
                supplier_info = supplier_info
            )

        return redirect(url_for('supplier.all'))

    if request.method == 'POST':
        params = request.form
        result = SupplierC.update({
            'address_1' : params['address_1'],
            'address_2' : params['address_2'],
            'city' : params['city'],
            'country' : params['country'],
            'zipcode' : params['zipcode'],
            'phone' : params['phone'],
            'email' : params['email'],
            'website' : params['website'],
            'geo_location' : params['geo_location'],
            'modify_emp_id' : session['employee']['id'],
            'supplier_id' : supplier_id
        })

        if result['success']:
            return redirect(url_for('supplier.all'))

        return result


@supplier.route('/delete/<int:supplier_id>', methods=['DELETE'])
def delete(supplier_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return SupplierC.delete(supplier_id)