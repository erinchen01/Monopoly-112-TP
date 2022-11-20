from cmu_112_graphics import *

import random, tkinter

npNameList = ['Acadia', 'American Samoa', 'Arches', 'Badlands', 'Big Bend',
            'Biscayne', 'Carlsbad Caverns', 'Crater Lake', 'Death Valley',
            'Dry Tortugas', 'Gates of the Arctic', 'Glacier Bay',
            'Great Smoky Mountains', 'Isle Royale', 'Joshua Tree',
            'Kings Canyon', 'Lake Clark', 'New River Gorge', 'North Cascades',
            'Petrified Forest', 'Redwood', 'Rocky Mountain', 'Saguaro',
            'Sequoia', 'Theodore Roosevelt', 'Voyageurs', 'Virgin Islands',
            'White Sands', 'Yellowstone', 'Zion']
cpNameList = ['Royal Gorge Park', 'Falls Park', 'Scioto Audubon',
              'Rifle Mountain Park', 'Fairmount Park', 'City Park',
              'Zilker Park', 'The Gathering Place', 'Papago Park']
npUKNameList = ['Peak District', 'Lake District', 'Snowdonia', 'Dartmoor',
                'Pembrokeshire Coast', 'North York Moors', 'Yorkshire Dales',
                'Exmoor', 'Northumberland', 'Brecon Beacons', 'The Broads',
                'Cairngorms', 'New Forest', 'South Downs']
nonFunctionalPlaces = [None]
nameList = npNameList + cpNameList + npUKNameList + nonFunctionalPlaces

class Grid:
    def __init__(self):
        self.name = random.choice(nameList)
        if self.name in (npNameList, cpNameList, npUKNameList):
            nameList.remove(self.name)
        self.owner = None
        self.priceToBuy = random.randint(3000, 6000)
        self.priceToUpgrade = int(0.4 * self.priceToBuy)
        
        self.level = 0
        self.toll = 0
        self.priceToSell = int(self.priceToBuy * 0.7)

        self.chargeTolls = False
    
    def buying(self, owner):
        self.owner = owner
        self.level = 1
        self.chargeTolls = True
        self.toll = int(4 * 0.1 * self.priceToBuy)

    def upgrading(self):
        self.level += 1
        self.toll += int(4 * 0.1 * self.priceToBuy)

    def selling(self):
        self.owner = None
        self.toll -= int(4 * 0.1 * self.priceToBuy)

    def __repr__(self): ####need to improve
        return f'{self.name}'
        





#board
board1 = [[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
          [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
          [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
          [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
          [0,0,0,0,0,0,0,0,0,1,1,1,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
          [1,1,1,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,0,1,1,1,1,1,1,1,1,0,0,0,0,0]
]



board2 = [[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,1,0,0,0.0,0,1],
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1],
          [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]
]


board3 = [[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
          [0,0,0,1,1,1,1,1,1,1,0,0,0,0,1],
          [0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
          [0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
          [0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
          [0,0,0,1,0,0,0,0,0,1,1,1,1,1,1],
          [0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
          [1,1,1,1,1,1,1,1,1,1,0,0.0,0,0],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [1,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
]

board4 = [[0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
          [1,1,1,1,0,0,0,0,0,0,0,1,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
          [1,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
          [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]



class Board():
    def __init__(self, selectedBoard):
        self.map = selectedBoard
        self.detailedInfo = self.makeDetailedInfo()
    
    def makeDetailedInfo(self):
        detailedInfo = dict()
        rows, cols = self.getDims()
        for row in range(rows):
            for col in range(cols):
                coord = (row, col)
                if self.map[row][col] == 0:
                    detailedInfo[coord] = None
                else:
                    detailedInfo[coord] = dict()
                    self.map[row][col] = Grid() #####
                    grid = self.map[row][col]
                    if grid.name != None:
                        detailedInfo[coord]['property name'] = grid.name
                        detailedInfo[coord]['price to buy'] = grid.priceToBuy
                        if grid.owner != None:
                            detailedInfo[coord]['owner'] = grid.owner
                            detailedInfo[coord]['cost to upgrade'] = (
                                                            grid.priceToUpgrade)
                            detailedInfo[coord]['toll'] = (grid.toll)
                        detailedInfo[coord]['owner'] = 'No Owner'
                    else:
                        detailedInfo[coord] = None
        return detailedInfo


    def getDims(self):
        rows = len(self.map)
        cols = len(self.map[0])
        return rows, cols

    def getRandomPlace(self): 
        rows, cols = self.getDims()
        if True:
            x = random.randint(0, rows-1)
            for y in range(cols):
                if self.map[x][y]:
                    return x, y

#testCase of getRandomPlace()
myBoard = Board(board4)  ## do not comment out
# print(myBoard.getRandomPlace())

dice = random.randint(1, 6)

colors = ['red', 'green', 'blue', 'yellow']


class Player:
    def __init__(self, playerName):
        self.loc = myBoard.getRandomPlace()
        self.cards = []
        self.myTurn = False
        self.myProperties = []
        self.money = 50000
        self.ori = self.checkOri()
        self.color = random.choice(colors)
        colors.remove(self.color)
        self.playerName = playerName
    
    
    def __repr__(self):
        return self.playerName
 

    def isLegalMove(self, checkingMove):
        curLocRow, curLocCol = self.loc
        dRow, dCol = checkingMove
        boardRows, boardCols = myBoard.getDims()

        if ((0 <= curLocRow + dRow < boardRows) and 
            (0 <= curLocCol + dCol < boardCols) and
            isinstance(myBoard.map[curLocRow + dRow][curLocCol + dCol], Grid)):
            return True
        return False


    def checkOri(self):
        leftMove = (0, -1)
        rightMove = (0, +1)
        upMove = (+1, 0)
        downMove = (-1, 0)
        for i in (rightMove, leftMove, downMove, upMove):
            if self.isLegalMove(i):
                ori = i
                return ori


    def changeOri(self): #only modify self.ori
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
            if self.isLegalMove(checkingMove):
                self.ori = checkingMove


    def move(self, dice): # only modify self.loc
        curLocRow, curLocCol = self.loc
        for _ in range(dice):
            if not self.isLegalMove(self.ori):
                self.changeOri()
            curLocRow += self.ori[0]
            curLocCol += self.ori[1]
            self.loc = curLocRow, curLocCol
    

    def changeMyTurn(self):
        self.myTurn = True
        

    def buyProperty(self):
        curRow, curCol = self.loc
        grid = myBoard.map[curRow][curCol]
        # modify the params of the grid
        grid.buying(self)

        # modify the params of players
        self.myProperties.append(grid)
        self.money -= grid.priceToBuy


    def upgradeProperty(self): # modify params of player and return msg
        curRow, curCol = self.loc
        grid = myBoard.map[curRow][curCol]
        if self.money < grid.priceToUpgrade:
            return "No enough money to upgrade!"
        elif self.money >= grid.priceToUpgrade:
            self.money -= grid.priceToUpgrade
            # modify the params of the grid
            grid.upgrading()
            return "Successfully upgraded the property."


    def sellProperty(self):
        curRow, curCol = self.loc
        grid = myBoard.map[curRow][curCol]
        # modify the params of players
        self.money += grid.priceToSell
        self.myProperties.remove(grid)

        # modify the params of the grid
        grid.selling()
        return f'''Successfully sold {grid.name}.\
Now you have {self.money} dollars left.\
        '''



# Please ignore the below code
# twoDx = 5
# twoDy = 5

# def twoDToIso(app, twoDx, twoDy):
#     app.isoWidth = twoDx * app.gridWidth
#     app.isoHeight = 
#     canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3)
#     twoDx 

# def appStarted(app):
#     app.gridLength = 5
#     app.gridWidth = 5
#     app.message = 'Press any key'

# def keyPressed(app, event):
#     app.message = f"event.key == '{event.key}'"

# def redrawAll(app, canvas):
#     canvas.create_text(app.width/2, 40, text=app.message,
#                        font='Arial 30 bold', fill='black')
    
#     keyNamesText = '''Here are the legal event.key names:
#                       * Keyboard key labels (letters, digits, punctuation)
#                       * Arrow directions ('Up', 'Down', 'Left', 'Right')
#                       * Whitespace ('Space', 'Enter', 'Tab', 'BackSpace')
#                       * Other commands ('Delete', 'Escape')'''

#     y = 80
#     for line in keyNamesText.splitlines():
#         canvas.create_text(app.width/2, y, text=line.strip(),
#                            font='Arial 20', fill='black')
#         y += 30

# runApp(width=600, height=400)

