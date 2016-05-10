#!/usr/bin/env python2

import sys
import json

from bottle import route, run, static_file, response, redirect

import utils
import DBLayer

if len(sys.argv) != 3 :
    print 'USAGE : ./pgm <hostname / ip> <port>'
    print 'Example : ' + sys.argv[0] + ' localhost 9000 conf.json'
    exit(1)

HOST_IP = sys.argv[1]
HOST_PORT = int(sys.argv[2])

@route('/cleanteam/static/<filename:path>')
def serve_static(filename) :
    return static_file(filename, root=server_conf['static_files_root'])

@route('/')
@route('/test')
def test() :
    return '<h1>wohoo!</h1>'


@route('/cleanteam/locs')
def locs() :
    response.content_type = 'application/json'
    return utils.get_json(DBLayer.read_locs())


@route('/cleanteam/clusters')
def clusters() :
    response.content_type = 'application/json'
    return utils.get_json(DBLayer.read_clusters())

@route('/cleanteam/cluster_route')
def cluster_route() :
    response.content_type = 'application/json'
    return utils.get_json(DBLayer.read_final_route())

@route('/cleanteam')
@route('/cleanteam/index.html')
def serve_index() :
    redirect('/cleanteam/static/index.html')

run(host=HOST_IP, port=HOST_PORT, debug=True)
