#rockpaperscissors 3 Introduction to variables
#rockpaperscissors 4 Introduction to Functions
#rockpaperscissors 5 Else, Elif Statements
#rockpaperscissors 6 Rock, Paper, Scissors Game

x = 10
print(x) #print 10
y = 3
print(x/y) #print 3.3333333333333335
print(int(x/y)) #print 3
print(float(y)) #print 3.0
customer_Name = "Bob"
balance = 100.55
print(customer_Name + "'s bank balance is $" + str(balance))

def circle(radius):
	area = (radius**2) * 3.14
	return area
print(circle(10)) #print 314.0

def rectange(width, height):
	area = width * height
	print(area)
rectange(5,6) #return 30

grade = 87.5
if grade >= 89.5:
	print("The letter grade is A.")
elif grade >= 79.5:
	print("The letter grade is B.")
elif grade >= 69.5:
	print("The letter grade is C.")
elif grade >= 59.5:
	print("The letter grade is D.")
else:
	print("The letter grade is F.")

import random

def rockpaperscissors():
	computer_choice = random.randint(1,1)
	if computer_choice == 1:		
		computer_choice_rock()
	elif computer_choice == 2:
		computer_choice_paper()
	elif computer_choice == 3:
		computer_choice_scissors()
def computer_choice_rock():
	user_choice = input("1 for rock, 2 for paper, 3 for scissors: ")
	if user_choice == "1":
		print("You tie.  You chose rock and the computer chose rock.")
		try_again()
	elif user_choice == "2":
		print("You win.  You chose paper and the computer chose rock.")
		try_again()
	elif user_choice == "3":
		print("You lose.  You chose scissors and the computer chose rock.")
		try_again()
	else:
		try_again()
def computer_choice_paper():
	user_choice = input("1 for rock, 2 for paper, 3 for scissors: ")
	if user_choice == "1":
		print("You lose.  You chose rock and the computer chose paper.")
		try_again()
	elif user_choice == "2":
		print("You tie.  You chose paper and the computer chose paper.")
		try_again()
	elif user_choice == "3":
		print("You win.  You chose scissors and the computer chose paper.")
		try_again()
	else:
		try_again()
def computer_choice_scissors():
	user_choice = input("1 for rock, 2 for paper, 3 for scissors: ")
	if user_choice == "1":
		print("You win.  You chose rock and the computer chose scissors.")
		try_again()
	elif user_choice == "2":
		print("You lose.  You chose paper and the computer chose scissors.")
		try_again()
	elif user_choice == "3":
		print("You tie.  You chose scissors and the computer chose scissors.")
		try_again()
	else:
		try_again()
def try_again():
	choice = input("Would you like to play again?  y or n ")
	if choice == "y":
		rockpaperscissors()
	elif choice == "n":
		print("Thanks for playing")
		quit()
	else:
		pass
rockpaperscissors()