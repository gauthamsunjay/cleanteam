#!/usr/bin/env python2

import json
import datetime
import dateutil.parser

import utils

'''
    Helper Class
    Init with json_clusters
    Use : getTotalVolCost(self, routes)
          getTotalDistCost(self, routes)
    Use and modify : getTotalCost(self, routes)
'''
class CalcHelper :
    def __init__(self, clusters_) :
        self.clusters = []
        self.raw_clusters = {}
        for i in range(len(clusters)) :
            tmp = clusters_[i]
            tmp['_id'] = i
            self.clusters.append(tmp)

        self.cluster_centers = {}
        for cluster in clusters :
            _id = cluster['_id']
            self.cluster_centers[_id] = cluster['cluster_center']['co_ord']

        self.vols = {}
        for cluster in self.clusters :
            _id = cluster['_id']
            self.vols[_id] = {}
            for loc in cluster['components'] :
                date = dateutil.parser.parse(loc['datetime'])
                date = date.date()
                date = date.isoformat()
                if date not in self.vols[_id].keys() :
                    self.vols[_id][date] = 0
                self.vols[_id][date] += loc['volume']

    def getVol(self, nodeidx, date) :
        tmp_date = date.isoformat()

        if tmp_date in self.vols[nodeidx].keys() :
            res = self.vols[nodeidx][tmp_date]
        else :
            res = 0

        return res

    def getRouteVol(self, route, date) :
        res = 0
        for i in route :
            res += self.getVol(i, date)

        return res

    def getRouteVolAll(self, route, date1, date2) :
        all_dates = []
        for x in range((date2-date1).days + 1) :
            tmp = date1 + datetime.timedelta(days=x)
            all_dates.append(tmp)
        res = 0
        for date in all_dates :
            res += self.getRouteVol(route, date)

        return res

    def getTotalVolCost(self, routes) :
        res = 0
        today = datetime.datetime.today().date()
        today_20daysprev = today - datetime.timedelta(days=20)
        for route in routes :
            res += self.getRouteVolAll(route, today_20daysprev, today)

        return res

    def getRouteDist(self, route) :
        res = 0
        for i in range(0, len(route) - 1) :
            co_ord1 = self.cluster_centers[route[i]]
            co_ord2 = self.cluster_centers[route[i+1]]
            res += utils.getGeoDist(co_ord1, co_ord2)
        return res

    def getTotalDistCost(self, routes) :
        res = 0
        for route in routes :
            res += self.getRouteDist(route)

        return res

    def getTotalCost(self, routes) :
        distcost = self.getTotalDistCost(routes)
        volcost = self.getTotalVolCost(routes)

        # apply formula and come to a value...
        return volcost / 10.0 + distcost

# Core algorithm implementation requirement.
def make_random_change(routes) :
    return routes

if __name__ == "__main__" :
    import sys

    if len(sys.argv) != 4 :
        print "USAGE : ./pgm <json clusters file> <json initial route file> <json final routes>"
        exit(1)

    clusters = utils.read_json_file(sys.argv[1])
    calc_helper = CalcHelper(clusters)

    route = utils.read_json_file(sys.argv[2])
    routes = route['routes']

    '''
        Core algorithm implementation
    '''
    curr_routes = routes
    curr_cost = calc_helper.getTotalCost(curr_routes)
    for i in range(30) :
        prev_routes = curr_routes
        prev_cost = curr_cost

        curr_routes = make_random_change(prev_routes)
        curr_cost = calc_helper.getTotalCost(curr_routes)

        if prev_cost > curr_cost :
            prev_routes = curr_routes
            prev_cost = curr_cost
        else :
            pass

    # putting clusters back instead of _id
    res = []
    for route in prev_routes :
        tmp = []
        for node in route :
            tmp.append(calc_helper.clusters[node])

        res.append(tmp)

        json_res = {'cost' : prev_cost, 'routes' : res}

    utils.write_json_file(sys.argv[3], json_res)
