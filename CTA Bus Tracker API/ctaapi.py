#imports
import ctakey
import requests
import json

#CTA API Docs
print('https://www.transitchicago.com/assets/1/6/cta_Bus_Tracker_API_Developer_Guide_and_Documentation_20160929.pdf' + '\n')

#Constants
baseUrl='http://www.ctabustracker.com/bustime/api/v2/'
apiKey=ctakey.apiKey

#request
def request(url):
	r=requests.get(url)
	parsed_json = json.loads(r.content)
	print('\nIt Worked!, Have a 🍺\n')
	return parsed_json

#Time
def getTime():
	apiCall='gettime'
	url= baseUrl + apiCall + '?key=' + apiKey + '&format=json'
	return request(url)

#Vehicles
def getVehicles(vids_or_rts,vids=True):
	apiCall='getvehicles'
	query=''
	if vids:
		query += '&vid='
		for vid in vids_or_rts:
			query += vid + ','
	else:
		query += '&rt='
		for rt in vids_or_rts:
			query += rt + ','
			
	url= baseUrl + apiCall + '?key=' + apiKey + query +'&format=json'
	return request(url)
	
#Routes
def getRoutes():
	apiCall='getroutes'
	url= baseUrl + apiCall + '?key=' + apiKey + '&format=json'
	return request(url)

#Route Directions
def getDirections(rt):
	apiCall='getdirections'
	query = '&rt=' + rt
	url= baseUrl + apiCall + '?key=' + apiKey + query +'&format=json'
	return request(url)

#Stops
def getStops(rt,dir):
	dirs_json=getDirections(rt)
	dirs=dirs_json['bustime-response']['directions']
	direction=dirs[dir]['dir']
	apiCall='getstops'
	query1 = '&rt=' + rt
	query2 = '&dir=' + direction
	print(direction)
	
	url= baseUrl + apiCall + '?key=' + apiKey + query1 + query2 +'&format=json'
	return request(url)

#Patterns
def getPatterns(rt_or_pids,rt=True):
	apiCall='getpatterns'
	query=''
	if rt:
		query += '&rt=' + rt_or_pids
	else:
		query += '&pid='
		for pid in rt_or_pids:
			query += pid + ','
	
	url= baseUrl + apiCall + '?key=' + apiKey + query +'&format=json'
	return request(url)
											
#Predictions
def getPredictions(vids_or_stpids,rts,stpids=True,top=4):
	apiCall='getpredictions'
	query=''
	if stpids:
		query += '&rt='
		for rt in rts:
			query += rt + ','
		query += '&stpid=' + vids_or_stpids	
	else:
		query += '&pvid='
		for vid in vids_or_stpids:
			query += vid + ','
	
	url= baseUrl + apiCall + '?key=' + apiKey + query +'&format=json'
	return request(url)

#Service bullitins
#http://www.transitchicago.com/developers

#Error Codes
