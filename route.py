#!/usr/bin/env python2

import json
import random
from ortools.constraint_solver import pywrapcp

class EdgeEval :
    def __init__(self) :
        pass

    def distance(self, i, j) :
        return random.randrange(1,8)

class NodeEval :
    def __init__(self) :
        pass

    def distance(self, i, j) :
        return random.randrange(1,8)

def find_optimal_route(num_nodes, num_vehicles, vehicle_cap, start_node, EdgeEval, NodeEval) :
    routing = pywrapcp.RoutingModel(num_nodes, num_vehicles)
    routing.SetDepot(start_node)
    routing.set_first_solution_strategy(routing.ROUTING_PATH_CHEAPEST_ARC)
    routing.SetCost(EdgeEval)
    routing.AddDimension(NodeEval, 0, vehicle_cap, True, "NodeWt")

    soln = routing.Solve()

    res = {}
    if soln :
        res['status'] = 'success'
        routes = []
        for route_number in range(routing.vehicles()) :
            tmp = []
            node = routing.Start(route_number)
            while not routing.IsEnd(node) :
                tmp.append(routing.IndexToNode(node))
                node = soln.Value(routing.NextVar(node))

            tmp.append(routing.IndexToNode(routing.End(route_number)))
            routes.append(tmp)

        res['routes'] = routes

    else :
        res['status'] = 'fail'

    res['num_nodes'] = num_nodes
    res['num_vehicles'] = num_vehicles
    res['start_node'] = start_node
    res['vehicle_capacity'] = vehicle_cap

    return res


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

    edge_wt = EdgeEval()
    node_wt = NodeEval()

    res = find_optimal_route(num_nodes, num_vehicles, vehicle_cap, start_node, edge_wt.distance, node_wt.distance)

    print json.dumps(res)
