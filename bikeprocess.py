f = open('201602-citibike-tripdata.csv','r')
headers = f.readline()
print headers
j = {}
for l in f:
	dat = l.split(',')

	lat = float(dat[9].replace('\"',''))
	lon = float(dat[10].replace('\"',''))
	if len(dat[13]) <4 :
		continue
	age = int(dat[13].replace('\"',''))
	
	j[age] = [lon,lat]



data=[]
for age in j.keys():
	g = {}
	g['type'] = "Feature"
	g['properties'] = {"name": age}
	g['geometry'] = {"type": "Point","coordinates": j[age]}
	data.append(g)

import json

with open('./201602-bike-data.json', 'w') as fp:
    json.dump(data, fp)