# code snippets



#move in randomish direction out from center with avoidance
            if site.strength > 120:
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
