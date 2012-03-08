"""
dictionary_1.py
===
1. Dictionaries are lists of key, value pairs (they're like hashes or associative arrays in other languages)
2. The keys and values are separated by colons, the key, value pairs are separated by commas
3. Dictionaries are enclosed by curly braces
4. An empty dictionary is represented by two curly braces with nothing in the middle - {}
5. The most common type of dictionary key is a string, but any immutable type (such as numerical types and tuples) can be keys too!
6. Dictionary keys are case sensitive
7. Dictionary keys are unique; you can't have duplicate keys
8. Values can be accessed by using the dictionary name followed by the key in square brackets
9. Order of the key, value pairs cannot be guaranteed!

Examples:
superstitious_things = {"lucky_charm":"horseshoe", "number" 7, "spirit_animal":squid}
superstitious_things["number"]

http://docs.python.org/library/stdtypes.html#mapping-types-dict
"""
# create an empty dictionary, set it to a variable named empty
so_empty = {}

# print out the empty dictionary
print so_empty

# create a dictionary that describes a pineapple using the keys name, type, and taste
pineapple = {"name": "pineapple", "type": "fruit", "taste": "sweet"}

# print out the dictionary 
print pineapple

# create another dictionary that describes a lemon using the keys name, type, and taste
lemon = {"name": "lemon", "type": "fruit", "taste": "sour"}

# print out the dictionary 
print lemon

# print out the value at key name
print lemon["name"]

# create a new key, color, by  using the new key and assigning it to a variable
lemon["color"] = "yellow"

# print the value at the new key
print lemon["color"]

# print the dictionary
print lemon

# create a dictionary of four of your favorite things using the keys color, food, animal, and number
my_favorites = {"color": "purple", "food": "rice pudding", "animal": "pink fairy armadillo", "number": "four"}

# print out the dictionary
print my_favorites

# print out your favorite color
print my_favorites["color"]

# print out your favorite number
print my_favorites["number"]

# print out your favorite animal
print my_favorites["animal"]

# print out your favorite animal and color in a sentence
print "Although my favorite color is %s, I *love* %s!" % (my_favorites["color"], my_favorites["animal"])

# change your favorite number
# ... but I like 4. :(
my_favorites["number"] = 3

# print out your favorite number
print my_favorites["number"]

# change your favorite animal
# ... why are you trying to change who I am! ;_;
my_favorites["animal"] = "wolf"

# print out your favorite animal
print my_favorites["animal"]

# print out your dictionary
print my_favorites

# try printing an item with a key that doesn't exist
# print my_favorites["person"]

# what happened?  comment out your previous line to continue
# KeyError: 'person'

# you can also use the get method on a dictionary to retrieve an element, but have a default value if the key doesn't exist
my_favorites.get("number")

# just like a list, you can use the del statement to delete a dictionary item
del(my_favorites["food"])

# print out the dictionary after deleting an element
print my_favorites

# get the list of keys in your dictionary using the keys method, set it to a variable named my_keys
my_keys = my_favorites.keys()

# print out the keys
print my_keys

# loop through the keys using a for loop, print out each element
for keys in my_keys:
	print keys

# get the list of values in your dictionary using the values method, set it to a variable named my_values
my_values = my_favorites.values()

# print out the values
print my_values

# loop through the values using a for loop, print out each element
for values in my_values:
	print values

# get all of the key, value pairs of your dictionary as a list of tuples using the items method; set it to a variable called tuples
tuples = my_favorites.items()

# print out this list
print tuples

# loop through the list of tuples using a for loop, print out each tuple
for stuff in tuples:
	print stuff