from subprocess import call

pip = 'env/bin/pip'

class Components(object):

	def __init__(self,start_message, pypi_id, end_message):
		self.start_message = start_message
		self.pypi_id = pypi_id
		self.end_message = end_message

	def install(self):
		print self.start_message
		call([pip,'install',self.pypi_id])
		print self.end_message

flask = Components(
				"Placing Flask in the backyard\n", 
				"flask", 
				"\nFlask placed\n")

tornado = Components(
				"A Tornado is coming to your backyard\n", 
				"tornado", 
				"\nTornado contained in the backyard\n")

flask_sqla = Components(
				"Placing Flask-SQLAlchemy in the backyard\n", 
				"flask-sqlalchemy", 
				"\nFlask-SQLAlchemy placed\n")

sqla_migrate = Components(
				"Placing SQLAlchemy-Migrate in the backyard\n", 
				"sqlalchemy-migrate", 
				"\nSQLAlchemy-Migrate placed\n##################################################\n# IMPORTANT                                      #'\n# to use SQLAlchemy with MySQL, PostgreSQL and   #'\n# Oracle, you need to install additional modules #\n##################################################\n")

FRAMEWORK_COMPONENTS = [
						flask,
						tornado,
						flask_sqla,
						sqla_migrate]