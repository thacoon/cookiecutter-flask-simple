from app.core import core


@core.route('/')
def hello():
    return 'Hello, World!'
