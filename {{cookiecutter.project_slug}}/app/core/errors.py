from app.core import core


@core.app_errorhandler(403)
def page_forbidden(e):
    return 'We are sorry. You are not allowed to do it.', 403


@core.app_errorhandler(404)
def page_not_found(e):
    return 'We are sorry. It has disappeared what you searched for.', 404


@core.app_errorhandler(500)
def internal_server_error(e):
    return 'We are sorry. It was just too much.', 500
