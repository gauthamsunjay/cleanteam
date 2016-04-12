#!/usr/bin/env python2

import tsp_route
import utils
import json

class EdgeEval :
    def __init__(self, locations) :
        self.locations = locations
        for i in range(len(self.locations)) :
            self.locations[i]['_id'] = i
        self.co_ords = [i['co_ord'] for i in self.locations]

    def distance(self, i, j) :
        return utils.getGeoDist(self.co_ords[i], self.co_ords[2])

class NodeEval :
    def __init__(self, locations) :
        self.locations = locations
        self.volumes = [i['volume'] for i in self.locations]

    def distance(self, i, j) :
        # provide demand of i
        return self.volumes[i]

if __name__ == '__main__' :
    import sys

    if len(sys.argv) != 6 :
        print 'USAGE : ./pgm <json clusters file> <num_vehicles> <vehicle_cap> <start_node> <json intial route file>'
        print sys.argv
        exit(1)

    clusters = utils.read_json_file(sys.argv[1])

    locs = [i['cluster_center'] for i in clusters]
    comps = [i['components'] for i in clusters]

    edge_wt = EdgeEval(locs)
    node_wt = NodeEval(locs)

    num_nodes = len(locs)
    num_vehicles = int(sys.argv[2])
    vehicle_cap = int(sys.argv[3])
    start_node = int(sys.argv[4])

    route = tsp_route.find_optimal_route(num_nodes, num_vehicles, vehicle_cap, start_node, edge_wt.distance, node_wt.distance)

    utils.write_json_file(sys.argv[5], route)
