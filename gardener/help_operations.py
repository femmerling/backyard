def help():
    # This lists the commands used by the db_tools.py.
    print '\nThe general usage pattern of the tool is ./yard [options] [extra parameters]\n'
    print 'The following are the available options:\n'
    print ' blow or b            : Run the production web server'
    print ' downgrade or d       : Downgrade the database to the previous migration version.'
    print '\t\t\tTo downgrade to a specific version use downgrade [version number]'
    print ' grow or g            : Generates a new controller, either seed, stub or tree'
    print '\t\t\tSeed will only generate model files while tree will generate both model file and REST controller. Stub is an initial endpoint with empty controller'
    print '\t\t\tFor stub the pattern is grow stub [controller name]'
    print '\t\t\tFor seed the pattern is grow seed [model name] [<field name>:<field type>--<field length (if applicable. otherwise, default will be used)>]'
    print '\t\t\tFor tree the pattern is grow tree [model name] [<field name>:<field type>--<field length (if applicable. otherwise, default will be used)>]'
    print '\t\t\tFor more documentation please see http://docs.sqlalchemy.org/en/rel_0_7/core/types.html#types-generic'
    print ' help or h            : Display the help file'
    print ' place or p           : Install a new python package into the backyard.'
    print '\t\t\tThe pattern is place [package name]'
    print ' shove or s           : Create the database for the first usage. Only use this if you want to create the database for the first time'
    print ' try or t             : Run The Development Server'
    print ' upgrade or u         : Upgrade the database to the latest migration version'
    print ' version or v         : Check current database version.'
    print ' water or w           : Create the migration script for migration process and perform the migration\n'

# end of file