# Changing these initial variables will ultimately change what is printed
# by the program, should the values not be numerically scaled.
people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."
    
if people <> dogs:
    print "People are NOT dogs."
    
# The "if" code makes the next block of indented code what actions will be performed
# should the conditional prove to be true.

# If the code is not indented, it produces an error, as four spaces is a tab which
# python recognizes as the beginning of a block, and python is whitespace significant.