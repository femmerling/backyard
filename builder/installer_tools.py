import os.path
from subprocess import call

class InstallerTools(object):

	@staticmethod
	def update_environment(file_path,environment_path):
		update_file = open(file_path, 'r')
		original_lines = update_file.readlines()
		original_lines[0] = environment_path+'\n'
		update_file.close()
		update_file = open(file_path, 'w')
		for lines in original_lines:
			update_file.write(lines)

		update_file.close()

	@staticmethod
	def fix_migrate(base_directory):
		print "\nFixing the migrate bug \n"
		buggy_path = os.path.join(base_directory, 
						 'env/lib/python2.7/site-packages/migrate/versioning/schema.py')
		buggy_file = open(buggy_path,'r')
		original_lines = buggy_file.readlines()
		original_lines[9] = "from sqlalchemy import exc as sa_exceptions\n"
		buggy_file.close()
		update_file = open(buggy_path,'w')
		for lines in original_lines:
			update_file.write(lines)
		update_file.close()

	@staticmethod
	def refresh_environment(framework_config):
		InstallerTools.update_environment(framework_config.yard_path,framework_config.environment_path)
		InstallerTools.update_environment(framework_config.blow_path,framework_config.environment_path)
		InstallerTools.update_environment(framework_config.try_path,framework_config.environment_path)

	@staticmethod
	def change_permissions(framework_config):
		call(['chmod', 'a+x', framework_config.yard_path])
		call(['chmod', 'a+x', framework_config.blow_path])
		call(['chmod', 'a+x', framework_config.try_path])

	@staticmethod
	def create_db_directory(base_directory):
		if not os.path.exists(os.path.join(base_directory, 'storage/')):
			os.makedirs(os.path.join(base_directory, 'storage/'))

	@staticmethod
	def create_virtual_environment(framework_config):
		call(['python', framework_config.v_path, framework_config.environment_name])
		InstallerTools.refresh_environment(framework_config)
		InstallerTools.change_permissions(framework_config)
