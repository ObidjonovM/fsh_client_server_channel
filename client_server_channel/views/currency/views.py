from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import CurrencyC
from .. import view_utils as utls


currency = Blueprint('currency', __name__, url_prefix='/currency')


@currency.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['currency', 'add.html'])
        )

    if request.method == 'POST':
        result = CurrencyC.add({
            'currency' : request.form['currency'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('currency.all'))

        return result


@currency.route('/get/<int:curr_id>')
def get(curr_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    curr_info = CurrencyC.get(curr_id)

    if len(curr_info['data']) > 0:

        return render_template(
            utls.url_join(['currency', 'get.html']),
            curr_info = curr_info
        )

    return redirect(url_for('currency.all'))


@currency.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    currencies = CurrencyC.get_all()

    if currencies['success']:

        return render_template(
            utls.url_join(['currency', 'all.html']),
            currencies = currencies
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@currency.route('/delete/<int:curr_id>', methods=['DELETE'])
def delete(curr_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return CurrencyC.delete(curr_id)