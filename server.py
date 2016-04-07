#!/usr/bin/env python2

import sys
import json

from bottle import route, run, static_file, response

def read_json_file(json_file) :
    f = open(json_file)
    w = f.read()
    f.close()
    return json.loads(w)

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


@route('/locs')
def locs() :
    response.content_type = 'application/json'
    return json.dumps(read_json_file('resources/tmpfiles/locs'))

@route('/clusters')
def clusters() :
    response.content_type = 'application/json'
    return json.dumps(read_json_file('resources/tmpfiles/clusters'))

@route('/route1')
def route1() :
    response.content_type = 'application/json'
    tmp = read_json_file('resources/tmpfiles/clusters')
    res = []
    for i in tmp :
        res.append(i['cluster_center'])

    return json.dumps(res)

run(host=HOST_IP, port=HOST_PORT, debug=True)
