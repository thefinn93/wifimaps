#!/usr/bin/env python


ignored_properties = ["lat", "lon", "heading", "fix"]

import sys
import json
from bs4 import BeautifulSoup


print "Parsing data..."
soup = BeautifulSoup(open(sys.argv[1]).read())

outdata = {"type": "FeatureCollection", "features": []}
points = soup.find_all("gps-point")
i = 0
print "Converting..."
for data in points:
    properties = {}
    for property in data.attrs:
        if not property in ignored_properties:
            properties[property] = data.attrs[property]
    point = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [data['lat'], data['lon']]
            },
        "properties": properties
    }
    outdata['features'].append(point)
    
    percent = (i/len(points))*100
    print str(percent) + "% done"
    i += 1

out = open(sys.argv[1].replace("gpsxml", "geo.json"), "w")
out.write(json.dumps(outdata, sort_keys=True, indent=4, separators=(',', ': ')))
out.close()
