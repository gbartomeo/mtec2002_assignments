"""
tuples.py
===
1. Tuples are lists that cannot be changed
2. Just like lists they are comma separated values
3. However, instead of square brackets, tuples are enclosed by parentheses
4. This means that:
	a. Elements can be accessed like regular lists (0 based start index, using brackets to index into an element)
	b. However, you can't assign any new values
	c. They don't have an append or extend method
	d. They don't have a remove method
	e. They don't have an index method

Examples:
(3, 7)
("hello", "how", "are", "you")

Where you've seen them before / why would you use one:
1. When creating constant set of values - for example, one could represent the origin of a two dimensional plane as: origin = (0, 0)
2. When you need to make sure your set of values cannot be changed or overridden
3. In string formatting/string interpolation
"""
# create a tuple with 2 strings
cute_tuple = ("not so", "cute")

# print out the tuple
print cute_tuple

# define a tuple with 5 numbers
numbery_tuple = (0,1,2,3,4)

# print out the tuple
print numbery_tuple

# print out the 2nd element in the tuple
print numbery_tuple[2]

# try to change the value of the second element
#numbery_tuple[2] = 3

# what happened?  comment out the line you just wrote to continue....
# TypeError: 'tuple' object does not support item assignment

# try using append() on a tuple to add another element
# numbery_tuple.append(9)

# what happened?  comment out the line you just wrote to continue....
# AttributeError: 'tuple' object has no attribute 'append'

# let's compare to lists: try creating a list and changing a value, it should work
listy_list = ["moo", "moon", "whee"]
listy_list[2] = "moony"

# try appending an element to a list
listy_list.append("luna")

# try using the tuple you created above in string formatting
print "This tuple is used in string formatting: %s" % (cute_tuple,)

# let's do another... without using a variable
print "This is another tuple with a value of %s!" % (tuple("cows"),)

# tuples can also be items in a list!
random_list = [cute_tuple, numbery_tuple]

# let's iterate through them
list_index = 0
while list_index < len(random_list):
	print random_list[list_index]
	list_index += 1