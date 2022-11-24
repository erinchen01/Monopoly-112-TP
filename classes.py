from cmu_112_graphics import *

import random, tkinter

##########################################
# Grid class
##########################################

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
functionPlaceList = ['prison']
nonFunctionalPlaces = [None]
nameList = (npNameList + cpNameList + npUKNameList +
            functionPlaceList + nonFunctionalPlaces)

class Grid:
    def __init__(self, app):
        self.name = random.choice(app.nameList)
        if self.name is 'prison':
            app.nameList.remove(app.functionPlaceList)
        if self.name in (app.npNameList, app.cpNameList, 
                         app.npUKNameList, app.functionPlaceList):
            app.nameList.remove(self.name)
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
        


##########################################
# Board class
##########################################
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
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
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
          [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
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
# myBoard = Board(board4)  ## do not comment out
# print(myBoard.getRandomPlace())
# print(myBoard.map[0][0])


##########################################
# Player class
##########################################

dice = random.randint(1, 6)

colors = ['red', 'green', 'blue', 'yellow']


class Player:
    def __init__(app, self, playerName):
        self.loc = app.myBoard.getRandomPlace()
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
 

    def isLegalMove(self, app, checkingMove):
        curLocRow, curLocCol = self.loc
        dRow, dCol = checkingMove
        boardRows, boardCols = app.myBoard.getDims()

        if ((0 <= curLocRow + dRow < boardRows) and 
            (0 <= curLocCol + dCol < boardCols) and
            isinstance(app.myBoard.map[curLocRow + dRow][curLocCol + dCol], Grid)):
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
            if self.isLegalMove(app, checkingMove):
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
        

    def buyProperty(self, app):
        curRow, curCol = self.loc
        grid = app.myBoard.map[curRow][curCol]
        # modify the params of the grid
        grid.buying(self)

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
        curRow, curCol = self.loc
        grid = app.myBoard.map[curRow][curCol]
        # modify the params of players
        self.money += grid.priceToSell
        self.myProperties.remove(grid)

        # modify the params of the grid
        grid.selling()
        return f'''Successfully sold {grid.name}.\
Now you have {self.money} dollars left.\
        '''

# The concept of mode is learnt from 112 course website
##########################################
# Splash Screen Mode
##########################################

def splashScreenMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, app.height/3, text='Monopoly',
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/2.5, 
                       text='Press y to start the game!',
                       font=font, fill='black')


def splashScreenMode_keyPressed(app, event):
    if event.key == 'y':
        app.mode = 'mapChooseMode'

# ##########################################
# # Map Choose Mode
# ##########################################

def mapChooseMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, app.height/8, 
                       text="Please press left and right key to choose the map",
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/5.7, 
                       text="Press 'y' to start the game!",
                       font=font, fill='black')
    mapChooseMode_drawBoard(app, canvas)


def mapChooseMode_keyPressed(app, event):

    if event.key == 'Left':
        app.index = max(1, app.index-1)
        
    elif event.key == 'Right':
        app.index = min(app.index+1, 4)
    
    if app.index == 1:
        app.myBoard = Board(board1)
    elif app.index == 2:
        app.myBoard = Board(board2)
    elif app.index == 3:
        app.myBoard = Board(board3)
    elif app.index == 4:
        app.myBoard = Board(board4)

    if event.key == 'y':
        app.mode = 'gameMode'
    


def mapChooseMode_drawBoard(app, canvas):
    rows, cols = app.myBoard.getDims()
    for row in range(rows):
        for col in range(cols):
            if app.myBoard.map[row][col] != 0:
                cx = app.gridWidth * col + app.width * 0.4
                cy = app.gridHeight * row
                placeGrid(app, canvas, cx, cy)

##########################################
# Game Mode
##########################################

def gameMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, 20, text='Game',
                       font=font, fill='black')
    x0Ins = app.width * 0.85
    y0Ins = app.height * 0.2
    x1Ins = app.width * 0.95
    y1Ins = app.height * 0.3
    
    canvas.create_oval(x0Ins, y0Ins, x1Ins, y1Ins, fill = 'white') # Instruction
    canvas.create_text(app.width * 0.8, app.height * 0.28, 
                       text = "Instruction", anchor = 'sw',
                       fill = 'black', font = font)

    x0Card = app.width * 0.85
    y0Card = app.height * 0.35
    x1Card = app.width * 0.95
    y1Card = app.height * 0.45
    canvas.create_oval(x0Card, y0Card, x1Card, y1Card, fill = 'white') # Special cards
    canvas.create_text(app.width * 0.845, app.height * 0.43, text = "Cards",
                       anchor = 'sw',
                       fill = 'black', font = font)
    gameMode_drawBoard(app, canvas)
    

def gameMode_mousePressed(app, event):
    x0Ins = app.width * 0.85
    y0Ins = app.height * 0.2
    x1Ins = app.width * 0.95
    y1Ins = app.height * 0.3
    x0Card = app.width * 0.85
    y0Card = app.height * 0.35
    x1Card = app.width * 0.95
    y1Card = app.height * 0.45
    # instruction page
    if x0Ins < event.x < x1Ins and y0Ins < event.y < y1Ins:
        app.mode = 'instructionMode'
    elif x0Card < event.x < x1Card and y0Card < event.y < y1Card:
        app.mode = 'specialCardsMode'
    

def draw_square(event):
    x0 = random.randint(30, 370)
    y0 = random.randint(30, 170)
    size = random.randint(10, 30)

    event.widget.create_rectangle(x0, y0, x0+size, y0+size, fill="red")

def gameMode_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'mapChooseMode'


###########
#draw map
###########
def twoDToIso(twoDx, twoDy):
    isoX = twoDx - twoDy
    isoY = (twoDx + twoDy) / 2
    return(isoX, isoY)

def gameMode_drawBoard(app, canvas):
    rows, cols = app.myBoard.getDims()
    for row in range(rows):
        for col in range(cols):
            if app.myBoard.map[row][col] != 0:
                cx = app.gridWidth * col + app.width * 0.4
                cy = app.gridHeight * row
                
                if app.myBoard.map[row][col].name == 'prison':
                    placePrisonGrid(app, canvas, cx, cy)
                elif app.myBoard.map[row][col].name == None:
                    placeNoneGrid(app, canvas, cx, cy)
                else:
                    placeGrid(app, canvas, cx, cy)

                
            


def placeGrid(app, canvas, cx, cy):
    twoDcx, twoDcy = twoDToIso(cx, cy)

    isox0, isoy0 = twoDcx, twoDcy - app.gridHeight/2
    isox1, isoy1 = twoDcx + app.gridWidth, twoDcy
    isox2, isoy2 = twoDcx, twoDcy + app.gridHeight/2
    isox3, isoy3 = twoDcx - app.gridWidth, twoDcy
    coord = isox0, isoy0, isox1, isoy1, isox2, isoy2, isox3, isoy3
    canvas.create_polygon(coord, fill='pink', outline='black')


def placePrisonGrid(app, canvas, cx, cy):
    twoDcx, twoDcy = twoDToIso(cx, cy)

    isox0, isoy0 = twoDcx, twoDcy - app.gridHeight/2
    isox1, isoy1 = twoDcx + app.gridWidth, twoDcy
    isox2, isoy2 = twoDcx, twoDcy + app.gridHeight/2
    isox3, isoy3 = twoDcx - app.gridWidth, twoDcy
    coord = isox0, isoy0, isox1, isoy1, isox2, isoy2, isox3, isoy3
    canvas.create_polygon(coord, fill='yellow', outline='black')

def placeNoneGrid(app, canvas, cx, cy):
    twoDcx, twoDcy = twoDToIso(cx, cy)

    isox0, isoy0 = twoDcx, twoDcy - app.gridHeight/2
    isox1, isoy1 = twoDcx + app.gridWidth, twoDcy
    isox2, isoy2 = twoDcx, twoDcy + app.gridHeight/2
    isox3, isoy3 = twoDcx - app.gridWidth, twoDcy
    coord = isox0, isoy0, isox1, isoy1, isox2, isoy2, isox3, isoy3
    canvas.create_polygon(coord, fill='purple', outline='black')

##########################################
# Instruction Mode
##########################################

def instructionMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, 200, text='This is the instruction!', 
                       font=font, fill='black')
    canvas.create_text(app.width/2, 300, text='Press r to return to the game!',
                       font=font, fill='black')

def instructionMode_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'gameMode'

##########################################
# Special cards Mode
##########################################

def specialCardsMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, 200, 
                       text='Here are all the special cards you have!', 
                       font=font, fill='black')
    canvas.create_text(app.width/2, 350, text='Press r to return to the game!',
                       font=font, fill='black')

def specialCardsMode_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'gameMode'


##########################################
# Main App
##########################################

def appStarted(app):
    app.mode = 'splashScreenMode'
    app.gridHeight = 23
    app.gridWidth = 23
    app.myBoard = Board(board1)
    app.index = 1
    app.npNameList = ['Acadia', 'American Samoa', 'Arches', 'Badlands', 'Big Bend',
            'Biscayne', 'Carlsbad Caverns', 'Crater Lake', 'Death Valley',
            'Dry Tortugas', 'Gates of the Arctic', 'Glacier Bay',
            'Great Smoky Mountains', 'Isle Royale', 'Joshua Tree',
            'Kings Canyon', 'Lake Clark', 'New River Gorge', 'North Cascades',
            'Petrified Forest', 'Redwood', 'Rocky Mountain', 'Saguaro',
            'Sequoia', 'Theodore Roosevelt', 'Voyageurs', 'Virgin Islands',
            'White Sands', 'Yellowstone', 'Zion']
    app.cpNameList = ['Royal Gorge Park', 'Falls Park', 'Scioto Audubon',
              'Rifle Mountain Park', 'Fairmount Park', 'City Park',
              'Zilker Park', 'The Gathering Place', 'Papago Park']
    app.functionPlaceList = ['prison']
    app.nonFunctionalPlaces = [None]
    app.nameList = (app.npNameList +
            app.functionPlaceList + app.nonFunctionalPlaces)

runApp(width=900, height=600)


# Please ignore the code below





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