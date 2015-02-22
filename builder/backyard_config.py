import os.path

class Config(object):

	def __init__(self,base_directory):
		self.base = base_directory
		self.environment_name = "env"
		self.environment_path = "#! "+self.environment_name+"/bin/python"


		self.pip = self.environment_name +'/bin/pip'
		self.valid_data_types = [
		    'bigint', 'biginteger', 'binary', 'blob', 'boolean', 'date', 'datetime',
		    'enum', 'float', 'int','integer', 'interval', 'pickletype', 'largebinary', 
		    'numeric', 'schematype',  'smallinteger', 'smallint', 'string', 'text',
		    'time', 'unicode', 'unicodetext'
		]

		self.try_path = os.path.join(self.base, 'try.py')
		self.v_path = os.path.join(self.base, 'virtualenv.py')
		self.blow_path = os.path.join(self.base, 'blow.py')
		self.yard_path = os.path.join(self.base, 'yard')