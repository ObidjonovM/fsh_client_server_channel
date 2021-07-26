from flask import Blueprint, render_template, request, redirect, url_for, session
from client_server_channel.controls import SubscriptionC
from .. import view_utils as utls

subscription = Blueprint('subscription', __name__, url_prefix='/subscription')


@subscription.route('/add', methods=['GET', 'POST'])
def add():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	if request.method == 'GET':

		return render_template(
			utls.url_join(['clients', 'subscription', 'add.html'])
		)

	if request.method == 'POST':
		params = request.form
		result = SubscriptionC.add({
			'name' : params['name'],
			'description' : params['desc'],
			'monthly_fee' : params['monthly_fee'],
			'add_emp_id' : session['employee']['id'],
			'modify_emp_id' : session['employee']['id']
		})

		if result['success']:
			return redirect(url_for('clients.subscription.all'))

		return result


@subscription.route('/get/<int:subs_id>')
def get(subs_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	subs_info = SubscriptionC.get(subs_id)
	
	if len(subs_info['data']) > 0:
		
		return render_template(
			utls.url_join(['clients', 'subscription', 'get.html']),
			subs_info = subs_info
		)

	return redirect(url_for('clients.subscription.all'))


@subscription.route('/all')
def all():
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	subs_info = SubscriptionC.get_all()
	
	if subs_info['success']:
		if len(subs_info['data']) > 0:
			return render_template(
				utls.url_join(['clients', 'subscription', 'all.html']),
				subs_info = subs_info
			)
		
		return render_template(
			utls.url_join(['clients', 'subscription', 'all.html'])
		)

	return redirect(url_for('core.index'))

@subscription.route('/update/<int:subs_id>', methods=['GET', 'POST'])
def update(subs_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	if request.method == 'GET':
		subs_info = SubscriptionC.get(subs_id)
	
		if len(subs_info['data']) > 0:
			return render_template(
				utls.url_join(['clients', 'subscription', 'update.html']),
				subs_info = subs_info
			)

		return redirect(url_for('clients.subscription.all'))

	if request.method == 'POST':
		params = request.form
		result = SubscriptionC.update({
			'description' : params['desc'],
			'monthly_fee' : params['monthly_fee'],
			'modify_emp_id' : session['employee']['id'],
			'subs_id' : subs_id
		})

		if result['success']:
			return redirect(url_for('clients.subscription.all'))

		return result


@subscription.route('/delete/<int:subs_id>', methods=['DELETE'])
def delete(subs_id):
	if not 'username' in session:
		return redirect(url_for('employees.login'))

	return SubscriptionC.delete(subs_id)