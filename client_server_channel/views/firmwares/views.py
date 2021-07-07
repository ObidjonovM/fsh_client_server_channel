from flask import Blueprint, render_template, request, redirect, url_for
from client_server_channel.controls import FirmwaresC, EmployeeC
from .. import view_utils as utls


firmwares = Blueprint('firmwares', __name__, url_prefix='/firmwares')


@firmwares.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template(
            utls.url_join(['firmwares', 'add.html']),
            ids_fullname = EmployeeC.get_all()
        )

    if request.method == 'POST':
        params = request.form
        result = FirmwaresC.add({'name': params['name'],
                                'model': params['model'],
                                'version': params['version'],
                                'description': params['desc'],
                                'author_id': params['emp_id']
        })
        
        if result['success']:
            return redirect(url_for('firmwares.get_all'))

        return result


@firmwares.route('/get/<int:fw_id>')
def get(fw_id):
    fw_info = FirmwaresC.get(fw_id)
    id_name = EmployeeC.get(fw_info['data']['author_id'])['data']
    fullname = f"{id_name['last_name']} {id_name['first_name']} {id_name['middle_name']}"
    
    if fw_info['data'] != []:
        
        return render_template(
            utls.url_join(['firmwares', 'get.html']),
            fw_info=fw_info,
            fullname = fullname
        )

    return redirect(url_for('firmwares.get_all'))


@firmwares.route('/get_all')
def get_all():
    firmwares = FirmwaresC.get_all()
    names_by_ids = EmployeeC.get_names_by_ids(firmwares['data']['author_id'])

    if firmwares['success'] and names_by_ids['success']:
        
        return render_template(
            utls.url_join(['firmwares', 'get_all.html']),
            firmwares = firmwares,
            names_by_ids = names_by_ids['data']
        )

    return redirect(url_for('core.index'))            # TODO later!!!!


@firmwares.route('/update/<int:fw_id>', methods=['GET', 'POST'])
def update(fw_id):
    if request.method == 'GET':
        fw_info = FirmwaresC.get(fw_id)
        id_name = EmployeeC.get(fw_info['data']['author_id'])['data']
        fullname = f"{id_name['last_name']} {id_name['first_name']} {id_name['middle_name']}"
        
        if len(fw_info['data']) > 0:
            
            return render_template(
                utls.url_join(['firmwares', 'update.html']),
                fw_info = fw_info['data'],
                fullname = fullname
            )

        return redirect(url_for('firmwares.get_all'))

    if request.method == 'POST':
        result = FirmwaresC.update({
            'description' : request.form['desc'],
            'fw_id' : fw_id
        })
        
        if result['success']:
            return redirect(url_for('firmwares.get_all'))

        return result


@firmwares.route('/delete/<int:fw_id>', methods=['DELETE'])
def delete(fw_id):
    return FirmwaresC.delete(fw_id)