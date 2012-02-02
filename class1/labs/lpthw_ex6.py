# The placeholder %d is an integer, which has a value of 10.
# This makes the string variable x read as, "There are 10 types of people."
x = "There are %d types of people." % 10 # String in a string number 1
# The string variable of binary reads as, "binary"
binary = "binary"
# The string variable of do_not reads as, "don't"
do_not = "don't"
# The placeholders %s are strings, the first of which having the value of
# the variable binary, the second of the variable do_not
# making the string variable y read as, "Those who know binary and those who don't."
y = "Those who know %s and those who %s." % (binary, do_not) # String in a string number 2

# Prints the string variable x to the screen
print x
# Prints the string variable y to the screen
print y

# Prints "I said: 'There are 10 types of people'."
print "I said: %r." % x # String in a string number 3
# Prints "I also said: 'Those who know binary and those who don't.'."
print "I also said: '%s'." % y # String in a string number 4

# The boolean varible hilarious has a value of false
hilarious = False
# The string variable of joke_evaluation reads as, "Isn't that funny?! %r"
# where %r is to have a value later determined
joke_evaluation = "Isn't that joke so funny?! %r" # String in a string number 5

# Prints "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

# The string variable of w reads as "This is the left side of..."
w = "This is the left side of..."
# The string variable of e reads as "a string with a right side."
e = "a string with a right side."

# Prints "This is the left side of...a string with a right side."
print w + e # Adding the string variables w and e makes a longer string because
# you are combining the strings by adding them, just as adding two whole numbers
# makes a larger number.

# Total of 5 strings within strings