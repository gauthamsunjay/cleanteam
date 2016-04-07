#!/usr/bin/env bash

./gen_coord.py bangalore.coord.range 200 150.55 20 resources/tmpfiles/locs && ./kmeans.py 10 resources/tmpfiles/locs resources/tmpfiles/clusters
