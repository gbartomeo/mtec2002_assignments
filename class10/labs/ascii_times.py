"""
ascii_times.py
=====
1. create a dictionary of ascii art - {"heart":"<3", "person":">-|o"}
2. loop forever
3. ask for a key
4. ask for the number of times the ascii art should be printed
5. print out the ascii art that number of times
6. what happens if we input a non-numeric value for number of times
7. what happens if we input a key that doesn't exist?
"""

d = {"heart": "<3", "turtle": ":\":", "kirby": "(/)'.')/)"}
user_input = ""
while user_input.lower() != "quit":
	try:
		user_input = raw_input("Gimme a key.\n> ").lower()
		d[user_input]
		try:
			num = int(raw_input("How many times we showin' it?\n> "))
			print d[user_input] * num
		except ValueError:
			print "That's not a number. Back to square one."
	except KeyError:
		print "I don't know how to draw that."
	user_input = raw_input("Quit or another ascii art?\n> ")