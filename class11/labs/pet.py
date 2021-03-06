"""
pet.py
=====
Create a class called Pet, subclass it to create a Dog and Cat class

Pet will have a speak and speak_twice method, as well as a name attribute that is initialized in a constructor.

Example Output:
>>> p = pet.Pet("mojo")
>>> print p
mojo
>>> p.speak()
generic animal talk
>>> p.speak_twice()
generic animal talk
generic animal talk
>>> c = pet.Cat("mittens")
>>> print c
mittens
>>> c.speak_twice()
meow
meow
>>> 
"""

class Pet:
	def __init__(self, name):
		self.name = name
		self.sound = "generic animal talk"
	
	def speak(self):
		return self.sound
		
	def speak_twice(self):
		return "%s \n%s" % (self.sound, self.sound)

class Cat(Pet):
	def __init__(self,name):
		self.name = name
		self.sound = "meow"

class Dog(Pet):
	def __init__(self,name):
		self.name = name
		self.sound = "woof"