"""
loops_lists_review.py

1. Create a list of numbers
2. Append a number to that list of numbers
3. Get the length of the list
4. Loop through the list and return the number minus 1
"""

numbers = range(10)

numbers.append(10)

print "There are %d numbers stored in this list!" % len(numbers)

"""
i = 0
while i < len(numbers):
	print numbers[i]-1
	i += 1
	
"""

for number in numbers:
	print number - 1