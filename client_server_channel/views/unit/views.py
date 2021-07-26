from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import UnitC
from .. import view_utils as utls


unit = Blueprint('unit', __name__, url_prefix='/unit')


@unit.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['unit', 'add.html'])
        )

    if request.method == 'POST':
        result = UnitC.add({
            'unit' : request.form['unit'],
            'description' : request.form['desc'],
            'add_emp_id' : session['employee']['id'],
            'modify_emp_id' : session['employee']['id']
        })

        if result['success']:
            return redirect(url_for('unit.all'))

        return result


@unit.route('/get/<int:unit_id>')
def get(unit_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    unit_info = UnitC.get(unit_id)

    if len(unit_info['data']) > 0:

        return render_template(
            utls.url_join(['unit', 'get.html']),
            unit_info = unit_info
        )

    return redirect(url_for('unit.all'))


@unit.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    units = UnitC.get_all()

    if units['success']:
        if len(units['data']) > 0:
            return render_template(
                utls.url_join(['unit', 'all.html']),
                units = units
            )

        return render_template(
            utls.url_join(['unit', 'all.html'])
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@unit.route('/update/<int:unit_id>', methods=['GET', 'POST'])
def update(unit_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        unit_info = UnitC.get(unit_id)

        if len(unit_info['data']) > 0:

            return render_template(
                utls.url_join(['unit', 'update.html']),  
                unit_info = unit_info
            )

        return redirect(url_for('unit.all'))

    if request.method == 'POST':
        result = UnitC.update({
            'description' : request.form['desc'],
            'modify_emp_id' : session['employee']['id'],
            'unit_id' : unit_id
        })

        if result['success']:
            return redirect(url_for('unit.all'))

        return result


@unit.route('/delete/<int:unit_id>', methods=['DELETE'])
def delete(unit_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return UnitC.delete(unit_id)