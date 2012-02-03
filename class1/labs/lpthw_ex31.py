import random

print "You enter a dark room with three doors.  Do you go through door #1, #2, or #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "3":
    print "You hesitantly open the third door."
    print "The room is dark, but illuminated in the corner of one end of the room is a \npile of golden coins and overflowing treasure chests."
    print "1. Go for the treasure."
    print "2. Leave the room."
    print "3. Flip a coin before making a decision."
    
    treasure = raw_input("> ")
    
    if treasure == "1":
        print "Of course you're going for that treasure!"
        print "You eagerly move to run across the room, only to discover the floor beneath you\n has ceased to exist. You fall down an endless pit."
    elif treasure == "2":
        print "You decide that there must be a catch."
        print "As you turn to leave the room, the door is slammed in your face. You hear the \ndoor click as it is locked from the outside."
        print "1. Go for the treasure."
        
        treasure2 = raw_input("> ")
        
        if treasure2 == "1":
            print "Being locked in the room with the treasure, you decide you will enjoy your \nconsolation prize."
            print "You begin to walk across the room, only to discover the floor beneath you has \nceased to exist. You fall down an endless pit."
        else:
            print "While you consider trying that option, you realize your only true option is \nto enjoy your consolation prize."
            print "You begin to walk across the room, only to discover the floor beneath you has \nceased to exist. You fall down an endless pit."
    else:
        print "You have no clue. Time to flip a coin!"
        print "Call it, which side says you go!"
        print "1. Heads."
        print "2. Tails."
        
        heads = {"One", "one", "1", "heads", "HEADS"}
        tails = {"Two", "two", "2", "tails", "TAILS"}
        coinflip1 = raw_input("> ")
        coinflip2 = random.randint(1,3)
        
        if coinflip1 in heads:
            print "You scream out, 'Heads!'"
            coinflip1 = 1
            print "You watch the coin twirl mid-air before it plummets achingly slowly to the \nground."
            print "It clangs annoyingly and you slowly lean over..."
            if coinflip1 == coinflip2:
                print "It's heads."
                print "You begin to walk across the room, only to discover the floor beneath you has \nceased to exist. You fall down an endless pit."
            elif coinflip2 == 3:
                print "The coin seems to suddenly fall off the edge of something. There's no floor \nahead of you."
                print "What now?"
                print "1. Wait."
                print "2. Throw yourself into the pit."
                decisions = raw_input("> ")
                if decisions == "1":
                    print "You wait for an hour. You're starting to get hungry."
                    print "1. Throw yourself into the pit."
                    print "2. Someone will come."
                    whatnow = raw_input("> ")
                    if whatnow == "1":
                        print "You walk closer to the edge of the floor and throw yourself into the pit. You \ndiscover it's endless."
                    else:
                        print "You continue to wait and eventually starve to death."
                elif decisions == "wait":
                    print "You wait for an hour. You're starting to get hungry."
                    print "1. Throw yourself into the pit."
                    print "2. Someone will come."
                    whatnow = raw_input("> ")
                    if whatnow == "1":
                        print "You walk closer to the edge of the floor and throw yourself into the pit. You \ndiscover it's endless."
                    else:
                        print "You continue to wait and eventually starve to death."
                else:
                    print "You walk closer to the edge of the floor and throw yourself into the pit. You \ndiscover it's endless."
            else:
                print "It's heads."
                print "You decide you'll wait."
                print "After an hour, you begin to get bored. What will you do?"
                print "1. Wait some more."
                print "2. Go for the treasure anyway."
                whatnow = raw_input("> ")
                if whatnow == "1":
                    print "You wait for an hour. You're starting to get hungry."
                    print "1. Someone will come."
                    print "2. Eat the coin."
                    whatnow = raw_input("> ")
                    if whatnow == "2":
                        print "You decide to eat the coin."
                        print "You choke to death."
                    else:
                        print "You continue to wait and eventually starve to death."
                else:
                    print "You begin to walk across the room, only to discover the floor beneath you has \nceased to exist. You fall down an endless pit."
                
        elif coinflip1 in tails:
            print "You scream out, 'Tails!'"
            coinflip1 = 2
            print "You watch the coin twirl mid-air before it plummets achingly slowly to the \nground."
            print "It clangs annoyingly and you slowly lean over..."
            if coinflip1 == coinflip2:
                print "It's tails."
                print "You begin to walk across the room, only to discover the floor beneath you has \nceased to exist. You fall down an endless pit."
            elif coinflip2 == 3:
                print "The coin seems to suddenly fall off the edge of something. There's no floor \nahead of you."
                print "What now?"
                print "1. Wait."
                print "2. Throw yourself into the pit."
                decisions = raw_input("> ")
                if decisions == "1":
                    print "You wait for an hour. You're starting to get hungry."
                    print "1. Throw yourself into the pit."
                    print "2. Someone will come."
                    whatnow = raw_input("> ")
                    if whatnow == "1":
                        print "You walk closer to the edge of the floor and throw yourself into the pit. You \ndiscover it's endless."
                    else:
                        print "You continue to wait and eventually starve to death."
                elif decisions == "wait":
                    print "You wait for an hour. You're starting to get hungry."
                    print "1. Throw yourself into the pit."
                    print "2. Someone will come."
                    whatnow = raw_input("> ")
                    if whatnow == "1":
                        print "You walk closer to the edge of the floor and throw yourself into the pit. You \ndiscover it's endless."
                    else:
                        print "You continue to wait and eventually starve to death."
                else:
                    print "You walk closer to the edge of the floor and throw yourself into the pit. You \ndiscover it's endless."
            else:
                print "It's heads."
                print "You decide you'll wait."
                print "After an hour, you begin to get bored. What will you do?"
                print "1. Wait some more."
                print "2. Go for the treasure anyway."
                whatnow = raw_input("> ")
                if whatnow == "1":
                    print "You wait for an hour. You're starting to get hungry."
                    print "1. Someone will come."
                    print "2. Eat the coin."
                    whatnow = raw_input("> ")
                    if whatnow == "2":
                        print "You decide to eat the coin."
                        print "You choke to death."
                    else:
                        print "You continue to wait and eventually starve to death."
                else:
                    print "You begin to walk across the room, only to discover the floor beneath you has \nceased to exist. You fall down an endless pit."
        else:
            print "You fumble around nervously. 'Uh.. uh... something!' you call out."
            print "The door behind you suddenly opens, and you see the exit."
            print "You run out and are safe... for now."
            

else:
    print "You stumble around and fall on a knife and die.  Good job!"