from app.skeletons import BaseSkeleton

class ErrorSkeleton(object):

    @staticmethod
    def bad_request(message="Bad request"):
        return ErrorSkeleton.response(400, message)

    @staticmethod
    def unauthorized(message="Unauthorized"):
        return ErrorSkeleton.response(401, message)

    @staticmethod
    def forbidden(message="Forbidden"):
        return ErrorSkeleton.response(403, message)

    @staticmethod
    def not_found(message="Not found"):
        return ErrorSkeleton.response(404, message)

    @staticmethod
    def not_allowed(message="Method not allowed"):
        return ErrorSkeleton.response(405, message)

    @staticmethod
    def server_error(message="Server error"):
        return ErrorSkeleton.response(500, message)

    @staticmethod
    def service_unavailable(message="Service unavailable"):
        return ErrorSkeleton.response(503, message)

    @staticmethod
    def response(status_code, message):
        payload = {'message':message}
        return BaseSkeleton(status_code, payload).response()