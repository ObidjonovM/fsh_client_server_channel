from flask import Flask
from .views import (clients, core, employees, products, 
                    error_pages, firmwares, departments)
from . import config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

app.register_blueprint(clients)
app.register_blueprint(core)
app.register_blueprint(employees)
app.register_blueprint(products)
app.register_blueprint(error_pages)
app.register_blueprint(firmwares)
app.register_blueprint(departments)

