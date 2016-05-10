#!/usr/bin/env bash

echo 'use cleanteam
db.dropDatabase()' | mongo  && \
./gen_coord.py bangalore.coord.range 100  && \
./assign_vol.py 30.5 2016-03-12 60  && \
./kmeans.py 12  && \
./initial_route.py 2 9500 4  && \
./algorithm_route.py 30 
