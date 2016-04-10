#!/usr/bin/env python2

import json
import random
import tsp_route

class EdgeConst :
    def __init__(self) :
        pass

    def distance(self, i, j) :
        return random.randint(1,6)

class NodeConst :
    def __init__(self) :
        pass

    def distance(self, i, j) :
        # provide demand of i
        return random.randint(1,7)

if __name__ == '__main__' :
    import sys

    if len(sys.argv) != 5 :
        print 'USAGE : ./pgm <num_nodes> <num_vehicles> <vehicle_cap> <start_node>'
        print 'Example : ' + sys.argv[0] + ' 10 3 8 4'
        exit(1)

    num_nodes = int(sys.argv[1])
    num_vehicles = int(sys.argv[2])
    vehicle_cap =  int(sys.argv[3])
    start_node = int(sys.argv[4])

    edge_wt = EdgeConst()
    node_wt = NodeConst()

    res = tsp_route.find_optimal_route(num_nodes, num_vehicles, vehicle_cap, start_node, edge_wt.distance, node_wt.distance)

    print json.dumps(res)
