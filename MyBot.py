from hlt import *
from networking import *
import math
#import numpy as np

myID, gameMap = getInit()
sendInit("RuBot")
#python addins

#def findPerimeter(locations, agress):
#keep a running perimeter and area
#    perimeter = agress
#    return perimeter

#def earlyGame(perimeter):

#def zoneID(prod):
    #site = gameMap.getSite(prod[last,0])



#def iniStrat(location):


def move(location,agress,agress3,origin,map):
    site = gameMap.getSite(location)
    perimeterx = len(agress)

    if perimeterx < 3:
        for d in CARDINALS:
            neighbour_site = gameMap.getSite(location, d)
            if neighbour_site.owner != myID and neighbour_site.strength < site.strength and neighbour_site.production > 0:
                agress3.append(1)
                return Move(location, d), agress3
            else:
                return Move(location, STILL), agress3

    else:
        for d in CARDINALS:
            neighbour_site = gameMap.getSite(location, d)
            for place in im_going_there:
                if neighbour_site.owner != myID and neighbour_site.strength < site.strength and neighbour_site != place:
                    im_going_there.append(neighbour_site)
                    agress3.append(1)
                    return Move(location, d), agress3
#            if neighbour_site.owner == myID and neighbour_site.strength + site.strength < 300 and neighbour_site != place:
#                im_going_there.append(neighbour_site)

        if perimeterx < 6:
            if site.strength < site.production * 7:
                return Move(location, STILL), agress3
        #    elif gameMap.getSite(location,d)
        else:
            if site.strength < site.production * 8:
                return Move(location, STILL), agress3

        moveprob = [0,0]
        angle = map.getAngle(location,origin)
        moveprob[0] = abs(math.sin(angle))
        moveprob[1] = abs(math.cos(angle))

        for place in im_going_there:
            p_thing = random.random()
            if angle >= 0 and moveprob[0] > moveprob[1] and gameMap.getSite(location, NORTH) != place:
                if p_thing > 0.2:
                    im_going_there.append(gameMap.getSite(location, NORTH))
                    return Move(location, NORTH), agress3
                elif p_thing > 0.05 and gameMap.getSite(location, WEST) != place:
                    im_going_there.append(gameMap.getSite(location, WEST))
                    return Move(location, WEST), agress3
            elif angle >= 0 and moveprob[1] >= moveprob[0] and gameMap.getSite(location, WEST) != place:
                if p_thing > 0.2:
                    im_going_there.append(gameMap.getSite(location, WEST))
                    return Move(location, WEST), agress3
                elif p_thing > 0.05 and gameMap.getSite(location, NORTH) != place:
                    im_going_there.append(gameMap.getSite(location, NORTH))
                    return Move(location, NORTH), agress3
            elif angle <= 0 and moveprob[1] >= moveprob[0] and gameMap.getSite(location, EAST) != place:
                if  p_thing > 0.2:
                    im_going_there.append(gameMap.getSite(location, EAST))
                    return Move(location, EAST), agress3
                elif p_thing > 0.05 and gameMap.getSite(location, SOUTH) != place:
                    im_going_there.append(gameMap.getSite(location, SOUTH))
                    return Move(location, SOUTH), agress3
            elif angle <= 0 and moveprob[0] > moveprob[1] and gameMap.getSite(location, SOUTH) != place:
                if p_thing > 0.2:
                    im_going_there.append(gameMap.getSite(location, SOUTH))
                    return Move(location, SOUTH), agress3
                elif p_thing > 0.05 and gameMap.getSite(location, EAST) != place:
                    im_going_there.append(gameMap.getSite(location, EAST))
                    return Move(location, EAST), agress3


            if site.strength > 100:
                if random.random() > 0.85 * moveprob[0] and gameMap.getSite(location, NORTH) != place:
                    im_going_there.append(gameMap.getSite(location, NORTH))
                    return Move(location, NORTH), agress3
                elif random.random() > 0.71 * moveprob[1] and gameMap.getSite(location, WEST) != place:
                    im_going_there.append(gameMap.getSite(location, WEST))
                    return Move(location, WEST), agress3
                elif random.random() > 0.64 * moveprob[1] and gameMap.getSite(location, EAST) != place:
                    im_going_there.append(gameMap.getSite(location, EAST))
                    return Move(location, EAST), agress3
                elif random.random() > 0.6 * moveprob[0] and gameMap.getSite(location, SOUTH) != place:
                    im_going_there.append(gameMap.getSite(location, SOUTH))
                    return Move(location, SOUTH), agress3
            return Move(location, STILL), agress3






agress = []
#zone
#perimeter = 1
i = 0

map = GameMap(30, 30, 2)
while True:
    moves = []
    gameMap = getFrame()
    im_going_there = [[23,10]]
    agress3 = []

    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if gameMap.getSite(location).owner == myID:
                if i==0:
                    origin = location
                moves.append(move(location,agress,agress3,origin,map)[0])
                agress3.append(move(location,agress,agress3,origin,map)[1])
    i = i + 1
    agress = agress3
    sendFrame(moves)
