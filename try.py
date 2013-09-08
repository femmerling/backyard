#! backyard/bin/python
"""
try.py

author: erich@emfeld.com
========================

This file acts as the test server.


WARNING!
This server is not for production usage it is only intended
as a testing server. Please use gunicorn or tornado webserver.

Please refer to yard help for more info.

"""
from app import app
from config import SERVER_PORT

app.run(debug = True,port=SERVER_PORT)


# end of file