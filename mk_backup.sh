#!/usr/bin/env bash
mongodump --db cleanteam --out data/mongodumps/`date '+%FT%T'`
