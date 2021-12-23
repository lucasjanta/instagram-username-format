with open('original.txt') as f:
	contents = f.read()
	users = contents.split()

file = open("users.txt", "w")
for user in users:
	file.write(("'") + ("@") + user + ("',\n")) #remove \n to put all usernames in the same line
file.close()

