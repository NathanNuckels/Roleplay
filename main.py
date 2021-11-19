#/home/pi/git/roleplay/main.py
import roleplay
caracters=[]
places=[]
objects=[]

print("Shell start. Type \"Help\" for help")
while True:
	cmd=input("><>").strip().lower().split(" ")
	if cmd[0]=="exit":
		break
	elif cmd[0]=="help":
		if len(cmd)==1:
			print("List of commands:")
			print("exit, help, create, move")
		if len(cmd)==2:
			pass #search for the command name and display information
	#create c <name> <type> <place>
	#example: create Clyde protogen space-station
	#create p <place-id>
	# example: create p des
	#create o <object-id> [name]
	elif cmd[0]=="enter" or cmd[0]=="create" or cmd[0]=="c":
		if len(cmd)==1:
			print("Too few arguments.")
		elif cmd[1]=="c" or cmd[1]=="caracter" or cmd[1]=="character":
			if len(cmd)<5:
				print("Too few arguments.")
			elif roleplay.isType(cmd[3]):
				foundPlace=False
				for place in places:
					if place.name==cmd[4]:
						caracters.append(roleplay.Character(cmd[2],cmd[3],cmd[4]))
						print("Created "+cmd[2].upper()+" the "+cmd[3].uppr()+" at "+cmd[4].uper())
						foundPlace=True
				if not foundPlace:
					print("Place not found")
			else:
				print("Invalid type. Try \"list type-ids\"")
		elif cmd[1]=="p" or cmd[1]=="place":
			if len(cmd)<3:
				print("Too few arguments.")
			elif roleplay.isPlace(cmd[2]):
				places.append(roleplay.Place(cmd[2]))
				print("Loaded Place "+cmd[2].upper())
			else:
				print("Invalid place-id. Try \"list place-ids\"")
		elif cmd[1]=="o" or cmd[1]=="object":
			if len(cmd)<3:
				print("Too few arguments.")
			elif roleplay.isObject(cmd[2]):
				if len(cmd)==3:
					objects.append([cmd[2],roleplay.Object(cmd[2])])
				else:
					objects.append([cmd[3],roleplay.Object(cmd[2])])
	elif cmd[0]=="move" or cmd[0]=="mv":
		if len(cmd)<3:
			print("Too few arguments.")
		else:
			foundCaracter=False
			foundPlace=False
			for caracter in caracters:
				if caracter.name==cmd[1]:
					foundCaracter=True
					for place in places:
						if place.name==cmd[2]:
							foundPlace=True
							caracter.place=place
			if not foundCaracter:
				print("Character not found")
			elif not foundPlace:
				print("Place not found.")
			else:
				print("Moved "+cmd[1]+" to "+cmd[2])
print("Shell stopped.")
