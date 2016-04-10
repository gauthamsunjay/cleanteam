#!/usr/bin/env python2

import json
import datetime

import utils

if __name__ == '__main__' :

    import sys
    if len(sys.argv) != 6 :
        print sys.argv
        print 'USAGE : ./pgm <coord range file> <no to gen> <max val of garbage> <valid no of days before today for garbage> <output file>'
        print 'EXAMPLE : ' + sys.argv[0] + ' bangalore.coord.range 1000 150.5 20 res'
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

    max_vol = float(sys.argv[3])
    rand_vols = utils.gen_rand_vols(n_gen, max_vol)

    n_days_before = sys.argv[4]
    rand_dates = utils.gen_rand_dates(n_gen, datetime.datetime.today(), 20)

    # create json result
    res = []
    for i in range(n_gen) :
        tmp = {}
        tmp['co_ord'] = new_co_ords[i]
        tmp['volume'] = rand_vols[i]
        tmp['datetime'] = rand_dates[i]
        res.append(tmp)

    outfile = sys.argv[5]
    utils.write_json_file(outfile, res)
