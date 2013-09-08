from subprocess import call

def install_package(package_name):
    if not package_name:
        print "You need to specify a valid package name"
    else:
        pip = 'backyard/bin/pip'

        call([pip, 'install', package_name.lower()])


# end of file