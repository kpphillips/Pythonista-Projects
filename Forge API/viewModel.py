import model

def presentUser(js):
	first=js['firstName']
	last=js['lastName']
	email=js['emailId']
	imageUrl=js['profileImages']['sizeX240']
	user=model.make_user(f'{first} {last}', email, imageUrl)		
	return user
	
def presentHubs(js):	
	data=js['data']
	list=[]
	for i in data:
		id=i['id']
		name=i['attributes']['name']
		hub=model.make_hub(name,id)
		list.append(hub)	
	return list
