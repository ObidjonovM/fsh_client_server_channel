from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import FirmwareC, EmployeeC
from .. import view_utils as utls


firmware = Blueprint('firmware', __name__, url_prefix='/firmware')


@firmware.route('/add', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        return render_template(
            utls.url_join(['products', 'firmware', 'add.html']),
            ids_fullname = EmployeeC.get_all()
        )

    if request.method == 'POST':
        params = request.form
        result = FirmwareC.add({
            'name': params['name'],
            'model': params['model'],
            'version': params['version'],
            'description': params['desc'],
            'author_id': params['emp_id'],
            'add_emp_id' : session['employee']['id'],
			'modify_emp_id' : session['employee']['id']
        })
        
        if result['success']:
            return redirect(url_for('products.firmware.all'))

        return result


@firmware.route('/get/<int:fw_id>')
def get(fw_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    fw_info = FirmwareC.get(fw_id)
    id_name = EmployeeC.get(fw_info['data']['author_id'])['data']
    fullname = f"{id_name['last_name']} {id_name['first_name']} {id_name['middle_name']}"
    
    if len(fw_info['data']) > 0:
        
        return render_template(
            utls.url_join(['products', 'firmware', 'get.html']),
            fw_info=fw_info,
            fullname = fullname
        )

    return redirect(url_for('products.firmware.all'))


@firmware.route('/all')
def all():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    firmwares = FirmwareC.get_all()

    if firmwares['success']:
        if len(firmwares['data']) > 0:
            return render_template(
                utls.url_join(['products', 'firmware', 'all.html']),
                firmwares = firmwares,
                names_by_ids = EmployeeC.get_names_by_ids(firmwares['data']['author_id'])
            )

        return render_template(
            utls.url_join(['products', 'firmware', 'all.html'])
        )
    
    return redirect(url_for('core.index'))            # TODO later!!!!


@firmware.route('/update/<int:fw_id>', methods=['GET', 'POST'])
def update(fw_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'GET':
        fw_info = FirmwareC.get(fw_id)
        id_name = EmployeeC.get(fw_info['data']['author_id'])['data']
        fullname = f"{id_name['last_name']} {id_name['first_name']} {id_name['middle_name']}"
        
        if len(fw_info['data']) > 0:
            
            return render_template(
                utls.url_join(['products', 'firmware', 'update.html']),
                fw_info = fw_info['data'],
                fullname = fullname
            )

        return redirect(url_for('products.firmware.all'))

    if request.method == 'POST':
        result = FirmwareC.update({
            'description' : request.form['desc'],
			'modify_emp_id' : session['employee']['id'],
            'fw_id' : fw_id
        })
        
        if result['success']:
            return redirect(url_for('products.firmware.all'))

        return result


@firmware.route('/delete/<int:fw_id>', methods=['DELETE'])
def delete(fw_id):
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    return FirmwareC.delete(fw_id)