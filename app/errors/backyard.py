class BackyardError(Exception):
	pass

class UnauthorizedAccessError(BackyardError):
	pass

class ForbiddenAccessError(BackyardError):
	pass

class ResourceNotFoundError(BackyardError):
	pass

class MethodNotAllowedError(BackyardError):
	pass