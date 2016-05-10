#!/usr/bin/env python2

import json
import datetime
import dateutil.parser
import random

import utils
import DBLayer

if __name__ == '__main__' :

    import sys
    if len(sys.argv) != 6 :
        print 'USAGE : ./pgm <json file of co_ords> <max val of garbage> <end date> <valid no of days before end date for garbage> <json locations file>'
        print 'EXAMPLE : ' + sys.argv[0] + ' co_ords 1000 150.5 20 res'
        sys.exit(1)

    co_ords_json = DBLayer.read_co_ords()
    n_gen = len(co_ords_json)

    max_vol = float(sys.argv[2])

    end_date = dateutil.parser.parse(sys.argv[3])
    n_days_before = int(sys.argv[4])
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

    """
    # create json result
    res = []
    for i in range(tot) :
        co_ord_idx = i / n_days_before
        tmp = {}
        tmp['co_ord'] = co_ords_json[co_ord_idx]['co_ord']
        tmp['volume'] = rand_vols[i]
        tmp['datetime'] = rand_dates[i]
        res.append(tmp)
    """
    DBLayer.write_locs(res)
