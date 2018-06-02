import ctaapi as c
import json

#r=c.getTime()
#r=c.getVehicles(['77'],False)
#r=c.getVehicles(['8265'])
#r=c.getRoutes()
#r=c.getDirections('77')
#r=c.getStops('77',1)
#r=c.getPatterns('77')
r=c.getPredictions('7941',['77'])

print(json.dumps(r, indent=1))

#get bus predicted times
prds=r['bustime-response']['prd']
prd1=prds[0]
print(prd1['stpnm'])
print(prd1['rtdir'])

for prd in prds:
	print(prd['prdctdn'])


