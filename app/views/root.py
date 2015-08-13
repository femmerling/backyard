from flask.views import MethodView
from flask import abort

class RootView(MethodView):

	def get(self):
		return "<h2>Welcome to Backyard.</h2><h3>hint:</h3><p>You need to see over the fence to see the whole backyard</p>"

	def post(self):
		abort(404)

	def delete(self):
		abort(404)

	def put(self):
		abort(404)
