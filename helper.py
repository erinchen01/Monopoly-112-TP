# the concept of the calculation is from 
# https://gamedevelopment.tutsplus.com/tutorials/
# creating-isometric-worlds-a-primer-for-game-developers--gamedev-6511

def twoDToIso(twoDx, twoDy):
    isoX = twoDx - twoDy
    isoY = (twoDx + twoDy) / 2
    return(isoX, isoY)

def isoToTwoD(isoX, isoY):
    twoDx = (2 * isoY + isoX) / 2
    twoDy = (2 * isoY - isoX) / 2
    return twoDx, twoDy