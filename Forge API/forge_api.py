'''
Calls to api endpoints formatted lists of data to display in a UI

Currently this script uses the viewmodel script to extract only relevant info to display.
'''

import forge_endpoints as c
import requests
import json
import model as m
import viewModel as vm
from PIL import Image

def commonGetRequest(endpoint, state):
	headers = c.GETheaders
	r = requests.request("GET", endpoint, headers=headers)
								
	if (r.status_code == requests.codes.ok):
		dict = json.loads(r.content)			
		return dict
	else:
		print(r.status_code)
		print(r.text)
		print('————————')
		print('Try running "forge_auth.py" and log in, Broshkee/Broski')
		print('————————')
		return 
		
#OAUTH				
def getUser():
	print('Getting User Info...💁🏻‍♀️')
	r=commonGetRequest(c.userEndpoint, 'User')
	u = vm.presentUser(r)
	imageResponse = requests.get(u.imgUrl, stream=True)
	im = Image.open(imageResponse.raw)
	im.show()	
	return u

#Data Managment API
def getHubs():
	print('\n')
	print('Getting User Hubs...🧸')
	r=commonGetRequest(c.hubEndpoint, 'Hubs')
	h=vm.presentHubs(r)
	return h

def getProjects(hub_id):
	url=c.projectsEndpoint(hub_id)
	js=commonGetRequest(url, 'Projects')
	pass
