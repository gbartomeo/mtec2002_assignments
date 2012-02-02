# The integer variable people has an assigned value of 30.
people = 10
# The integer variable cars has an assigned value of 40.
cars = 80
# The integer variable buses has an assigned value of 15.
buses = 100


# If there are more cars than people
if cars > people:
    print "We should take the cars." # Will print
# Else if there should be more people than cars
elif cars < people:
    print "We should not take the cars."
# Otherwise,
else:
    print "We can't decide."

# If there are more buses than cars
if buses > cars:
    print "That's too many buses." # Will print
# Else if there should be more cars than buses
elif buses < cars:
    print "Maybe we could take the buses."
# Otherwise,
else:
    print "We still can't decide."

# If there are more people than buses
if people > buses:
    print "Alright, let's just take the buses."
# Otherwise,
else:
    print "Fine, let's stay home then." # Will print, but makes no contextual sense.
    
    
# Should the if statement prove false, the code then moves on to
# the elif statements. Should there be no elif statements or should
# the elif statements prove false, the code moves onto the else statement.