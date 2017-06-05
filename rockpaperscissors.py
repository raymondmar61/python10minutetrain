#import Random
import random

#Define function computer choice random
def rockpaperscissors():
	computer_choice = random.randint(1,3) #random.randint Python returns random integer (low range, high range)
	if computer_choice == 1:
		computer_choice_rock()
	elif computer_choice == 2:
		computer_choice_paper()
	else:
		computer_choice_scissors()

#Define	function rock
def computer_choice_rock():
	user_choice = raw_input("1 for rock, 2 for paper, 3 for scissors: ") #raw_input is string, not an integer
	if user_choice == "1":
		print("You tie.  You chose rock and the computer chose rock")
		try_again()
	elif user_choice == "2":
		print("You win.  You chose paper and the computer chose rock")
		try_again()
	elif user_choice == "3":
		print("You lost.  You chose scissors and the computer chose rock")
		try_again()
	else:
		print("Try again")
		computer_choice_rock()

#Define	function paper
def computer_choice_paper():
	user_choice = raw_input("1 for rock, 2 for paper, 3 for scissors: ") #raw_input is string, not an integer
	if user_choice == "1":
		print("You lost.  You chose rock and the computer chose paper")
		try_again()
	elif user_choice == "2":
		print("You tie.  You chose paper and the computer chose paper")
		try_again()
	elif user_choice == "3":
		print("You win.  You chose scissors and the computer chose paper")
		try_again()
	else:
		print("Try again")
		computer_choice_paper()
	
#Define	function scissors
def computer_choice_scissors():
	user_choice = raw_input("1 for rock, 2 for paper, 3 for scissors: ") #raw_input is string, not an integer
	if user_choice == "1":
		print("You win.  You chose rock and the computer chose scissors")
		try_again()
	elif user_choice == "2":
		print("You lost.  You chose paper and the computer chose scissors")
		try_again()
	elif user_choice == "3":
		print("You tie.  You chose scissors and the computer chose scissors")
		try_again()
	else:
		print("Try again")
		computer_choice_scissors()
	
#Define function try again
def try_again():
	choice = raw_input("Would you like to play again? y/n ")
	if choice == "y" or choice =="Y" or choice =="yes" or choice =="Yes":
		rockpaperscissors()
	elif choice == "n" or choice =="N" or choice =="no" or choice =="No":
		print("Thanks for playing")
		quit()
	else:
		print("Try again")
		try_again()

#call the function to begin the program, duh
rockpaperscissors()
