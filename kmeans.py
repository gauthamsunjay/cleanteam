#!/usr/bin/env python2 


import sys
import json
import datetime
from scipy.cluster.vq import kmeans, vq

import utils

def read_json_input(json_file) :
    f = open(json_file, 'r')
    w = f.read()
    f.close()
    data = json.loads(w)
    
    locs = []
    vols = []
    for i in data :
        locs.append(i['co_ord'])
        vols.append(i['volume'])

    return locs, vols

def write_json_output(json_file, py_obj) :
    f = open(json_file, 'w')
    f.write(json.dumps(py_obj, default=utils.json_serial))
    f.close()

def get_means(data, num_centers):
    centroids, _ = kmeans(data, num_centers)
    indexes, _ = vq(data, centroids)
    return centroids, indexes

if __name__ == "__main__":
    import csv
    if len(sys.argv) != 4 :
        print sys.argv
        print 'USAGE : ./pgm <num_centers> <input file> <output file>'
        print 'EXAMPLE : ./kmeans.py 10 garbage.csv centers.csv'
        exit(1)

    num_centers = int(sys.argv[1])
    
    locations, volumes = read_json_input(sys.argv[2])

    centroids, indexes = get_means(locations, num_centers)
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
        tmp['cluster_center'] = list(centroids[i])
        tmp['volume'] = volume_in_centers[i]
        tmp['components'] = comps[i]
        tmp['datetime'] = datetime.datetime.today()
        res.append(tmp)
        
    write_json_output(sys.argv[3], res)
