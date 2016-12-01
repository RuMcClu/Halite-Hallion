import numpy as np
#from source.hlt import *
#from source.networking import *
#import math

def mapWeight(gameMap,neutral,splash,nearby):
    neutral_site_mult = neutral
    splash_mult = splash
    weight = np.zeros((gameMap.width, gameMap.height), dtype=float)
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
                    weight[x,y] = site.production + splash * new_strength + nearby*nearbyweight
                else:
                    if site.strength != 0:
                        weight[x,y] = site.production/(neutral * site.strength) + nearby*nearbyweight
                    else:
                        weight[x,y] = site.production/neutral + nearby*nearbyweight
            else:
                for d in CARDINALS:
                    neighbour = gameMap.getSite(loca,d)
                    if neighbour.owner != myID:
                        border.append(loca)
                        break
    return weight , border

def updateWeight(gameMap,gameMap2,weightMat,neutral,splash,nearby):
    neutral_site_mult = neutral
    splash_mult = splash
    weight = weightMat
    border = []
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            loca = Location(x,y)
            site = gameMap.getSite(loca)
            oldsite = gameMap2.getSite(loca)
            nearbyweight = 0
            if site.owner != myID:
                if oldsite.owner != site.owner:
                    for d in CARDINALS:
                        neighbour = gameMap.getSite(loca,d)
                        nearbyweight += neighbour.production

                    if site.owner != 0:
                        new_strength = site.strength
                        for d in CARDINALS:
                            neighbour = gameMap.getSite(loca,d)
                            if neighbour.owner != myID and neighbour.owner != 0:
                                new_strength = new_strength + neighbour.strength
                        weight[x,y] = site.production + splash * new_strength + nearby*nearbyweight
                    else:
                        if site.strength != 0:
                            weight[x,y] = site.production/(neutral * site.strength) + nearby*nearbyweight
                        else:
                            weight[x,y] = site.production/neutral + nearby*nearbyweight
                else:
                    for d in CARDINALS:
                        neighbour = gameMap.getSite(loca,d)
                        if neighbour.owner != myID:
                            border.append(loca)
                            break
    return weight , border

def getWeight(weightMat,location):
    weight4 = []
    for d in CARDINALS:
        neighbour_loc = gameMap.getLocation(location, d)
        neigh_y = neighbour_loc.y
        neigh_x = neighbour_loc.x
        weight4.append(weightMat[neigh_x][neigh_y])
    return weight4
