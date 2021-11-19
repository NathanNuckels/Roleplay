#/home/pi/git/roleplay/main.py
import roleplay
import os
caracters=[]
places=[]
objects=[]
logs=[]
print("Quit anytime by closeing the window its running in or press Ctrl+C\n")
print("Please enter a log file")
while True:
	logfile=input("><> ")
	if not os.path.exists(logfile):
		print("TEKNIQ: Ready to create a new file.")
		break
	else:
		print("TEKNIQ: Hey Hey! This file already exists. If you keep going, you will just append to the existing file. Just letting you know.")
		break

def log(string):
	global logs
	logs.append(string+"\n")

print("Shell start. Type \"Help\" for help")
while True:
	cmd=input("><>").strip().lower().split(" ")
	if cmd[0]=="exit":
		break
	elif cmd[0]=="help":
		if len(cmd)==1:
			print("List of commands:")
			print("exit, help, create, move, hold")
			print("exit\nhelp\ncreate c <name> <type> <place>\ncreate p <place>\ncreate o <object> [nickname]\nmove <character> <place>\nhold <character> [held-item] [hand]\ndrop <character> <hand>")
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
						print("Created "+cmd[2].upper()+" the "+cmd[3].upper()+" at "+cmd[4].upper())
						log("Created a "+cmd[3].upper()+" named "+cmd[2].upper()+" at "+cmd[4].upper())
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
				log("Created place "+cmd[2].upper())
			else:
				print("Invalid place-id. Try \"list place-ids\"")
		elif cmd[1]=="o" or cmd[1]=="object":
			if len(cmd)<3:
				print("Too few arguments.")
			elif roleplay.isObject(cmd[2]):
				if len(cmd)==3:
					objects.append([cmd[2],roleplay.Object(cmd[2])])
					print("Created a "+cmd[2])
					log("Created a "+cmd[2].upper())
				else:
					objects.append([cmd[3],roleplay.Object(cmd[2])])
					print("Created a "+cmd[2].upper()+" nicknamed "+cmd[3].upper())
					log("Created a "+cmd[2].upper()+" nicknamed "+cmd[3].upper())
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
				log("Moved "+cmd[1]+" to "+cmd[2])
				
	elif cmd[0]=="list" or cmd[0]=="l":
		if len(cmd)==1:
			print("List what?")
		elif cmd[1]=="type-ids":
			for type in roleplay.types:
				print(type)
		elif cmd[1]=="place-ids":
			for place in roleplay.places:
				print(place)
		elif cmd[1]=="places" or cmd[1]=="p":
			if len(places)==0:
				print("There are no places")
			else:
				for place in places:
					print(place.name)
		elif cmd[1]=="characters" or cmd[1]=="c":
			if len(caracters)==0:
				print("There are no characters.")
			else:
				for caracter in caracters:
					print(caracter.name)
		elif cmd[1]=="objects" or cmd[1]=="o":
			if len(objects)==0:
				print("There are no objects")
			else:
				for objeect in objects:
					print(objeect[0])
		else:
			print("Invalid list.")
	elif cmd[0]=="hold":
		if len(cmd)==1:
			print("Not enough arguments")
		elif len(cmd)==2:
			found=False
			for character in caracters:
				if character.name==cmd[1]:
					found=True
					print("Left:"+character.helditem[0])
					print("Right:"+character.helditem[1])
			if not found:
				print("Character not found")
		elif len(cmd)==3:
			found=False
			for character in caracters:
				if character.name==cmd[2]:
					found=True
					if character.helditem[1]=="":
						character.helditem[1]=cmd[3]
						print("Set held item. (right hand)")
						log("Gave "+character.name.upper()+" a "+cmd[3]+" in their right hand")
					elif character.helditem[0]=="":
						character.helditem[0]=cmd[3]
						print("Set held item. (left hand)")
						log("Gave "+character.name.upper()+" a "+cmd[3]+" in their left hand")
					else:
						print("Character has no hands free. use the drop command.")
			if not found:
				print("Character not found")
		elif len(cmd)==4:
			found=False
			for character in caracters:
				if character.name==cmd[2]:
					found=True
					if cmd[4]=="left" or cmd[4]=="l":
						if character.helditem[0]=="":
							character.helditem[0]=cmd[3]
							print("Done.")
							log("Gave "+character.name.upper()+" a "+cmd[3]+" in their left hand")
						else:
							print("Hand full.")
					if cmd[4]=="right" or cmd[4]=="r":
						if character.helditem[1]=="":
							character.helditem[1]=cmd[3]
							print("Done.")
							log("Gave "+character.name.upper()+" a "+cmd[3]+" in their right hand")
						else:
							print("Hand full.")
			if not found:
				print("Character not found")

print("Shell stopped.")
print("Saveing..")
with open(logfile,"w+") as f:
	f.writelines(logs)
print("done!")