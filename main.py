import player
import shelve
import rooms

#Need to fix
#	Intro
#	Hints maeby
#	Game too short
#		Might add hide mechanic

print('''\nFinaly after all this time, after all the deception, trickery, and wrong moves you are here. 
Pharaoh Movieses tomb
In front of you stands a large stone door without any handles just a hole on the right door. 
The steps in front of the door is covered in sand.''')
	
userIn = ""
quit = ("quit", "q")
actions = ('''
	quit/q - Quit out of the game
	save/sa - saves the game
	load/l - loads last save file
	search/s - searches room for items and gets the object 
	use/u - uses iteam in inventorty
	hint/h - gives hint in room
	map/m - gives your location
''')

#This is the function to save the game
def save():
	s = shelve.open('game.bin')
	s["location"] = user.GetLocation()
	s["inventory"] = user.GetInventory()
	s["outsideStuff"] = rooms.outside
	s["mainHall"] = rooms.mainHall
	s["watingR"] = rooms.watingR
	s["dinnH"] = rooms.dinnH
	s["hiddenR"] = rooms.hiddenR
	s["obserR"] = rooms.obserR
	s["waterR"] = rooms.waterR
	s["tomb"] = rooms.tomb
	s.sync()
	s.close()

#This is the function to load the game
def load():
	s = shelve.open('game.bin')
	user.location(s["location"])
	user.SetInventorty(s["inventory"])
	rooms.outside = s["outsideStuff"]
	rooms.mainHall = s["mainHall"]
	rooms.watingR = s["watingR"]
	rooms.dinnH = s["dinnH"]
	rooms.hiddenR = s["hiddenR"]
	rooms.obserR = s["obserR"]
	rooms.waterR = s["waterR"]
	rooms.tomb = s["tomb"]
	s.close()

user = player.Player()

def EndGame():
	print(f'''After truding through the long forgotten tomb, 
you finally reach it: The Final Resting Place of Pharaoh Movieses. 
You scan the room it is by far the most wonderfully decorated room in the tomb. 
With riches pilling around the room, gold in one corner, dimonds in the next.
It was obvous that it was once a throne room, along with this tomb used to be a castel. 
Sitting on the old throne chair was the sarcofigus of Pharaoh Movieses. 
As you move closer to the sarcofoges the throuch you were holding dimmed, 
the door to the room slide shut. 
Finally you hear a voice from the sarcofogus, 'What is your quarry?' ''')
       
	print("You think to yourself, 'What do I want?'")
	quarry = input("Mabey something like money, power, knowelge, to be gone?")
	if quarry == "money":
		print('''You mange to stammer out, "Money! I want money. 
I came into this crypt to find things that would make me wealthy" 
Then there was silence, no movement, no voice.
The door behind you opened up and the toruch regained its brighness.
You were free to fully excovate the tomb bringing in money from sopsners and inverviews,
and its not like anyone missed a dimoand or two from the piles, right?''')
	elif quarry == "power":
		print('''As you fell to the floor pondering the question, you relies that
you are being asked a question by a 5 thousand year old Pharaoh. "Power," you shout back
"I want power."
"Let it be done," the sarcophogues replied, "Now you can use the 'Admin' powers
At first you did not know what he ment until you tried to do something and you could do more.
Mabey in your next life you can take full advange of it.''')
	elif quarry == "knowelge":
		print('''You stoud there shocked, what do you want? Why have you done all of this?
Then it hits you, you stand up and reply, "I want knowelge. This kingdom used to be the head 
of knowelge in its time, with many of its secrests lots when it fell. These things I want to know."
Silence fallowed you remarks, the door opened behind you and your toruch was no longer dimmed.
Just as you started to head out the wall to your right opend up. In side was a huge library full
of lost arts, history, and ideas. Amoug these books you also found information on magic, and the
rituals that seem to have let Pharaoh Movieses speak to you, something refured to 'Admin'. 

I wonder what you will do with that? ''')
	elif quarry in ("to be gone", "be gone", "gone"):
		print('''In a fit of fear you shouted the onlything you could think of, "To be home."
While shutting your eyes as hard as you can. Almost instantly you no longer feel the heat and 
humidity from being in the temple cave, but the air conditing of the 21st centry. Opeing your eyes 
you look around your surroudings, it was in fact your home. Now you are 8 thousand miles from the undead Pharaoh.
Nows the question, do you go back or forget about it?''')
	else:
		print('''A silence fills the room after your answer. This gones on for what feels like an
eternity, befor the sarcofogus replies, "Hmmmm, no." Then inexplicably you find yourself at the entrance of the tomb.''')

while userIn not in quit:
	userIn = input("What do you do?\n")
	if userIn == "help":
		print(actions)
	elif userIn in ("search", "s"):
		user.ChangeInventory(2)
	elif userIn in ("u", "use"):
		user.ChangeInventory(1)
	elif userIn == "move":
		direction = input("What direction? (N, E, S, W)\n")
		user.MovePlayer(direction)
		if user.GetLocation() == "tomb":
			userIn = "quit"
			EndGame()
	elif userIn == "map":
		print(user)
	elif userIn in ("i", "inventory"):
		a = user.PrintInventory()
		print(a)
	elif userIn == "Admin":
		cd = input("Enter command\n")
		if cd == "tp":
			goal = input("Which room?\n")
		else:
			goal = 'na'
		user.Admin(cd, goal)
	elif userIn in ('save'):
		save()
	elif userIn in ("l", "load"):
		load()
	elif userIn != 'quit':
		print("Type 'help' for list of commands")
	else:
		print("Command unknonw try again.")

