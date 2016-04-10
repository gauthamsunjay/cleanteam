#!/usr/bin/env python2

import sys
import json

from bottle import route, run, static_file, response, redirect

import utils

if len(sys.argv) != 3 :
    print sys.argv
    print 'USAGE : ./pgm <hostname / ip> <port>'
    print 'Example : ' + sys.argv[0] + ' localhost 9000'
    exit(1)

HOST_IP = sys.argv[1]
HOST_PORT = int(sys.argv[2])


@route('/cleanteam/static/<filename:path>')
def serve_static(filename) :
    return static_file(filename, root='resources/')

@route('/')
@route('/test')
def test() :
    return "<h1>wohoo!</h1>"


@route('/cleanteam/locs')
def locs() :
    response.content_type = 'application/json'
    return json.dumps(utils.read_json_file('resources/tmpfiles/locs'))

@route('/cleanteam/clusters')
def clusters() :
    response.content_type = 'application/json'
    return json.dumps(utils.read_json_file('resources/tmpfiles/clusters'))

@route('/cleanteam/route1')
def route1() :
    response.content_type = 'application/json'
    tmp = utils.read_json_file('resources/tmpfiles/clusters')
    return json.dumps([i['cluster_center'] for i in tmp])

@route('/cleanteam')
@route('/cleanteam/index.html')
def serve_index() :
    redirect('/cleanteam/static/index.html')

run(host=HOST_IP, port=HOST_PORT, debug=True)
