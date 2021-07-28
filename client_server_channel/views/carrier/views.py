from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import CarrierC
from .. import view_utils as utls


carrier = Blueprint('carrier', __name__, url_prefix='/carrier')


@carrier.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['carrier', 'add.html'])
        )

    if request.method == 'POST':
        params = request.form
        result = CarrierC.add({
            'name' : params['name'],
            'address_1' : params['address_1'],
            'address_2' : params['address_2'],
            'city' : params['city'],
            'country' : params['country'],
            'zipcode' : params['zipcode'],
            'phone' : params['phone'],
            'email' : params['email'],
            'website' : params['website'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('carrier.all'))

        return result


@carrier.route('/get/<int:carrier_id>')
def get(carrier_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    carrier_info = CarrierC.get(carrier_id)

    if len(carrier_info['data']) > 0:

        return render_template(
            utls.url_join(['carrier', 'get.html']),
            carrier_info = carrier_info
        )

    return redirect(url_for('carrier.all'))


@carrier.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    carriers = CarrierC.get_all()

    if carriers['success']:

        return render_template(
            utls.url_join(['carrier', 'all.html']),
            carriers = carriers
        )
        
        
    return redirect(url_for('core.index'))            # TODO later!!!!


@carrier.route('/update/<int:carrier_id>', methods=['GET', 'POST'])
def update(carrier_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        carrier_info = CarrierC.get(carrier_id)

        if len(carrier_info['data']) > 0:

            return render_template(
                utls.url_join(['carrier', 'update.html']),  
                carrier_info = carrier_info
            )

        return redirect(url_for('carrier.all'))

    if request.method == 'POST':
        params = request.form
        result = CarrierC.update({
            'address_1' : params['address_1'],
            'address_2' : params['address_2'],
            'city' : params['city'],
            'country' : params['country'],
            'zipcode' : params['zipcode'],
            'phone' : params['phone'],
            'email' : params['email'],
            'website' : params['website'],
            'modify_emp_id' : session['employee']['id'],
            'carrier_id' : carrier_id
        })

        if result['success']:
            return redirect(url_for('carrier.all'))

        return result


@carrier.route('/delete/<int:carrier_id>', methods=['DELETE'])
def delete(carrier_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return CarrierC.delete(carrier_id)