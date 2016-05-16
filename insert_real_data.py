#!/usr/bin/env python2

import json
import dateutil.parser

import dblayer

if __name__ == '__main__' :
    import sys

    if len(sys.argv) != 2 :
        print 'Usage : ' + sys.argv[0] + ' <alldata.csv>'
        exit(1)

    f = open(sys.argv[1], 'r')
    w = f.read()
    f.close()

    l = w.strip().split('\n')
    l = [i.strip().split(',') for i in l]

    res = []
    for i in l :
        tmp = {}
        tmp['co_ord'] = map(float, i[:2])
        tmp['volume'] = float(i[3])
        tmp['datetime'] = dateutil.parser.parse(i[2])
        res.append(tmp)

    dblayer.write_locs(res)
