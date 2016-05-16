#!/usr/bin/env bash

echo 'use cleanteam
db.clusters.drop()' | mongo  && \
echo 'use cleanteam
db.initial_route.drop()' | mongo  && \
echo 'use cleanteam
db.final_route.drop()' | mongo  && \
./kmeans.py 4  && \
./initial_route.py 1 100000 3  && \
./algorithm_route.py 30 
