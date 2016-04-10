#!/usr/bin/env python2

import route
import utils
import json

if __name__ == "__main__" :
    import sys

    if len(sys.argv) != 5 :
        print "USAGE : ./pgm <json_locations_file> <num_vehicles> <vehicle_cap> <start_node>"
        exit(1)

    locs = utils.read_json_file(sys.argv[1])

    edge_wt = route.EdgeEval(locs)
    node_wt = route.NodeEval(locs)

    num_nodes = len(locs)
    num_vehicles = int(sys.argv[2])
    vehicle_cap = int(sys.argv[3])
    start_node = int(sys.argv[4])

    res = route.find_optimal_route(num_nodes, num_vehicles, vehicle_cap, start_node, edge_wt.distance, node_wt.distance)

    print json.dumps(res)
