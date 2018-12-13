from app.core import core
from app.core.exceptions import AppCoreError


@core.route('/')
def hello():
    return 'Hello, World!'


@core.route('/error')
def error():
    raise AppCoreError('Error Error')
