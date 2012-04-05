from gameClasses import *
from random import *
import string
import re


room_num[0] = Room("At the gates of Mahiri.", 0,0,0, "Ominous gates made of spiked wood and iron stand fiercely infront of the city of Mahiri. A ghostly whisper caresses your ear, the faint sound of the wind through the open gates.")
room_num[1] = Room("A barren road.", 0,1,0, "Barren and without life, the wilting husks of wilted weeds flank the degenerating road. The bricks show signs of wear and tear, cracking down the middle with the concrete between nearly gone.")
room_num[2] = Room("The market at Hadjawik Njiathanda.", 0,2,0, "A tall wooden post points in four different directions, each labeled with far-past-faded text. Upon the post sits a crow, lifelike in every aspect, made of the finest rowan. Unlike the city it inhabits, it appears clean and in pristine shape. Up ahead is a tent with a figure inside, standing amongst different items, presumably all for sale.")
room_num[3] = Room("Inside a market tent.", 0,3,0, "Loads of wares, odd, beautiful, and frightening lay about. Great care has been taken in their stacking so while they slant and tilt, they do not fall. Dust has begun collecting on them, a sure sign of their unuse.")
room_num[4] = Room("In an underground cave.", 0,3,-1, "Light barely reaches into this cave, and the air within it is moist and rich with magic. The ground is littered with crystal skeletons, one hand reaching towards a pedestal.")

npc_num[0] = NPC("Aknosti the Merchant",0,3,0,"human","male","A short dark robed man stands here, hands folded across his lap.","Spectacularly short, Aknosti stands a good foot beneath you. His body is swathed in dark grey robes with a raised hood. He seems nearly consistently stoic, standing amongst his wares with an aura of pride.")

for j in range(len(Room.rooms.keys())):
    room_num[j].update()

confused = ["\nI don't understand.", "\nWhat are you trying to do?", "\nTry putting that another way."]

hp = 100
mp = 200
healthprompt = "HP: %d, MP: %d >\t" % (hp, mp)

print "Please enter your name.\n"
user.name = raw_input("> ")
print
look()

while userinput.lower() != "quit":
    userinput = raw_input(healthprompt)
    
    # Can I use regex to make the first word lowercase?
    # Should I bother?
    emotion = ""
    
    if re.search(r"^look$", userinput):
        look()
    elif re.search(r"^l$", userinput):
		look()
    elif re.search(r"^say ", userinput):
        if re.search(r"\(\w+\)", userinput[4:]):
            emotionend = userinput.index(")")
            emotion = " " + userinput[5].lower() + userinput[6:emotionend]
            emotionbuffer = 2
        else:
            emotion = ""
            emotionend = 4
            emotionbuffer = 0
        if userinput[-1] not in string.punctuation:
            print "\nYou say%s, \"%s.\"" % (emotion, userinput[emotionend+emotionbuffer:].capitalize())
        elif userinput[-2:] == "!!":
            print "\nYou exclaim%s, \"%s\"" % (emotion, userinput[emotionend+emotionbuffer:-1].capitalize())
        elif userinput[-2:] == "??":
            print "\nYou ask%s, \"%s\"" % (emotion, userinput[emotionend+emotionbuffer:-1].capitalize())
        else:
            print "\nYou say%s, \"%s\"" % (emotion, userinput[emotionend+emotionbuffer:].capitalize())
    elif userinput in Command.commands.keys():
        print Command.commands[userinput]["string"]

    elif userinput.lower() in drxns:
    	dir_try = userinput.lower()
        # print "\n***||BEFORE THE MOVE FUNCTION||***\ndir_try: %s\nuserinput: %s" % (dir_try, userinput) # testing!
        move(dir_try)
    elif userinput == "quit":
        print "\n\n\t\t\t ============\n\t\t\t|| Goodbye! ||\n\t\t\t ============\n"
    else:
        print confused[randint(0, len(confused)-1)]
