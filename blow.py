#! env/bin/python
"""
blow.py

author: erich@emfeld.com
========================

This file acts as the tornado web server.
It simply wraps the app into a WSGI container of tornado web server.

Configs for port number is available in config.py file.

"""
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado import autoreload
from app import app
from config import user_config

print "\nbackyard is now running powered by Tornado Web Server on port " + str(user_config.SERVER_PORT) + " ...\n"

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(user_config.SERVER_PORT)
autoreload.start()
IOLoop.instance().start()


# end of file