"""
config.py

author: erich@emfeld.com
========================

This file acts as the configuration holder for the environment.
If you want to define a global configuration please define it here.

Naming convention:
- Use capital letters.
- If needed, use underscores ('_') as separators between words 
"""

import os

# Additional packages that you need
ADDITIONAL_GARDEN_TOOLS = []

# The root directory of backyard
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Application server port. Default value is 8888
SERVER_PORT = 8888

# The database migration file storage folder
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'warehouse')

# 
#SQLALCHEMY_DATABASE_URI = 'mysql://root:password01@127.0.0.1/flasklearn' 
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'greenhouse/app.db')
#SQLALCHEMY_DATABASE_URI = 'postgresql://scott:tiger@localhost/mydatabase'
#SQLALCHEMY_DATABASE_URI = 'oracle://scott:tiger@127.0.0.1:1521/sidname'

VALID_DATA_TYPES = [
    'bigint', 'biginteger', 'binary', 'blob', 'boolean', 'date', 'datetime',
    'enum', 'float', 'int','integer', 'interval', 'pickletype', 'largebinary', 
    'numeric', 'schematype',  'smallinteger', 'smallint', 'string', 'text',
    'time', 'unicode', 'unicodetext'
]

WHITE_SPACE = "\t"