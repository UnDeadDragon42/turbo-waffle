import intoSeqence
import userActions
#def main():
#print("HERE WE ARE")
intoSeqence.main()

userIn = input("What do you do?\n")

if userIn == "help":
	userActions.printActions()
else:
	print("Type 'help' for list of commands")