"""
loop_dictionary.py
===
1. Create two dictionaries, book1 and book2,  that contain information about a book: title, author, pages
	Dune, Frank Herbert, 500
	Frankenstein, Mary Shelley, 278
2. Iterate through each dictionary and print out both the key and value in a sentence - ex: title is Dune.
3. Put the dictionaries in a list called list of books
4. Iterate over the list and print each dictionary

Example Output:
author is Frank Herbert
pages is 500
title is Dune
author is Mary Shelley.
pages is 278.
title is Frankenstein.
{'author': 'Frank Herbert', 'pages': 500, 'title': 'Dune'}
{'author': 'Mary Shelley', 'pages': 278, 'title': 'Frankenstein'}
"""

book1 = {"title": "Dune", "author": "Frank Herbert", "pages": "500"}
book2 = {"title": "Frankenstein", "author": "Mary Shelley", "pages": "278"}

keys = book1.keys()
values = book1.values()
values += book2.values()

whileindex = 0
bookinfo = 0
while (whileindex < len(values)):  # for k,v in dictionary.items() :DDDD
	print "%s is %s" % (keys[bookinfo], values[whileindex])
	bookinfo += 1
	whileindex += 1
	if bookinfo > 3:
		bookinfo = 0