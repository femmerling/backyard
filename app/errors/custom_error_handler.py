from app import app
from app.skeletons import ErrorSkeleton

def bad_request():
    return ErrorSkeleton.bad_request()

def unauthorized():
    return ErrorSkeleton.unauthorized()

def forbidden():
    return ErrorSkeleton.forbidden()

def not_found():
    return ErrorSkeleton.not_found()

def not_allowed():
    return ErrorSkeleton.not_allowed()

def server_error():
    return ErrorSkeleton.server_error()

def service_unavailable():
    return ErrorSkeleton.service_unavailable()

def attach_custom_error_handlers():
    app.error_handler_spec[None][400] = bad_request
    app.error_handler_spec[None][401] = unauthorized
    app.error_handler_spec[None][403] = forbidden
    app.error_handler_spec[None][404] = not_found
    app.error_handler_spec[None][405] = not_allowed
    app.error_handler_spec[None][500] = server_error
    app.error_handler_spec[None][503] = service_unavailable