from flask import Blueprint, redirect, url_for, session, request
from client_server_channel.controls import ProductPhotoC

product_photo = Blueprint('product_photo', __name__, url_prefix='/photo')


@product_photo.route('/add', methods=['POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('employees.login'))


    if request.method == 'POST':
        params = request.json

        result = ProductPhotoC.add({
                        'main_photo' : params['main_photo'],
                        'other_photos' : params['other_photos'],
                        'product_id' : params['product_id'],
                        'add_emp_id' : session['employee']['id'],
                        'modify_emp_id' : session['employee']['id'],
                    })

        return result


@product_photo.route('/update', methods=['POST'])
def update():
    if not 'username' in session:
        return redirect(url_for('employees.login'))

    if request.method == 'POST':
        params = request.json
        result = ProductPhotoC.update_main_photo({
            'main_photo' : params['main_photo'],
            'photos_id' : params['photos_id'],
            'modify_emp_id' : session['employee']['id']
        })

        return result


@product_photo.route('/delete/<int:photo_id>', methods=['DELETE'])
def delete(photo_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	return ProductPhotoC.delete(photo_id)