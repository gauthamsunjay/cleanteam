#!/usr/bin/env python2

import sys

from bottle import route, run, static_file

if len(sys.argv) != 3 :
    print sys.argv
    print 'USAGE : ./pgm <hostname / ip> <port>'
    print 'Example : ' + sys.argv[0] + ' localhost 9000'
    exit(1)

HOST_IP = sys.argv[1]
HOST_PORT = int(sys.argv[2])


@route('/static/<filename:path>')
def serve_static(filename) :
    return static_file(filename, root='resources/')

@route('/')
@route('/test')
def test() :
    return "<h1>wohoo!</h1>"

run(host=HOST_IP, port=HOST_PORT, debug=True)
