#!/usr/bin/env python2

import json
import datetime

import utils

if __name__ == '__main__' :

    import sys
    if len(sys.argv) != 5 :
        print 'USAGE : ./pgm <json file of co_ords> <max val of garbage> <valid no of days before today for garbage> <json locations file>'
        print 'EXAMPLE : ' + sys.argv[0] + ' co_ords 1000 150.5 20 res'
        sys.exit(1)

    co_ords_json = utils.read_json_file(sys.argv[1])
    n_gen = len(co_ords_json)

    max_vol = float(sys.argv[2])
    n_days_before = int(sys.argv[3])
    tot = n_gen * n_days_before
    
    rand_vols = utils.gen_rand_vols(tot, max_vol)

    rand_dates = utils.gen_rand_dates(tot, datetime.datetime.today(), n_days_before)


    # create json result
    res = []
    for i in range(tot) :
        co_ord_idx = i / n_days_before
        tmp = {}
        tmp['co_ord'] = co_ords_json[co_ord_idx]['co_ord']
        tmp['volume'] = rand_vols[i]
        tmp['datetime'] = rand_dates[i]
        res.append(tmp)

    outfile = sys.argv[4]
    utils.write_json_file(outfile, res)
