#!/usr/bin/env python2

import json
import datetime
import dateutil.parser
import random

import utils
import dblayer

if __name__ == '__main__' :

    import sys
    if len(sys.argv) != 4 :
        print 'USAGE : ./pgm <max vol of garbage> <end date> <valid no of days before end date for garbage>'
        print 'EXAMPLE : ' + sys.argv[0] + ' 1000 150.5 20'
        sys.exit(1)

    co_ords_json = dblayer.read_co_ords()
    n_gen = len(co_ords_json)

    max_vol = float(sys.argv[1])

    end_date = dateutil.parser.parse(sys.argv[2])
    n_days_before = int(sys.argv[3])
    tot = n_gen * n_days_before
    
    rand_vols = utils.gen_rand_vols(tot, max_vol)

    rand_dates = utils.gen_rand_dates(tot, end_date, n_days_before)


    # create json result
    res = []
    idx = 0
    for i in range(n_gen) :
        reps = random.randint(0, 20)
        for i in range(reps) :
            tmp = {}
            tmp['co_ord'] = co_ords_json[i]['co_ord']
            tmp['volume'] = rand_vols[idx]
            tmp['datetime'] = rand_dates[idx]
            idx += 1
            res.append(tmp)

    dblayer.write_locs(res)
