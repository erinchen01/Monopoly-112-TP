
import random, decimal
from boards import *

##########################################
# Button class
##########################################
class Button:
    def __init__(self, buttonName, centerpoints):
        self.name = buttonName
        self.enabled = False
        self.coord = centerpoints
    
    def getCoords(self, app):
        cx, cy = self.coord
        x0, x1 = cx - app.width * 0.05, cx + app.width * 0.05
        y0, y1 = cy - app.height * 0.05, cy + app.height * 0.05
        return x0, y0, x1, y1
        
##########################################
# Grid class
##########################################
# This function of roundHalfUp(d) is taken from 112 cource website
def roundHalfUp(d):
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

class Grid:
    def __init__(self, gridName, gridPriceToBuy):
        self.name = gridName
        self.owner = None
        self.priceToBuy = gridPriceToBuy
        self.priceToUpgrade = int(0.4 * self.priceToBuy)
        
        self.level = 0
        self.toll = 0
        self.priceToSell = int(self.priceToBuy * 0.7)

        self.chargeTolls = False
    
    def buying(self, owner):
        self.owner = owner
        self.level = 1
        self.chargeTolls = True
        self.toll = int(0.35 * self.priceToBuy)
        self.priceToSell = int(self.priceToBuy * 0.7)

    def upgrading(self):
        self.level += 1
        self.toll += int(0.35 * self.priceToBuy)
        self.priceToSell == int(self.priceToBuy * 0.7) * self.level

    def selling(self):
        self.owner = None
        self.toll = 0
        self.level = 0

    def __repr__(self): ####need to improve
        return f'{self.name}'
        

eventsDetails = dict()
eventsDetails['Market Crash'] = dict()
eventsDetails['Market Crash']['description'] = '''
\nYou encountered a markect crash;
everyone loses $2000.\
'''
eventsDetails['Go to Jail'] = dict()
eventsDetails['Go to Jail']['description'] = '''
\nYou were arrested on 
suspicion of drunk driving
for three rounds.\
'''
eventsDetails['Get out of Jail Free'] = dict()
eventsDetails['Get out of Jail Free']['description'] = '''
\nYou accidentally picked up 
a magic card.
Get out of Jail Free. 
This card may be kept until needed.\
'''
eventsDetails['Chairman'] = dict()
eventsDetails['Chairman']['description'] = '''
You have been elected
Chairman of the Board.
Pay each player $500. \
'''
eventsDetails['competition'] = dict()
eventsDetails['competition']['description'] = '''\
You have won a crossword competition.
Collect $900.\
'''
eventsDetails['poor tax'] = dict()
eventsDetails['poor tax']['description'] = '''\
Pay poor tax of $120.\
'''
eventsDetails['parking fee'] = dict()
eventsDetails['parking fee']['description'] = '''\
Pay parking fine of $500.\
'''

class chanceCards():
    def __init__(self, eventName):
        self.name = 'chance'
        # events of chance cards
        self.eventName = eventName
        self.description = eventsDetails[eventName]['description']
        
    
    


##########################################
# Board class
##########################################

class Board():
    def __init__(self, selectedBoard):
        self.map = selectedBoard

    def getDims(self):
        rows = len(self.map)
        cols = len(self.map[0])
        return rows, cols

    def getRandomPlace(self): 
        rows, cols = self.getDims()
        if True:
            row = random.randint(0, rows-1)
            for col in range(cols):
                if self.map[row][col]:
                    return row, col



##########################################
# Player class
##########################################

class Player:
    def __init__(self, playerName, color):
        self.cards = []
        self.myTurn = False
        self.myProperties = []
        self.money = 50000
        self.playerName = playerName
        self.color = color
        self.activated = True
    
    
    def __repr__(self):
        return f'Player {self.playerName}'
 

    def isLegalMove(self, app, checkingMove):
        curLocRow, curLocCol = self.loc
        dRow, dCol = checkingMove
        boardRows, boardCols = app.myBoard.getDims()

        if ((0 <= curLocRow + dRow < boardRows) and 
            (0 <= curLocCol + dCol < boardCols) and
            app.myBoard.map[curLocRow + dRow][curLocCol + dCol]):
            return True
        return False


    def checkOri(self, app):
        leftMove = (0, -1)
        rightMove = (0, +1)
        upMove = (+1, 0)
        downMove = (-1, 0)
        for ori in (rightMove, leftMove, downMove, upMove):
            if self.isLegalMove(app, ori):
                return ori


    def changeOri(self, app): #only modify self.ori
        lastOri = self.ori
        leftMove = (0, -1)
        rightMove = (0, +1)
        upMove = (+1, 0)
        downMove = (-1, 0)
        availableOris = [rightMove, leftMove, downMove, upMove]
        if lastOri == rightMove:
            availableOris.remove(leftMove)
        elif lastOri == leftMove:
            availableOris.remove(rightMove)
        elif lastOri == downMove:
            availableOris.remove(upMove)
        else:
            availableOris.remove(downMove)

        for checkingMove in availableOris:
            if self.isLegalMove(app, checkingMove):
                self.ori = checkingMove

    def playDice(self):
        dice = random.randint(1,6)
        return dice

    def move(self, app, dice): # only modify self.loc
        curLocRow, curLocCol = self.loc
        for _ in range(dice):
            if not self.isLegalMove(app, self.ori):
                self.changeOri(app)
            curLocRow += self.ori[0]
            curLocCol += self.ori[1]
            self.loc = curLocRow, curLocCol
        app.playerInfo[app.curPlayer]['loc'] = self.loc
    

    def changeMyTurn(self):
        self.myTurn = True
        

    def buyProperty(self, app):
        curRow, curCol = app.row, app.col
        grid = app.myBoard.map[curRow][curCol]
        # modify the params of players
        self.myProperties.append(grid)
        self.money -= grid.priceToBuy


    def upgradeProperty(self, app): # modify params of player and return msg
        curRow, curCol = self.loc
        grid = app.myBoard.map[curRow][curCol]
        if self.money < grid.priceToUpgrade:
            return "No enough money to upgrade!"
        elif self.money >= grid.priceToUpgrade:
            self.money -= grid.priceToUpgrade
            # modify the params of the grid
            grid.upgrading()
            return "Successfully upgraded the property."


    def sellProperty(self, app):
        curRow, curCol = app.row, app.col
        grid = app.myBoard.map[curRow][curCol]
        # modify the params of players
        self.money += grid.priceToSell
        self.myProperties.remove(grid)

        # modify the params of the grid
        grid.selling()

    def payToll(self, app):
        row, col = self.loc
        grid = app.myBoard.map[row][col]
        toll = grid.toll
        self.money -= toll
        owner = grid.owner
        owner.money += toll
