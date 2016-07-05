from hashlib import *
inventory = {
			
			}
answer = input("enter 1 to login or 0 to exit. ")
if answer == "1":
	username = input ("Enter your username. ")
	password = input("Enter your password. ")
	print("You're not signed up. Sign up to continue.")
	username = input ("Enter a username. ")
	password = input ("Enter a new password. ")
	securityquestion = input("What's your spirit animal? ")
	sha256(password.encode("utf-8")).hexdigest() 
	inventory [username]= password
	print("Now you can login!")
	newusername = input("Enter your username. ")
	newpassword = input("Enter your password. ")
	if newusername == username and newpassword == password :
		print("Congrats you're in!")
	else:
		print ("Your username or password is incorrect.")
		securityAnswer = input ("Did you forget your password? ")
		if securityAnswer == "yes":
			spirit = input("What's your spirit animal?")
			if spirit == securityquestion:
				print ("your password is " + password)
				newusername = input("Enter your username. ")
				newpassword = input("Enter your password. ")
				if newusername == username and newpassword == password :
					print("Congrats you're in!")
				
			else:
				print ("Sorry thats invalid.System disabled.")
		else:
			newusername2 = input("Enter your username. ")
			newpassword2 = input("Enter your password. ")
			if newusername2 == username and newpassword2 == password :
				print("Congrats you're in!")
		
			
			
		
if answer == "0":
	exit()