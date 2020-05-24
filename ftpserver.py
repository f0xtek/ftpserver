#!/usr/bin/env python3
"""
A simple FTP server for quickly serving up files via FTP

Usage: python3 ftpserver.py [10.10.10.10]

Listens on localhost by default, unless overridden by the first argument.
FTP directory is /tmp/ftp.
"""

import getpass
import sys
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

user = input("Please create a username: ")
password = getpass.getpass(prompt="Please create a password: ", stream=None)
authorizer = DummyAuthorizer()
authorizer.add_user(user, password, "/tmp/ftp", perm="elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer

if len(sys.argv) == 2:
    listen = sys.argv[1]
else:
    listen = '127.0.0.1'

server = FTPServer((listen, 21), handler)
server.serve_forever()
