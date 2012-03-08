"""
equal_to_three_while.py
===
1. Create a list of strings called animals...  "dog", "zebra", "giraffe", "elephant", "cat", "lion", "bear"
2. Create an empty list called three_letter_words
3. Use a while loop to append all of the three letter words from animals to three_letter_words 
4. Print out the animals list and the three_letter_words list

Example Output:
All words: ['dog', 'zebra', 'giraffe', 'elephant', 'cat', 'lion', 'bear']
Three letter words: ['dog', 'cat']
"""

animals = ["dog", "zebra", "giraffe", "elephant", "cat", "lion", "bear"]
three_letter_words = []

animal = 0
while animal < len(animals):
	if len(animals[animal]) == 3:
		three_letter_words.append(animals[animal])
	animal += 1
		
print animals
print three_letter_words