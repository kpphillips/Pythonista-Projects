'''
Test script to run and utilizes forge_api and supporting files. 
'''

import forge_api as f

user = f.getUser()
print(user.name)
print(user.email)
hubs = f.getHubs()
for h in hubs:
	print(h.name)

