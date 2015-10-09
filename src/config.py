#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author Jan Löser <jloeser@suse.de>
# Published under the GNU Public Licence 2
PROGRAM_NAME = 'redfish-server'
PROGRAM_NAME_SHORT = 'rfserver'
ROOT_LOGGER = 'rfserver'

SERVER_ADDRESS = '0.0.0.0'
SERVER_PORT = 4443
SERVER_SSL_CRT = '../server.crt'
SERVER_SSL_KEY = '../server.key'

MAJOR_VERSION = 0
MINOR_VERSION = 1
PROTOCOL_VERSION = 1

PROGRAM_VERSION = "{}.{}".format(MAJOR_VERSION, MINOR_VERSION)
VERSION_STR = "v" + str(PROTOCOL_VERSION)

USER = 'root'
PASS = 'test'

ROOT_URL = '/rest'
SERVICEROOT_URL = "{}/v{}/".format(ROOT_URL, PROTOCOL_VERSION)
