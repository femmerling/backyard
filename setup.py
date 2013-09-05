"""
setup.py

author: erich@emfeld.com
========================

This file will create your backyard app environment.

To use the file simply run python setup.py

The file will install basic packages of EmeraldBox, which are:
- Flask
- Flask-SQLAlchemy
- SQLAlchemy-Migrate
- Tornado
- Gunicorn

Additional packages that you may require can be defined in config.py file
using the list of ADDITIONAL_PACKAGES

Note:
Please remember to add mysql-python to GARDEN_TOOLS if you wish to
use MySQL as your database

"""

import os.path
import platform

from subprocess import call

from config import BASEDIR, GARDEN_TOOLS

current_platform = platform.system()

#this is the path to the jog.py file which will act as the testing server
jog_path = os.path.join(BASEDIR, 'jog.py')
#this is the path to the virtualenv file
v_path = os.path.join(BASEDIR, 'virtualenv.py')
#this is the path to the mow.py file which will act as the tornado based production server
mow_path = os.path.join(BASEDIR, 'mow.py')
#this is the path to the hammock.py file which will act as the gunicorn based production server
hammock_path = os.path.join(BASEDIR, 'hammock.py')
#this is the path to the yard.py file, the main framework tool file
yard_path = os.path.join(BASEDIR, 'yard.py')

"""
This will auto adjust the python runtime being used by the file.

Todo:
On windows this has no effect. Need to do more research on making 
it executable like in UNIX/Linux

"""

def update_environment(file_path):
	update_file = open(file_path, 'r')
	original_lines = update_file.readlines()
	original_lines[0] = '#! backyard/bin/python\n'
	if current_platform == 'Windows':
		original_lines[0] = '#! backyard\Scripts\python\n'
	update_file.close()
	update_file = open(file_path, 'w')
	for lines in original_lines:
		update_file.write(lines)

	update_file.close()


# """
# This is to fix the migrate versioning bug.
# Will be removed when the bug on the original package is fixed

# """

# def tempfix_migrate():
# 	print "\nFixing the migrate bug \n"
# 	buggy_path = os.path.join(BASEDIR, 
# 					 'backyard/lib/python2.7/site-packages/migrate/versioning/schema.py')
# 	if current_platform == 'Windows':
# 		buggy_path = os.path.join(BASEDIR, 
# 					 'backyard\lib\site-packages\migrate\\versioning\schema.py')
# 	buggy_file = open(buggy_path,'r')
# 	original_lines = buggy_file.readlines()
# 	original_lines[9] = "\n"
# 	buggy_file.close()
# 	update_file = open(buggy_path,'w')
# 	for lines in original_lines:
# 		update_file.write(lines)
# 	update_file.close()

update_environment(yard_path)
update_environment(mow_path)
update_environment(jog_path)
update_environment(hammock_path)

bin_base = 'backyard/bin/pip'
if current_platform == 'Windows':
	bin_base = 'backyard\Scripts\pip'
	if not os.path.exists(os.path.join(BASEDIR, 'db\\')):
		os.makedirs(os.path.join(BASEDIR, 'db\\'))
	call(['python', v_path, 'backyard'])	
else:
	if not os.path.exists(os.path.join(BASEDIR, 'db/')):
		os.makedirs(os.path.join(BASEDIR, 'db/'))
	call(['python', v_path, 'backyard'])
	call(['chmod', 'a+x', yard_path])
	call(['chmod', 'a+x', mow_path])
	call(['chmod', 'a+x', jog_path])
	call(['chmod', 'a+x', hammock_path])

print '\nNew backyard created, now placing garden tools in the backyard\n'

print 'Placing Flask in the backyard\n'
call([bin_base, 'install', 'flask'])
print '\nFlask placed\n'

# print 'Placing SQLAlchemy in the backyard\n'
# call([bin_base, 'install', 'sqlalchemy'])
# print '\nSQLAlchemy placed\n'

print 'Placing Flask-SQLAlchemy in the backyard\n'
call([bin_base, 'install', 'flask-sqlalchemy'])
print '\nFlask-SQLAlchemy placed\n'

print 'Placing SQLAlchemy-Migrate in the backyard\n'
call([bin_base, 'install', 'sqlalchemy-migrate'])
print '\nSQLAlchemy-Migrate placed\n'
print '##################################################'
print '# IMPORTANT                                      #'
print '# to use SQLAlchemy with MySQL, PostgreSQL and   #'
print '# Oracle, you need to install additional modules #'
print '##################################################\n'

# tempfix_migrate()

print 'A Tornado is coming to your backyard\n'
call([bin_base, 'install', 'tornado'])
print '\nTornado contained in the backyard\n'

print 'A Green Unicorn is coming to your backyard\n'
call([bin_base, 'install', 'gunicorn'])
print '\nGreen Unicord Stays in the backyard\n'

print '\nAll garden tools and creatures are complete\n'
print '\nYour initial backyard is ready\n'

if len(GARDEN_TOOLS) > 0:
	print '\nWait, seems like you need some extra tools.\n'
	for package in GARDEN_TOOLS:
		print 'Placing ' + package.title() + " in the backyard\n"
		call([bin_base,'install',package])
		print "\n" + package.title() + " placed\n"

	print '\nAll extra tools placed.\n'

print '\nRun ./yard.py -h for full details on what you can do with your backyard.\n'
print '\nEnjoy your time at the backyard and thank your for using!\n\n'

# end of file