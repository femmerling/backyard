from subprocess import call
from builder import Config
from config import UserConfig

user_config = UserConfig()
config = Config(user_config.BASEDIR)

def install_package(package_name):
    if not package_name:
        print "You need to specify a valid package name"
    else:
        call([config.pip, 'install', package_name.lower()])


# end of file