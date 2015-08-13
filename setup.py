"""
setup.py

author: erich@emfeld.com
========================

This file will create your backyard app environment.

To use the file simply run python setup.py

The file will install basic packages of Backyard, which are:
- Flask
- Flask-SQLAlchemy
- SQLAlchemy-Migrate
- Tornado

Additional packages that you may require can be defined in config.py file
using the list of ADDITIONAL_PACKAGES

Note:
Please remember to add mysql-python to GARDEN_TOOLS if you wish to
use MySQL as your database

"""
from subprocess import call

from config import user_config
from builder import Config, FRAMEWORK_COMPONENTS, InstallerTools


class Setup(object):

    def __init__(self, base):
        self.config = Config(base)
        self.user_config = user_config
        self.base = base

    def create_environment(self):
        InstallerTools.create_virtual_environment(self.config)
        InstallerTools.create_db_directory(self.base)
        print '\nNew backyard created, now placing garden \
               tools in the backyard\n'

    def install_components(self):
        print 'Checking if pip needs to be upgraded\n'
        InstallerTools.upgrade_pip()
        print 'pip check done!\n'
        for component in FRAMEWORK_COMPONENTS:
            component.install()

        InstallerTools.fix_migrate(self.base)

        print '\nAll garden tools and creatures are complete\n'
        print '\nYour initial backyard is ready\n'

        if len(self.user_config.ADDITIONAL_GARDEN_TOOLS) > 0:
            print '\nWait, seems like you need some extra tools.\n'
            for package in self.user_config.ADDITIONAL_GARDEN_TOOLS:
                print 'Placing ' + package.title() + " in the backyard\n"
                call([self.config.pip, 'install', package])
                print "\n" + package.title() + " placed\n"

            print '\nAll extra tools placed.\n'

    def end_setup(self):
        print '\nRun ./yard help for full details on what \
               you can do with your backyard.\n'
        print '\nEnjoy your time at the backyard and thank your for using!\n\n'

    def run(self):
        self.create_environment()
        self.install_components()
        self.end_setup()


if __name__ == '__main__':
    config = UserConfig()
    setup = Setup(config.BASEDIR)
    setup.run()


# end of file
