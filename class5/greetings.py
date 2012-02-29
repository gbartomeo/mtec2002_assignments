"""
greetings.py
=====
Write the following program:
1. Create a list of names and assign to a variable called names
2. Append another name to this list using append
3. Print out the length of this list
4. Loop through each item of this list and print out the name with a greeting, like "hello", appended before it

For example...

Hello Dave
Hello Sue
Hello James
"""

names = ["Mary", "Jane", "Marth", "Jacob", "Dave", "Sue", "James"]

names.append("Kiara")

print "There are %d names in this list!" % len(names)

i = 0
while i < len(names):
	print "Hello %s!" % names[i]
	i += 1