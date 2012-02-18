""" Module: connection_manager

...
"""
import urllib, urllib2

import response_parser

def create_request(host, port):
    return urllib2.Request("http://" + host + ":" + port + "/db/data/"


