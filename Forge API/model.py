#User Class
class User(object):	
	def __init__(self, name, email, imgUrl):
		self.name = name
		self.email = email
		self.imgUrl = imgUrl
		
def make_user(name, email, imgUrl):
	user = User(name, email, imgUrl)
	return user
	
#Hub Class
class Hub(object):
	def __init__(self, name, id):
		self.name = name
		self.id = id
		
def make_hub(name, id):
	hub = Hub(name, id)
	return hub
