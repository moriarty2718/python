#Import Random to get random.choice function
import random

#line break and variables
br = " "

loose = 0
win = 0
#Nice Message - Very Cool
print("Welcome to Monty Hall Probability Finder!")
print(br)

#Ask for number of times input
duration = input("No. of times to simulate the game?: ")
duration = int(duration)
print(br)
print("Choose to switch doors or stay after revealing a wrong door")
print(br)
action = input("switch/stay: ")
print(br)

for i in range(duration):
	#Assigning Values behind doors
	#Used Goat 2 times, in door1 so the chance of getting car is 1/3
	door1 = random.choice(["Goat", "Goat", "Car"])

	#If door1 is Car, assign Goat to rest
	if door1=="Car":
		door2 = "Goat"
		door3 = "Goat"
	else:
		#Used Goat and Car just once, so probability is 1/2. Hence Overall Probability is 1/3
		door2 = random.choice(["Goat", "Car"])

		#More if
		if door2=="Car":
			door3 = "Goat"
		else:
			door3 = "Car"

	#Now choose a door randomly
	chosen_door = random.choice(["door1st","door2nd","door3rd"])

	if chosen_door=="door1st":
		if door1=="Car":
			#they win if stay, loose on switch
			if action=="switch":
				loose+=1
			elif action=="stay":
				win+=1
		else:
			if door2=="Goat":
				#open door2
				if action=="switch":
					win+=1
				elif action=="stay":
					loose+=1

			else:
				#open door3
				if action=="switch":
					win+=1
				elif action=="stay":
					loose+=1

	elif chosen_door=="door2nd":
		if door2=="Car":
			#they win if stay, loose on switch
			if action=="switch":
				loose+=1
			elif action=="stay":
				win+=1
		else:
			if door1=="Goat":
				#open door1
				if action=="switch":
					win+=1
				elif action=="stay":
					loose+=1

			else:
				#open door3
				if action=="switch":
					win+=1
				elif action=="stay":
					loose+=1
	elif chosen_door=="door3rd":
		if door3=="Car":
			#they win if stay, loose on switch
			if action=="switch":
				loose+=1
			elif action=="stay":
				win+=1
		else:
			if door1=="Goat":
				#open door1
				if action=="switch":
					win+=1
				elif action=="stay":
					loose+=1

			else:
				#open door2
				if action=="switch":
					win+=1
				elif action=="stay":
					loose+=1


#Finally print stats
print("Total: "+str(duration))
print("Won: "+str(win))
print("Lost: "+str(loose))

input("end")