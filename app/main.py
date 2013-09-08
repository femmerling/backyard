from app import app
from flask import jsonify

def not_found(error):
    response = jsonify({'code': 404,'message': 'Not found'})
    response.status_code = 404
    return response

def not_allowed(error):
    response = jsonify({'code': 405,'message': 'Method not allowed'})
    response.status_code = 405
    return response

app.error_handler_spec[None][404] = not_found
app.error_handler_spec[None][405] = not_allowed

from controllers import base_view

app.register_blueprint(base_view)