
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
    
# raw_input takes input from the user, converts it to a string,
# and displays it directly after the last string
# without creating a new line.

yes = {"y", "yes", "Y", "YES", "Yes", "I am awesome", "I'm awesome", "im awesome", "i'm awesome", "yep", "yup", "yea", "yeah"}
print "Are you awesome?"
answer = raw_input()
if answer in yes:
  print "You're right, you are awesome!"
else:
  print "You suck."