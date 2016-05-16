#!/usr/bin/env python2

import json
import dateutil.parser

if __name__ == '__main__' :
    import sys

    if len(sys.argv) != 3 :
        print sys.argv
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
        tmp['datetime'] = dateutil.parser.parse(i[2]).isoformat()
        res.append(tmp)

    f = open(sys.argv[2], 'w')
    f.write(json.dumps(res))
    f.close()
