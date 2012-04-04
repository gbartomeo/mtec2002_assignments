"""
exceptions.py
=====
To handle errors, use a try/catch block:

-----
try:
	# do your stuff
except SomeError:
	# deal with some error
-----

optionally... you can continue catching more than one exception:

-----
.
.
except AnotherError:
	# deal with another error
-----

Substitute SomeError with the kind of error you want to handle - for example:

KeyError
ValueError
TypeError
IndexError
ZeroDivisionError
"""
#KeyError
d = {"shape": "circle"}

try:
	print d['shape'] #fine
	print d["color"] #KEY ERROR
except KeyError:
	print "That key doesn't exist!!! :( "
print "Done"


#ValueError (conversion errors)

try:
	print int("this is not a number! :D")
except ValueError:
	print "That was not a number! D:"
print "Done"

#TypeError 

try:
	print "foo" * "bar"
except TypeError:
	print "You can't multiply by that!"
print "Done"


#IndexError
myList = ["cat", "dog"]

try:
	print myList[2]
except IndexError:
	print "Yer index be outta range, yarr."
print "Done"


#ZeroDivisionError

try:
	5/0
except TypeError:
	print "The universe will implode if we try to do that again."
print "Done"


#catching multiple possible exceptions - try possible KeyError AND TypeError like dictionary value divided by another value
#ex... which player do you want to add a score to, and add that score

d = {"score": 10}
k = "score"
divisor = 2
try:
	print d[k] / divisor
except KeyError:
	print "That key doesn't exist."
except ZeroDivisionError:
	print "You can't divide by zero."