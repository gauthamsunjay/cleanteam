#!/usr/bin/env python2

import json

import utils

if __name__ == '__main__' :
    import sys
    if len(sys.argv) != 3 :
        print 'USAGE : ./pgm <json conf file> <output shell script>'
        print 'EXAMPLE : ' + sys.argv[0] + ' conf.json driver.sh'
        exit(1)

    conf = utils.read_json_file(sys.argv[1])

    pgms = conf['pgms']
    s = '#!/usr/bin/env bash'
    s += '\n\n'
    cmds = []
    for pgm in pgms : 
        cmd = pgm['name'] + ' '
        for arg in pgm['args'] :
            cmd += str(arg['value']) + ' '
    
        if pgm['use'] == 'true' :
            cmds.append(cmd)

    s += ' && \\\n'.join(cmds)        

    s += '\n'

    f = open(sys.argv[2], 'w')
    f.write(s)
    f.close()
