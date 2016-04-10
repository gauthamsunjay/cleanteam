#!/usr/bin/env python2

import random
import datetime
import json

def read_json_file(json_file) :
    f = open(json_file)
    w = f.read()
    f.close()
    return json.loads(w)

def write_json_file(json_file, pyobj) :
    f = open(json_file, 'w')
    f.write(json.dumps(pyobj, default=json_serial))
    f.close()

def json_serial(obj) :
    if isinstance(obj, datetime.datetime) :
        serial = obj.isoformat()
        return serial
    raise TypeError("Type not serializable")

# return list of co_ords : [ [cx1,cy1], [cx2,cy2] ]
def gen_rand_co_ords(co_ord1, co_ord2, n_gen) :
    '''
        co_ord1 is the upper left corner
        co_ord2 is the bottom right corner
    '''
    range_x = (co_ord1[0], co_ord2[0]) if co_ord1[0] < co_ord2[0]  else (co_ord2[0], co_ord1[0])
    range_y = (co_ord1[1], co_ord2[1]) if co_ord1[1] < co_ord2[1]  else (co_ord2[1], co_ord1[1])

    new_co_ords = []
    for i in range(n_gen) :
        new_co_ord_x = random.uniform(range_x[0], range_x[1])
        new_co_ord_y = random.uniform(range_y[0], range_y[1])
        new_co_ord = [new_co_ord_x, new_co_ord_y]
        new_co_ords.append(new_co_ord)

    return new_co_ords

# returns list of volumes b/w 1 and max_val : [ 1.123, 2.00, 3.123, max_val]
def gen_rand_vols(n_gen, max_val) :
    '''
        generate floats b/w 1 and max_val.
    '''
    vols = []
    for i in range(n_gen) :
        vols.append(random.uniform(1, max_val))

    return vols

def gen_rand_dates(n_gen, max_date, max_days_before) :
    dates = []
    for i in range(n_gen) :
        rand = random.randrange(0, max_days_before + 1)
        tmp = max_date - datetime.timedelta(days=rand)
        dates.append(tmp)

    return dates

# Not Used anymore !
# adds attr to list of lists ie. list1
# list1 : [ [1,2], [3,4] ]
# attr_list : [10, 11]
# return : [ [1,2,10], [3,4,11] ]
def add_attr(list1, attr_list) :
    new_list = []
    for i in range(len(list1)) :
        tmp = list1[i]
        tmp.append(attr_list[i])
        new_list.append(tmp)

    return new_list


if __name__ == '__main__' :
    print "Does Nothing. Only Import"
