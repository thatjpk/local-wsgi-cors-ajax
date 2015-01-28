#!/usr/bin/env python

from wsgiref.simple_server import make_server


def origin_html(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    f = open('./index.html', 'rb')
    return [f.read()]

httpd = make_server('localhost', 9010, origin_html)
httpd.serve_forever()
