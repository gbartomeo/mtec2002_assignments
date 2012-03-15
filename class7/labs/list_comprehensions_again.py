"""
list_comprehensions_again.py
===
1. Create two dictionaries, book1 and book2,  that contain information about a book: title, author, pages
    Dune, Frank Herbert, 500
    Frankenstein, Mary Shelley, 278
2. Iterate through each dictionary and create a list of strings with the key and value in a sentence - ex: title is Dune.
3. Use list comprehensions to do this
4. Print out the resulting lists

Example Output:
['author is Frank Herbert.', 'pages is 500.', 'title is Dune.']
['author is Mary Shelley.', 'pages is 278.', 'title is Frankenstein.']
"""

book1 = {"title": "Dune", "author": "Frank Herbert", "pages": 500}
book2 = {"title": "Frankenstein", "author": "Mary Shelley", "pages": 278}

list1 = book1.items()
list2 = book2.items()


a = 0

for k,v in list1:
	list1[a] = "%s is %s" % (k, v)
	a += 1

a = 0

for k,v in list2:
	list2[a] = "%s is %s" % (k, v)
	a += 1

	
print list1
print list2