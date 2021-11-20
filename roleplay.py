types=["protogen"]
places=["space-station","des"]
objects=["sword","gem"]

def isType(type):
	for validType in types:
		if type==validType:
			return True
	return False

def isPlace(place):
	for validPlace in places:
		if place==validPlace:
			return True
	return False

def isObject(object):
	for validObject in objects:
		if object==validObject:
			return True
	return False

class Place:
	def __init__(self,name):
		self.name=name


class Character:
	def __init__(self,name,type,place):
		self.name=name
		self.place=place
		self.type=type
		self.helditem=["",""]

class Object:
	def __init__(self,id):
		self.id=id