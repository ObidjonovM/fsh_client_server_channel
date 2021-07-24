from flask import Flask
from .views import (clients, core, employees, products, error_pages,
                    currency, unit, supplier, carrier, shipping_type,
                    tracking_status, sp_type, sp_logistic)
from . import config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

app.register_blueprint(clients)
app.register_blueprint(core)
app.register_blueprint(employees)
app.register_blueprint(products)
app.register_blueprint(error_pages)
app.register_blueprint(currency)
app.register_blueprint(unit)
app.register_blueprint(supplier)
app.register_blueprint(carrier)
app.register_blueprint(shipping_type)
app.register_blueprint(tracking_status)
app.register_blueprint(sp_type)
app.register_blueprint(sp_logistic)