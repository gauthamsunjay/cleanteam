from ortools.constraint_solver import pywrapcp

def find_optimal_route(num_nodes, num_vehicles, vehicle_cap, start_node, EdgeEval, NodeEval) :
    routing = pywrapcp.RoutingModel(num_nodes, num_vehicles)
    routing.SetDepot(start_node)
    routing.set_first_solution_strategy(routing.ROUTING_PATH_CHEAPEST_ARC)
    routing.SetCost(EdgeEval)
    routing.AddDimension(NodeEval, 0, vehicle_cap, True, 'NodeWt')

    soln = routing.Solve()

    res = {}
    if soln :
        res['status'] = 'success'
        routes = []
        for route_number in range(routing.vehicles()) :
            tmp = []
            node = routing.Start(route_number)
            while not routing.IsEnd(long(node)) :
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
