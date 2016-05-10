#!/usr/bin/env python2


import sys
import json
import datetime
from scipy.cluster.vq import kmeans, vq

import utils
import DBLayer

def parse_json_input() :
    data = DBLayer.read_locs()

    co_ords = []
    vols = []
    for i in data :
        co_ords.append(i['co_ord'])
        vols.append(i['volume'])

    return data, co_ords, vols

def get_means(data, num_centers):
    centroids, _ = kmeans(data, num_centers)
    indexes, _ = vq(data, centroids)
    return centroids, indexes

if __name__ == '__main__' :
    import csv
    if len(sys.argv) != 2 :
        print sys.argv
        print 'USAGE : ./pgm <num_centers>'
        print 'EXAMPLE : ' + sys.argv[0] + ' 10'
        exit(1)

    num_centers = int(sys.argv[1])

    locations, co_ords, volumes = parse_json_input()

    centroids, indexes = get_means(co_ords, num_centers)
    volume_in_centers = [0] * num_centers
    comps = {}
    for i, v in enumerate(volumes):
        center = indexes[i]
        if center not in comps.keys() :
            comps[center] = []
        comps[center].append(locations[i])
        volume_in_centers[center] += v

    res = []
    for i in range(len(centroids)) :
        tmp = {}
        tmp['cluster_center'] = {}
        tmp['cluster_center']['co_ord'] = list(centroids[i])
        tmp['cluster_center']['volume'] = volume_in_centers[i]
        tmp['cluster_center']['datetime'] = datetime.datetime.today()
        tmp['components'] = comps[i]
        res.append(tmp)

    DBLayer.write_clusters(res)
