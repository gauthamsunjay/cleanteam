#!/usr/bin/env bash

./gen_coord.py bangalore.coord.range 200 150.55 20 resources/tmpfiles/locs  && \
./kmeans.py 10 resources/tmpfiles/locs resources/tmpfiles/clusters  && \
./initial_route.py resources/tmpfiles/clusters 2 10000 4 resources/tmpfiles/initial_route  && \
./algorithm_route.py resources/tmpfiles/clusters resources/tmpfiles/initial_route 30 resources/tmpfiles/final_route 
