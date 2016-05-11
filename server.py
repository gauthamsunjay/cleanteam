#!/usr/bin/env python2

import sys
import json

from bottle import route, run, static_file, response, redirect

import utils
import dblayer

if len(sys.argv) != 4 :
    print 'USAGE : ./pgm <hostname / ip> <port> <server root>'
    print 'Example : ' + sys.argv[0] + ' localhost 9000 conf.json'
    exit(1)

HOST_IP = sys.argv[1]
HOST_PORT = int(sys.argv[2])

@route('/cleanteam/static/<filename:path>')
def serve_static(filename) :
    return static_file(filename, root=sys.argv[3])

@route('/')
@route('/test')
def test() :
    return '<h1>wohoo!</h1>'


@route('/cleanteam/locs')
def locs() :
    response.content_type = 'application/json'
    return utils.get_json(dblayer.read_locs())


@route('/cleanteam/clusters')
def clusters() :
    response.content_type = 'application/json'
    return utils.get_json(dblayer.read_clusters())

@route('/cleanteam/cluster_route')
def cluster_route() :
    response.content_type = 'application/json'
    return utils.get_json(dblayer.read_final_route())

@route('/cleanteam')
@route('/cleanteam/index.html')
def serve_index() :
    redirect('/cleanteam/static/index.html')

run(host=HOST_IP, port=HOST_PORT, debug=True)
