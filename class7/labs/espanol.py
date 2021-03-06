"""
espanol.py 
===
1. Write a function called to_spanish that takes a string, s, as a parameter
2. Just like the exam, translate cat and dog into spanish
3. However, instead of using a conditional, use a dictionary to store translations
4. Call the function on cat, dog, and turtle
5. Print out the original string as well as the result of the function
6. Hint: again, get might help with the default value

Example Output:
dog in spanish: perro
cat in spanish: gato
turtle in spanish: no se
"""

def to_spanish(s):
	eng_to_span = {"cat": "gato", "dog": "perro"}
	print s
	if s in eng_to_span:
		return eng_to_span[s]
	else:
		return eng_to_span.get("turtle", "no se")
