"""
fizzbuzz.py
===
1.  Print integers 1 to 100, but replace multiples of 3 with "Fizz" and multiples of 5 with "Buzz" and multiples of both with "FizzBuzz"
joe@walsh~/projects/archived/fizzbuzz$ python fizzbuzz.py 
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
.
.
"""

integers = range(1,101)

for integer in integers:
	if (integer%3==0) and (integer%5==0):
		print "fizzbuzz"
	elif integer%3==0:
		print "fizz"
	elif integer%5==0:
		print "buzz"
	else:
		print integer