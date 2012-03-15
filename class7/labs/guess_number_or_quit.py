"""
guess_number_or_quit.py
===
Revisit the guess number exercise from class 2.  Write a program that stores a secret number in a variable and asks the user to guess the secret number.  

* Create a variable named secret_number; set it equal to some number...
* Create a while loop that will loop forever.
* In the while loop...
* Ask the user to enter a number; store it in a variable named user_input.  
* If the number entered is the same as the secret number, print out "You got it!".  
* If the number entered is not equal to the secret number, print out "Nope.  Try again.", and continue asking the user to enter another number.
* If the user enters the word "quit", the program will exit.

Hints:

* Use the exit() function to stop the execution of your program
* Remember to use the int() to convert user input into a number.

Example Output 1:

Guess the number I'm thinking of...
> 10
Nope, try again
Guess the number I'm thinking of...
> 21
You got it

Example Output 2:

Guess the number I'm thinking of...
> quit
Bye!
"""

from random import *

secret_number = randint(1,20)
print "A secret number has been chosen!"
while True:
	user_input = raw_input("Guess the secret number!\n> ")
	if user_input.lower() == "quit":
		print "Goodbye!"
		break
	elif int(user_input) == secret_number:
		print "You got it!"
	else:
		print "Nope. Try again."
exit()