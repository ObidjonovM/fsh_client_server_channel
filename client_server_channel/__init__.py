from flask import Flask

from .clients import clients
from .core import core
from .employees import employees
from .products import products
from .error_pages import error_pages



app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

app.register_blueprint(clients)
app.register_blueprint(core)
app.register_blueprint(employees)
app.register_blueprint(products)
app.register_blueprint(error_pages)