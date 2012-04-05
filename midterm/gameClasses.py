room_num = range(0,10)
npc_num = range(0,20)

class Room(object):
    
    rooms ={}

    def __init__(self,name,x,y,z,desc):
        self.name = name
        self.coords = (int(x),int(y),int(z))
        self.desc = desc
        self.exits = []
        self.exits_as_str = ""
        self.npcs = []
        self.npcs_as_str = ""
        Room.rooms[self.name] = {"name": self.name, "coords": self.coords, "exits": self.exits}
        
    def update(self):
    	self.exits = []
        for i in (range(len(Room.rooms.keys()))):
            #for other in Room.rooms:   
            xdiff = -(self.coords[0] - Room.rooms[Room.rooms.keys()[i]]["coords"][0]) #Indexing TO THE EXTREEEME
            ydiff = -(self.coords[1] - Room.rooms[Room.rooms.keys()[i]]["coords"][1])
            zdiff = -(self.coords[2] - Room.rooms[Room.rooms.keys()[i]]["coords"][2])
            
            if xdiff == 1 and ydiff == 1 and zdiff == 0:
                self.exits.append("northeast")
            elif xdiff == 1 and ydiff == 0 and zdiff == 0:
                self.exits.append("east")
            elif xdiff == 0 and ydiff == 1 and zdiff == 0:
                self.exits.append("north")
            elif xdiff == 0 and ydiff == 0 and zdiff == 1:
                self.exits.append("up")
            elif xdiff == 0 and ydiff == 0 and zdiff == -1:
                self.exits.append("down")
            elif xdiff == -1 and ydiff == 0 and zdiff == 0:
                self.exits.append("west")
            elif xdiff == -1 and ydiff == -1 and zdiff == 0:
                self.exits.append("southwest")
            elif xdiff == 0 and ydiff == -1 and zdiff == 0:
                self.exits.append("south")
            elif xdiff == -1 and ydiff == 1 and zdiff == 0:
                self.exits.append("northwest")
            elif xdiff == 1 and ydiff == -1 and zdiff == 0:
                self.exits.append("southeast")
        if self.exits:

            for blah in range(0,len(self.exits)):
                if len(self.exits) == 1:
                    self.exits_as_str = self.exits[0]                    
                    
                elif len(self.exits) == 2:
                    self.exits_as_str = self.exits[0] + " and " + self.exits[1]
                elif blah == len(self.exits)-1 and len(self.exits) != 2:
                    self.exits_as_str = "and "+ self.exits[-1]
                else:
                    self.exits_as_str += self.exits[blah] + ", "
                
        if len(self.exits)== 0:
            self.exit_str = " There are no exits."
        else:
            self.exit_str = " You may leave to the %s." % (self.exits_as_str)
        #if 
        
class Player(object):

    def __init__(self):
        self.name = ""
        self.coords = [0,0,0]
        self.items = {}


user = Player()

def look():
    for key in range(len(Room.rooms.keys())):
        if user.coords[0] == room_num[key].coords[0] and user.coords[1] == room_num[key].coords[1] and user.coords[2] == room_num[key].coords[2]:
            print room_num[key].name
            print room_num[key].desc + room_num[key].exit_str
        

userinput = "" # Global; needed for possibly Command Class and main game

  
class Command(object):
    commands = {}
    def __init__(self, name, string):
        self.name = name.lower()
        self.string = string
        Command.commands[self.name] = {"name": self.name, "string": self.string}
    
    
# Make this
drxns = ["n", "north", "e", "east", "w","west", "s", "south", "ne", "northeast", "nw", "northwest", "se", "southeast", "sw","southwest", "u", "up", "d", "down"]
directions = [["n", "north"], ["e", "east"], ["w","west"], ["s", "south"], ["ne", "northeast"], ["nw", "northwest"], ["se", "southeast"], ["sw","southwest"], ["u", "up"], ["d", "down"]]
#dir_try = ""
userinput = ""
  
def move(direction):
    #global dir_try #test variable // lost in the definition
    global userinput # test variable // lost in the definition
    # print "***||AFTER THE MOVE FUNCTION||***\ndir_try: %s\nuserinput: %s" % (direction, userinput) # testing! // not appearing at this point
    for dirs in range(len(directions)):
        if direction == directions[dirs][0]:
            direction = directions[dirs][1]
    for key in range(len(Room.rooms.keys())):
        if user.coords[0] == room_num[key].coords[0] and user.coords[1] == room_num[key].coords[1] and user.coords[2] == room_num[key].coords[2]:
            # print "The exits: %s" % (room_num[key].exits)
            if direction in room_num[key].exits:
                if direction == "north":
                    user.coords[1] += 1
                elif direction == "south":
                    user.coords[1] -= 1
                elif direction == "west":
                    user.coords[0] -= 1
                elif direction == "east":
                    user.coords[0] += 1
                elif direction == "up":
                    user.coords[2] += 1
                elif direction == "down":
                    user.coords[2] -= 1
                print "\nYou move %s.\n" % direction
                for j in range(len(Room.rooms.keys())):
    				room_num[j].update()
                look()
                break
            else:
                print "You can't go %s, there are no directions that way!" % direction
        	userinput = ""


class NPC(object):
    npcs = {}
    def __init__(self,name,x,y,z,type,gender,shortDesc,longDesc):
        self.name = name
        self.coords = [int(x),int(y),int(z)]
        self.type = type
        self.gender = gender
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        #NPC.npcs[self.name] = {"name": self.name, "coords": self.coords, "type"}