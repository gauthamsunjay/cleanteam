#!/usr/bin/env bash

./gen_coord.py bangalore.coord.range 200 150.55 20 resources/tmpfiles/locs && ./kmeans.py 10 resources/tmpfiles/locs resources/tmpfiles/clusters && ./inital_route.py resources/tmpfiles/clusters 2 10000 3 && ./algorithm_route.py resources/tmpfiles/clusters resources/tmpfiles/initial_cluster_route resources/tmpfiles/final_routes
