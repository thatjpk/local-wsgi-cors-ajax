#!/usr/bin/env python

from wsgiref.simple_server import make_server
import json


def cors_json(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*')
    ]
    start_response(status, response_headers)

    return [json.dumps({'foo': 'bar'})]

httpd = make_server('localhost', 9011, cors_json)
httpd.serve_forever()
