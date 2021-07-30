from flask import Blueprint, redirect, url_for


error_pages = Blueprint('error_pages', __name__)


@error_pages.app_errorhandler(404)
def error_404(error):
	return redirect(url_for('core.index'))


@error_pages.app_errorhandler(403)
def error_403(error):
	return 'error page 403', 403