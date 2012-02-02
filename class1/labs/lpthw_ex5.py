name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches, or %d cm, tall!" % (height, height*2.54)
print "He's %d pounds, or %d kilos, heavy." % (weight, weight/2.2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
print "However, in metric, if you add %d, %d, and %d I get %d." %(
  age, height*2.54, weight/2.2, age+height*2.54+weight/2.2)


# Removed all the "my_". Added metric measurements.