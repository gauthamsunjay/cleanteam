#!/usr/bin/env bash

./gen_coord.py bangalore.coord.range 100 resources/tmpfiles/co_ords  && \
./assign_vol.py resources/tmpfiles/co_ords 30.5 20 resources/tmpfiles/locs  && \
./kmeans.py 15 resources/tmpfiles/locs resources/tmpfiles/clusters  && \
./initial_route.py resources/tmpfiles/clusters 2 23000 4 resources/tmpfiles/initial_route  && \
./algorithm_route.py resources/tmpfiles/clusters resources/tmpfiles/initial_route 30 resources/tmpfiles/final_route 
