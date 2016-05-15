import json
import pprint
import hashlib
import os.path
import requests

from google_maps_config import *

def GetMat(co_ords) :
    locations = '|'.join([','.join([str(latlng) for latlng in co_ord]) for co_ord in co_ords])

    sha = hashlib.sha1(locations).hexdigest()
    fpath = os.path.join('data', 'mats', sha)
    iscached = os.path.isfile(fpath)

    if iscached :
        print 'getting from cache'
        f = open(fpath)
        w = f.read()
        f.close()

        mat = eval(w)
    
    else : # retreive from google maps web service
        payload = {
            'origins' : locations,
            'destinations' : locations,
            'departure_time' : 'now',
            'traffic_model' : GOOGLE_MAPS_TRAFFIC_MODEL,
            'key' : GOOGLE_MAPS_API_KEY,
        }

        resp = requests.get(GOOGLE_MAPS_DIST_MATRIX_URL, params=payload)
        
        json_resp = resp.json()
        mat = []
        for row in json_resp['rows'] :
            tmp = []
            for element in row['elements'] :
                cell = {}
                cell['distance'] = element['distance']['value']
                cell['time'] = element['duration_in_traffic']['value']
                tmp.append(cell['time'])

            mat.append(tmp)
            
        f = open(fpath, 'w')
        f.write(str(mat))
        f.close()
    
    return mat
