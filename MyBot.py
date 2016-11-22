from hlt import *
from networking import *

#import logging
#logging.basicConfig(filename='example.log',level=logging.DEBUG)
#logging.debug('your message here')

myID, gameMap = getInit()
sendInit("RuBot")
#python addins

#def findPerimeter(locations, agress):
#keep a running perimeter and area
#    perimeter = agress
#    return perimeter

#def earlyGame(perimeter):
"""
def move(location,agress3):
    site = gameMap.getSite(location)
    perimeterx = len(agress3)
    for d in CARDINALS:
        neighbour_site = gameMap.getSite(location, d)
        if neighbour_site.owner != myID and neighbour_site.strength < site.strength:
            agress3.append(1)
            return Move(location, d), agress3

    if site.strength < site.production * 5:
        return Move(location, STILL), agress3
    return Move(location, NORTH if random.random() > 0.5 else WEST), agress3

"""
def zoneID(prod):
    site = gameMap.getSite(prod[:,0])



def iniStrat(location):


def move(location,agress,agress3):
    site = gameMap.getSite(location)
    perimeterx = len(agress)
    if perimeterx < 3:
        for d in CARDINALS:
            neighbour_site = gameMap.getSite(location, d)
            if neighbour_site.owner != myID and neighbour_site.strength < site.strength:
                agress3.append(1)
                return Move(location, d), agress3
            else:
                return Move(location, STILL), agress3
    elif perimeterx < 6:
    #insert biased random walk

        for d in CARDINALS:
            neighbour_site = gameMap.getSite(location, d)
            if neighbour_site.owner != myID and neighbour_site.strength < site.strength:
                agress3.append(1)
                return Move(location, d), agress3
        if site.strength < site.production * 5:
            return Move(location, STILL), agress3


    else:

        for d in CARDINALS:
            neighbour_site = gameMap.getSite(location, d)
            if neighbour_site.owner != myID and neighbour_site.strength < site.strength:
                agress3.append(1)
                return Move(location, d), agress3
        if site.strength < site.production * 2:
            return Move(location, STILL), agress3

    return Move(location, NORTH if random.random() > 0.5 else WEST), agress3

agress = []
prod=[]
zone
#perimeter = 1
i = 0
while True:
    moves = []
    gameMap = getFrame()
    agress3 = []
    weights = []

#    locationNo = []
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if i=0:
                prod.append(location,gameMap.getSite(location).production)
                zone.append(zoneID(prod))

            if gameMap.getSite(location).owner == myID:
                moves.append(move(location,agress,agress3)[0])
                agress3.append(move(location,agress,agress3)[1])
            else:
                weights.append(iniStrat(location))
#            locationNo.append(1)
    if i=0:

    agress = agress3
    sendFrame(moves)
    i + 1
