#!/usr/bin/env python2

import json
import datetime

import utils
import DBLayer

if __name__ == '__main__' :

    import sys
    if len(sys.argv) != 4 :
        print 'USAGE : ./pgm <coord range file> <no to gen> <json locations file>'
        print 'EXAMPLE : ' + sys.argv[0] + ' bangalore.coord.range 1000 res'
        exit(1)

    infile = sys.argv[1]
    f = open(infile, 'r')
    w = f.read()
    f.close()
    lines = w.strip().split('\n')
    co_ord1 = map(float, lines[0].strip().split(','))
    co_ord2 = map(float, lines[1].strip().split(','))

    n_gen = int(sys.argv[2])

    new_co_ords = utils.gen_rand_co_ords(co_ord1, co_ord2, n_gen)

    # create json result
    res = []
    for i in range(n_gen) :
        tmp = {}
        tmp['co_ord'] = new_co_ords[i]
        res.append(tmp)

    DBLayer.write_co_ords(res)
