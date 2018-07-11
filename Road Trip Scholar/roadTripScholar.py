import location
import console
import wikipedia
import speech
import socket


#check for internet
#wifi_ip = socket.gethostbyname(socket.gethostname())
#print(wifi_ip)

console.clear()

location.start_updates()
currentGeoLoc = location.get_location()
location.stop_updates()

print("----> GeoLoc")
print(currentGeoLoc)
print("----> GeoLoc end")

addrList = location.reverse_geocode(currentGeoLoc)

addrDict = addrList[0]

print(addrDict.items())
print("------------")

locStr = ""
space = " "

#check and add sublocality
if 'SubLocality' in addrDict.keys():
  locStr += addrDict['SubLocality']
else:
  print("No SubLocality")

locStr += space

#check and add City
locStr += (addrDict['City']) if 'City' in addrDict else print("No 'City'")

locStr += space

#check and add state
locStr += (addrDict['State']) if 'State' in addrDict else print("No 'State'")

print("---> Search: " + locStr)
print("--------")

#search wiki based on string
search = wikipedia.search(locStr)

###TODO: check if search is empty first
#get all recomendationa
for s in search:
	print(s)

print("----> First response: " + search[0])

#get page
page = wikipedia.page(search[0])

#test
#page = wikipedia.page("illinois")
sections = page.sections

print("---> Page id: " + page.pageid)

#get page data
pageData = wikipedia.WikipediaPage(search[0])
print("Categories: ")
if not pageData.categories:
	print("No Categories")
else:
	print(pageData.categories[0])

print("----------")
#get page summary
#show other options for disambig error
try:
	localSummary = wikipedia.summary(search[0])
	print(localSummary)

except wikipedia.exceptions.DisambiguationError as e:
		print(e.options)
		
		
speech.say(localSummary)
speech.stop()
