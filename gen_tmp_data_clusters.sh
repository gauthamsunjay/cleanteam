#!/usr/bin/env bash

./gen_coord.py bangalore.coord.range 100 150.55 20 resources/tmpfiles/locs && ./kmeans.py 10 resources/tmpfiles/locs resources/tmpfiles/clusters
