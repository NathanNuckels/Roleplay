#/home/pi/git/roleplay/main.py

print("Shell start. Type \"Help\" for help")
while True:
	cmd=input("><>").strip().lower().split(" ")
	if cmd[0]=="exit":
		break
	elif cmd[0]=="help":
		if len(cmd)==1:
			print("List of commands:")
			print()
		if len(cmd)==2:
			pass #search for the command name and display information
	#create c <name> <type> <place>
	#example: create Clyde protogen space-station
	#create p <place-id>
	# example: create p des
	#create o <object-name> <object-id>
	elif cmd[0]=="enter" or cmd[0]=="create" or cmd[0]=="c":
		if len(cmd)==1:
			print("Too few arguments.")
		elif cmd[1]=="c" or cmd[1]=="caracter" or cmd[1]=="character":
			if len(cmd)>5:
				print("Too few arguments.")
			elif roleplay.isType(cmd[3]):
				#Caracter(name, type, place)
				caracters.append(roleplay.Caracter(cmd[2],cmd[3],cmd[4])
			else:
				print("Invalid type. Try \"list types\"")
print("Shell stopped.")
