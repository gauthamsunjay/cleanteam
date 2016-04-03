#!/usr/bin/env python2

import utils

if __name__ == '__main__' :
    
    import sys
    if len(sys.argv) != 5 :
        print sys.argv
        print 'USAGE : ./pgm <coord range file> <no to gen> <max_val> <output file>'
        print 'EXAMPLE : ' + sys.argv[0] + ' bangalore.coord.range 1000 150.5 res'
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

    new_list = utils.add_attr(new_co_ords, rand_vols)

    csv = ''
    for i in new_list :
        tmp = [str(j) for j in i]
        csv += ','.join(tmp) + '\n'
    
    outfile = sys.argv[4]
    f = open(outfile, 'w')
    f.write(csv)
    f.close()
