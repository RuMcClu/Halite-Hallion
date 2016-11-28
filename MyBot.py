from source.hlt import *
from source.networking import *
import math
#import numpy as np

myID, gameMap = getInit()

#python addins
import logging
logging.basicConfig(filename='debugging\debug.log',level=logging.DEBUG)
logging.debug('initiating new run')
#def findPerimeter(locations, agress):
#keep a running perimeter and area
#    perimeter = agress
#    return perimeter

#def earlyGame(perimeter):

def mapDistance(map):
    dist4 = [[[[0.0 for i in range(30)] for j in range(30)] for k in range(30)] for l in range(30)]
    angle4 = [[[[0.0 for i in range(30)] for j in range(30)] for k in range(30)] for l in range(30)]
    #logging.debug('managed the empty cells')
    for v in range(map.height):
        for w in range(map.width):
            for y1 in range(map.height):
                for x1 in range(map.width):
                    locat1 = Location(x1,y1)
                    locat2 = Location(w,v)
                    #logging.debug('managed the locations')
                    #site1 = map.getSite(loc1)
                    #site2 = map.getSite(loc2)
                    dist4[x1-1][y1-1][w-1][v-1] = map.getDistance(locat1,locat2)
                    #logging.debug('managed the distances')
                    angle4[x1-1][y1-1][w-1][v-1] = map.getAngle(locat1,locat2)
                    #logging.debug('managed the angles')
                    #logging.debug(dist4[x1-1][y1-1][w-1][v-1])
    #logging.debug('about to return the dist and angle')
    return dist4, angle4



def mapWeight(gameMap,neutral,splash,nearby):
    neutral_site_mult = neutral
    splash_mult = splash
    weight = [[0 for i in range(30)] for j in range(30)]
    border = []
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            loca = Location(x,y)
            site = gameMap.getSite(loca)
            nearbyweight = 0
            if site.owner != myID:
                for d in CARDINALS:
                    neighbour = gameMap.getSite(loca,d)
                    nearbyweight += neighbour.production

                if site.owner != 0:
                    new_strength = site.strength
                    for d in CARDINALS:
                        neighbour = gameMap.getSite(loca,d)
                        if neighbour.owner != myID and neighbour.owner != 0:
                            new_strength = new_strength + neighbour.strength
                    weight[x][y] = site.production + splash * new_strength + nearby*nearbyweight
                else:
                    if site.strength != 0:
                        weight[x][y] = site.production/(neutral * site.strength) + nearby*nearbyweight
                    else:
                        weight[x][y] = site.production/neutral + nearby*nearbyweight
            else:
                for d in CARDINALS:
                    neighbour = gameMap.getSite(loca,d)
                    if neighbour.owner != myID:
                        border.append(loca)
                        break
    return weight , border
    #site = gameMap.getSite(prod[last,0])

def getWeight(weightMat,location):
    weight4 = []
    for d in CARDINALS:
        neighbour_loc = gameMap.getLocation(location, d)
        neigh_y = neighbour_loc.y
        neigh_x = neighbour_loc.x
        weight4.append(weightMat[neigh_x][neigh_y])
    return weight4



#def iniStrat(location):


def move(location,border,origin,wait4,gameMap,ang2,dist2):
    site = gameMap.getSite(location)

    if len(border) < 10:
        for d in CARDINALS:
            neighbour_site = gameMap.getSite(location, d)
            if neighbour_site.owner != myID and max(wait4)==wait4[d-1]:
                if neighbour_site.strength < site.strength and neighbour_site.production > 0:
                    return Move(location, d),
                else:
                    for e in CARDINALS:
                        neighbour_site2 = gameMap.getSite(location, e)
                        if neighbour_site2.owner == myID:
                            if neighbour_site2.strength + site.strength > neighbour_site.strength and neighbour_site.production > 0:
                                if e == NORTH:
                                    dire = SOUTH
                                elif e == SOUTH:
                                    dire = NORTH
                                elif e == EAST:
                                    dire = WEST
                                else:
                                    dire = EAST
                                return Move(gameMap.getLocation(location, e),dire), Move(location, STILL), gameMap.getLocation(location, e)

        return Move(location, STILL),

    else:
        for d in CARDINALS:
            neighbour_site = gameMap.getSite(location, d)
            if location == origin:
                if neighbour_site.owner != myID and neighbour_site.strength < site.strength:
#                    logging.debug(max(wait4))
                    return Move(location, d),
                elif neighbour_site.owner != myID and neighbour_site.strength > site.strength:
                    return Move(location, STILL),
#                logging.debug(wait4[d-1])
            if neighbour_site.owner != myID and neighbour_site.strength < site.strength and max(wait4)==wait4[d-1]:
#                    logging.debug(max(wait4))
                return Move(location, d),
#            if neighbour_site.owner == myID and neighbour_site.strength + site.strength < 300 and neighbour_site != place:
#                im_going_there.append(neighbour_site)
    #put in here the thing about weight dist find max of the thing
    #    if weight/dist
        if len(border) < 6:
            if site.strength < site.production * 7:
                return Move(location, STILL),
        #    elif gameMap.getSite(location,d)
        else:
            if site.strength < site.production * 8:
                return Move(location, STILL),


        moveprob = [0,0]
        angle = ang2[origin.x][origin.y]
        moveprob[0] = abs(math.sin(angle))
        moveprob[1] = abs(math.cos(angle))

        for place in im_going_there:
            if site.strength > 200:
                bordlist = []
                for bord in border:
                    bordlist.append(dist2[bord.x][bord.y])
                for bord in border:
                    if max(bordlist) == dist2[bord.x][bord.y]:
                        dx = bord.x-x
                        dy = bord.y-y
                        if abs(dx)<=abs(dy):
                            if dx > 0 and gameMap.getSite(location, EAST) != place:
                                im_going_there.append(gameMap.getSite(location, EAST))
                                Move(location,EAST)
                            elif dx < 0 and gameMap.getSite(location, WEST) != place:
                                im_going_there.append(gameMap.getSite(location, WEST))
                                Move(location,WEST)
                        elif abs(dy)<abs(dx):
                            if dy > 0 and gameMap.getSite(location, NORTH) != place:
                                im_going_there.append(gameMap.getSite(location, NORTH))
                                Move(location,NORTH)
                            elif dy < 0 and gameMap.getSite(location, SOUTH) != place:
                                im_going_there.append(gameMap.getSite(location, SOUTH))
                                Move(location,SOUTH)

            p_thing = random.random()

            if site.strength > 100:
                if random.random() > 0.95 * moveprob[0] and gameMap.getSite(location, NORTH) != place:
                    im_going_there.append(gameMap.getSite(location, NORTH))
                    return Move(location, NORTH),
                elif random.random() > 0.92 * moveprob[1] and gameMap.getSite(location, WEST) != place:
                    im_going_there.append(gameMap.getSite(location, WEST))
                    return Move(location, WEST),
                elif random.random() > 0.88 * moveprob[1] and gameMap.getSite(location, EAST) != place:
                    im_going_there.append(gameMap.getSite(location, EAST))
                    return Move(location, EAST),
                elif random.random() > 0.82 * moveprob[0] and gameMap.getSite(location, SOUTH) != place:
                    im_going_there.append(gameMap.getSite(location, SOUTH))
                    return Move(location, SOUTH),

            if angle >= 0 and moveprob[0] > moveprob[1] and gameMap.getSite(location, NORTH) != place:
                if p_thing > 0.2:
                    im_going_there.append(gameMap.getSite(location, NORTH))
                    return Move(location, NORTH),
                elif p_thing > 0.05 and gameMap.getSite(location, WEST) != place:
                    im_going_there.append(gameMap.getSite(location, WEST))
                    return Move(location, WEST),
            elif angle <= 0 and moveprob[1] >= moveprob[0] and gameMap.getSite(location, WEST) != place:
                if p_thing > 0.2:
                    im_going_there.append(gameMap.getSite(location, WEST))
                    return Move(location, WEST),
                elif p_thing > 0.05 and gameMap.getSite(location, NORTH) != place:
                    im_going_there.append(gameMap.getSite(location, NORTH))
                    return Move(location, NORTH),
            elif angle >= 0 and moveprob[1] >= moveprob[0] and gameMap.getSite(location, EAST) != place:
                if  p_thing > 0.2:
                    im_going_there.append(gameMap.getSite(location, EAST))
                    return Move(location, EAST),
                elif p_thing > 0.05 and gameMap.getSite(location, SOUTH) != place:
                    im_going_there.append(gameMap.getSite(location, SOUTH))
                    return Move(location, SOUTH),
            elif angle <= 0 and moveprob[0] > moveprob[1] and gameMap.getSite(location, SOUTH) != place:
                if p_thing > 0.2:
                    im_going_there.append(gameMap.getSite(location, SOUTH))
                    return Move(location, SOUTH),
                elif p_thing > 0.05 and gameMap.getSite(location, EAST) != place:
                    im_going_there.append(gameMap.getSite(location, EAST))
                    return Move(location, EAST),



            return Move(location, STILL),






agress = []
#zone
#perimeter = 1
i = 0

logging.debug('is about to do the map')
map = GameMap(30, 30, 2)
distAngMat = mapDistance(map)
distMat = distAngMat[0]
angMat = distAngMat[1]
#logging.debug(distAngMat)

sendInit("RuBot v1.06")

while True:
    moves = []
    gameMap = getFrame()
    im_going_there = [[23,10]]
    agress3 = []
    skip_location = [[23,10]]
    k = 1
    weight_border = mapWeight(gameMap,1.0,1.0,1.0)
    weightMat=weight_border[0]
    borderList=weight_border[1]
    logging.debug(borderList)
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if gameMap.getSite(location).owner == myID:
                wait4 = getWeight(weightMat, location)
                if i==0:
                    origin = location
                for kk in range(k):
                    if location != skip_location[kk]:
                        the_move = move(location,borderList,origin,wait4,gameMap,angMat[x][y][:][:],distMat[x][y][:][:])
                        logging.debug('the_move worked')
                        logging.debug(the_move)
                        if len(the_move) == 3:
                        #    logging.debug(i)
                        #    logging.debug('len == 3 true')
                            moves.append(the_move[0])
                    #        logging.debug('move 0 okay')
                            moves.append(the_move[1])
                    #        logging.debug('move 1 okay')
                            skip_location.append(the_move[2])
                            k = k + 1
                        else:
                            moves.append((the_move)[0])
                    #        logging.debug('move appended')
                    #j = j + 1
    logging.debug('x y over')
    i = i + 1
    logging.debug(moves)
    sendFrame(moves)
    logging.debug('Frame sent')
