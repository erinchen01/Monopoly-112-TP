from cmu_112_graphics import *

import random, tkinter, time, decimal


class Button:
    def __init__(self, buttonName, coord):
        self.name = buttonName
        self.enabled = False
        self.coord = coord
    
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
        # self.ori = (0, -1)
        # self.color = random.choice(colors)
        # colors.remove(self.color)
        self.playerName = playerName
        self.color = color
    
    
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
        # # modify the params of players
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

    def payToll(self, app):
        row, col = self.loc
        grid = app.myBoard.map[row][col]
        # toll = app.boardDetailedInfo[coord]['toll']
        toll = grid.toll
        self.money -= toll
        owner = grid.owner
        # owner = app.boardDetailedInfo[coord]['owner']
        owner.money += toll


        


##########################################
# Splash Screen Mode
##########################################

def splashScreenMode_redrawAll(app, canvas):
    font = 'Baloo 28'
    canvas.create_text(app.width/2, app.height/3, text='Monopoly!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/2.5, 
                       text='Press y to start a new game',
                       font=font, fill='black')


def splashScreenMode_keyPressed(app, event):
    if event.key == 'y':
        app.mode = 'playerSettingMode'

    
# ##########################################
# # Player setting Mode
# ##########################################

def playerSettingMode_redrawAll(app, canvas):
    font = font = 'Baloo 28'
    
    canvas.create_text(app.width/2, app.height/8, 
                       text=app.message,
                       font=font, fill='black')
    canvas.create_text(app.width/7, app.height/8, 
                       text=f"Player number: {app.playerNum}",
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/2, 
                       text=f"Press 'y' to start the game!",
                       font=font, fill='black')


def playerSettingMode_mousePressed(app, event):
    pass
        

def playerSettingMode_keyPressed(app, event):
    if event.key == 'y':
        if app.playerNum < 2:
            app.message = "Please add at least\n      two players."
        else:
            app.mode = 'mapChooseMode'
    else:
        name = app.getUserInput('Please enter your name:)')
        if name == '':
            app.message = 'Please type in a name.'
        else:
            if app.playerNum < 4:
                if name != None:
                    app.playerNum += 1
                    app.message = 'Successfully add a player'
                    app.playerNameList.append(name)
            if app.playerNum == 4:
                    app.message = '''
                        Has reached the maximum of players. 
                        Let's start the game!
                    '''

    

# ##########################################
# # Map Choose Mode
# ##########################################

def mapChooseMode_redrawAll(app, canvas):
    font = 'Baloo 28'
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
        # set players
        for playerName in app.playerNameList:
            colors = ['blue', 'red', 'yellow', 'green']
            color = random.choice(colors)
            player = Player(playerName, color)
            app.playerInfo[player] = dict()

            loc = app.myBoard.getRandomPlace() #returns a tuple
            player.loc = loc
            
            app.playerInfo[player]["loc"] = player.loc
            app.playerInfo[player]["myTurn"] = player.myTurn
            app.playerInfo[player]["color"] = player.color
            ori = player.checkOri(app)
            player.ori = ori
        app.playerInfoKeysList = list(app.playerInfo)
        app.curPlayer = app.playerInfoKeysList[app.curPlayerIndex-1] #app.playerNameList[0]
        app.whoseTurn = app.curPlayer
        
        # set grids in Board
        makeDetailedInfo(app)

        # modify app mode
        app.mode = 'gameMode'


def makeDetailedInfo(app): #modify app.boardDetailedInfo

    nameList = ['Peak District', 'Lake District', 'Snowdonia', 'Dartmoor',
                'Pembrokeshire Coast', 'North York Moors','Yorkshire Dales',
                'Exmoor', 'Northumberland', 'Brecon Beacons', 'The Broads',
                'Cairngorms', 'New Forest', 'South Downs',
                'Royal Gorge Park', 'Falls Park', 'Scioto Audubon',
                'Rifle Mountain Park', 'Fairmount Park', 'City Park',
                'Zilker Park', 'The Gathering Place', 'Papago Park']
    index = 0
    app.boardDetailedInfo = dict()
    rows, cols = app.myBoard.getDims()
    for row in range(rows):
        for col in range(cols):
            coord = (row, col)
            if app.myBoard.map[row][col] != 0:
                if index == 7:
                    gridName = 'prison'
                    app.boardDetailedInfo[coord] = gridName
                    app.myBoard.map[row][col] = Grid(gridName, 0)
                elif 0 < index % 7 % 4 <= 4:
                    gridName = None
                    gridPriceToBuy = 0
                    app.boardDetailedInfo[coord] = None
                else:
                    gridName = random.choice(nameList)
                    gridPriceToBuy = random.randint(3000, 6000)
                    app.boardDetailedInfo[coord] = dict()
                    app.myBoard.map[row][col] = Grid(gridName, gridPriceToBuy) #####
                    grid = app.myBoard.map[row][col]
                if (gridName is not None) and (gridName is not 'prison'):
                        nameList.remove(gridName)
                        app.boardDetailedInfo[coord]['property name'] = gridName
                        app.boardDetailedInfo[coord]['price to buy'] = (
                                                                gridPriceToBuy)
                        app.boardDetailedInfo[coord]['owner'] = 'No Owner'
                        if grid.owner != None:
                            app.boardDetailedInfo[coord]['owner'] = grid.owner
                            app.boardDetailedInfo[coord]['cost to upgrade'] = (
                                                            grid.priceToUpgrade)
                            app.boardDetailedInfo[coord]['toll'] = (grid.toll)
                index += 1

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
    font = 'Baloo 24'
    canvas.create_text(app.width/2, 20, text='Game',
                       font=font, fill='black')
    x0Ins = app.width * 0.85
    y0Ins = app.height * 0.2
    x1Ins = app.width * 0.95
    y1Ins = app.height * 0.3
    
    canvas.create_oval(x0Ins, y0Ins, x1Ins, y1Ins,
                       fill='#FFC125', outline='#FFC125') # Instruction
    canvas.create_text(app.width * 0.83, app.height * 0.28, 
                       text="Instruction", anchor='sw',
                       fill='black', font=font)

    x0Card = app.width * 0.85
    y0Card = app.height * 0.35
    x1Card = app.width * 0.95
    y1Card = app.height * 0.45
    canvas.create_oval(x0Card, y0Card, x1Card, y1Card, 
                       fill='#FFC125', outline='#FFC125') # Special cards
    canvas.create_text(app.width * 0.865, app.height * 0.43, text = "Cards",
                       anchor = 'sw',
                       fill = 'black', font=font)
    gameMode_drawBoard(app, canvas)
    gameMode_drawPlayer(app, canvas)
    
    # msg of rolling dice
    if type(app.dice) != str:
        canvas.create_text(app.width/2, 45, text=f"You rolled {app.dice}.",
                           font=font, fill='blue')
    
    if app.clickGrid == True:
        gameMode_drawGridInfo(app, canvas)

    if app.openInstruction == True:
        gameMode_drawInstruction(app, canvas)
    
    if app.askBuy == True:
        gameMode_askBuy(app, canvas)
    elif app.askUpgrade == True:
        gameMode_askUpgrade(app, canvas)
    elif app.askToPayToll == True:
        gameMode_askToPayToll(app, canvas)
    
    gameMode_drawMoneyAndPropertyCoin(app, canvas)
    canvas.create_text(app.width/2, app.height*0.75, 
                       text=f"Press 'r' to roll a dice.",
                       font=font, fill='black')
    gameMode_drawDice(app, canvas)

def gameMode_askBuy(app, canvas):
    text = 'Do you want to buy the land?'
    font = 'Baloo 15'
    canvas.create_text(app.width/2, app.height/3, text=text, font=font)


def gameMode_askUpgrade(app, canvas):
    text = 'Do you want to upgrade the land?'
    font = 'Baloo 15'
    canvas.create_text(app.width/2, app.height/3, text=text, font=font)

def gameMode_askToPayToll(app, canvas):
    row, col = app.curPlayer.loc
    grid = app.myBoard.map[row][col]
    pOwner = grid.owner
    text = f'''
Bad luck:(
You visited {pOwner}'s property - {grid.name} and have to 
pay a ${grid.toll} toll.
    '''
    font = 'Baloo 15'
    canvas.create_text(app.width/2, app.height/3, text=text, font=font)

    tollText = f'-         {grid.toll}'
    cx = app.width*0.64
    cy = app.height*0.283
    rCoin = app.width * 0.009
    x0, x1 = cx - rCoin, cx + rCoin
    y0, y1 = cy - rCoin, cy + rCoin
    canvas.create_oval(x0, y0, x1, y1, fill='#FFC125', outline='#FFC125')
    canvas.create_text(cx, cy, text='$', fill='#8B5742', font=font)
    canvas.create_text(app.width*0.66, cy, 
                       text=tollText, font='Arial 13 bold', fill='#8B5742')

def gameMode_drawMoneyAndPropertyCoin(app, canvas):
    
    # money coin
    for indexOfPlayer in range(len(app.playerInfoKeysList)):
        text = '$'
        font = 'Arial 10'
        cx = app.width*(indexOfPlayer+1)/4 - app.width/4*0.5
        cy = app.height*0.25*0.4*0.5
        rCoin = app.width * 0.009
        x0, x1 = cx - rCoin, cx + rCoin
        y0, y1 = cy - rCoin, cy + rCoin
        canvas.create_oval(x0, y0, x1, y1, fill='#FFC125', outline='#FFC125')
        canvas.create_text(cx, cy, text=text, fill='#8B5742', font=font)

        money = app.playerInfoKeysList[indexOfPlayer].money
        cxM = cx + rCoin * 4
        cyM = cy
        canvas.create_text(cxM, cyM, text=money, font=font)
    
    # property coin
    for indexOfPlayer in range(len(app.playerInfoKeysList)):
        text = 'P'
        font = 'Arial 10'
        cx = app.width*(indexOfPlayer+1)/4 - app.width/4*0.5
        cy = (app.height*0.25*0.4*0.5)*1.8
        rCoin = app.width * 0.009
        x0, x1 = cx - rCoin, cx + rCoin
        y0, y1 = cy - rCoin, cy + rCoin
        canvas.create_oval(x0, y0, x1, y1, fill='#FFC125', outline='#FFC125')
        canvas.create_text(cx, cy, text=text, fill='#8B5742', font=font)

        cxP = cx + rCoin * 4
        cyP = cy 
        property = len(app.playerInfoKeysList[indexOfPlayer].myProperties)
        canvas.create_text(cxP, cyP, text=property, font=font)
    
    # playerName
    for indexOfPlayer in range(len(app.playerInfoKeysList)):
        font = 'Arial 15'
        player = app.playerInfoKeysList[indexOfPlayer]
        cx = app.width*(indexOfPlayer+1)/4 - app.width*0.18
        cy = (app.height*0.25*0.4*0.5)*1.3
        if player == app.curPlayer:
            canvas.create_text(cx, cy, text=player, font=font, fill='blue')
        else:
            canvas.create_text(cx, cy, text=player, font=font)


def gameMode_drawDice(app, canvas):
    x0S, x1S = app.width*0.87 - app.width*0.03, app.width*0.87 + app.width*0.03
    y0S, y1S = app.height*0.85 - app.width*0.03, app.height*0.85 + app.width*0.03
    canvas.create_rectangle(x0S, y0S, x1S, y1S, outline='#FDC669', width=4.5)

    p01 = x0S, y0S
    p02 = x1S, y0S
    p03 = x0S + app.width*0.0182, y0S - app.width*0.0182
    p04 = x1S + app.width*0.0182, y0S - app.width*0.0182
    canvas.create_polygon(p01, p02, p04, p03, 
                          outline='#FDC669', fill='white', width=4.5)
    
    p11 = p04
    p12 = p02
    p13 = x1S, y1S
    p14 = x1S + app.width*0.0182, y1S - + app.width*0.0182
    canvas.create_polygon(p11, p12, p13, p14,
                          outline='#FDC669', fill='white', width=4.5)
    
def gameMode_mousePressed(app, event):
    # instruction page and special cards mode
    # x0Ins = app.width * 0.85
    # y0Ins = app.height * 0.2
    # x1Ins = app.width * 0.95
    # y1Ins = app.height * 0.3
    cxIns = app.width * 0.9
    cyIns = app.height * 0.25

    # x0Card = app.width * 0.85
    # y0Card = app.height * 0.35
    # x1Card = app.width * 0.95
    # y1Card = app.height * 0.45
    cxCards = app.width * 0.9
    cyCards = app.height * 0.4
    instructionButton = Button('Inst', (cxIns, cyIns))
    x0Ins, y0Ins, x1Ins, y1Ins = instructionButton.getCoords(app)

    cardsButton = Button('Cards', (cxCards, cyCards))
    x0Cards, y0Cards, x1Cards, y1Cards = cardsButton.getCoords(app)

    if ((app.openInstruction == False) and 
        (x0Ins < event.x < x1Ins) and 
        (y0Ins < event.y < y1Ins)):
        app.openInstruction = True
    elif x0Cards < event.x < x1Cards and y0Cards < event.y < y1Cards:
        app.mode = 'specialCardsMode'

    # click grids
    Isox, Isoy = event.x, event.y
    twoDx, twoDy = isoToTwoD(Isox, Isoy)
    col = roundHalfUp((twoDx - app.width * 0.4) / app.gridWidth)
    row = roundHalfUp(twoDy / app.gridHeight)
    app.clickTime = time.time()

    if (((row, col) in app.boardDetailedInfo) and 
        (app.boardDetailedInfo[(row, col)] != None)):
        app.clickGrid = True
        app.gridInfo = app.boardDetailedInfo[(row, col)]
        app.gridClicked = (row, col)

    
def gameMode_timerFired(app):
    if (app.clickGrid == True) and (time.time() - app.clickTime > 2):
        app.clickGrid = False
    updateDetailedInfoDict(app)
    if app.payToll:
        app.curPlayer.payToll(app)
        app.payToll = False

    if (app.askToPayToll) and (time.time() - app.startToAskForToll > 5):
        app.askToPayToll = False
    
    
    
        
        
def gameMode_drawGridInfo(app, canvas):
    row, col = app.gridClicked
    gridcx, gridcy = app.gridWidth * col + app.width * 0.4, app.gridHeight * row
    gridIsocx, gridIsocy = twoDToIso(gridcx, gridcy)
    x0, y0 = gridIsocx - app.width * 0.07, gridIsocy - app.height * 0.14
    x1, y1 = gridIsocx + app.width * 0.07, gridIsocy - app.height * 0.02
    canvas.create_rectangle(x0, y0, x1, y1, fill = '#FFEC8B')


    font = 'Arial 9'
    text = ''
    for key in app.gridInfo:
        if key == 'property name':
            text += f'{key} :\n{app.gridInfo[key]}\n'
        else:
            text += f'{key} : {app.gridInfo[key]}\n'
    canvas.create_text(gridIsocx, (y1+y0)/2, 
                           text=text, font=font, fill='#8B3A3A')


def gameMode_drawPlayer(app, canvas):
    
    for eachPlayer in app.playerInfo:     
        loc = app.playerInfo[eachPlayer]['loc'] #returns a tuple
        twoDRow, twoDCol = loc[0], loc[1]
        cx = app.gridWidth * twoDCol + app.width * 0.4
        cy = app.gridHeight * twoDRow
        isoX, isoY = twoDToIso(cx, cy)
        playerRadius = 9
        x0 = isoX - playerRadius
        y0 = isoY - playerRadius
        x1 = isoX + playerRadius
        y1 = isoY + playerRadius
        canvas.create_oval(x0, y0, x1, y1, fill=eachPlayer.color)

def gameMode_keyPressed(app, event):
    if app.openInstruction == True and event.key == 'Escape':
        app.openInstruction = False


    if ((not app.payToll) and
        (not app.askToPayToll) and
        (not app.askBuy) and 
        (not app.askUpgrade) and 
        (not app.openInstruction)):
        if event.key == 'r': # A player rolled the dice
            # after A rolled the dice, current turn changes
            app.dice = app.curPlayer.playDice()
            app.curPlayer.move(app, app.dice)
            
            row, col = app.curPlayer.loc
            app.row, app.col = row, col
            
            if (app.boardDetailedInfo[(row, col)] != None and
                app.myBoard.map[row][col].name != 'prison'):
                if app.boardDetailedInfo[(row, col)]['owner'] == None:
                    app.askBuy = True
                elif app.boardDetailedInfo[(row, col)]['owner'] == app.curPlayer:
                    app.askUpgrade = True
                elif app.boardDetailedInfo[(row, col)]['owner'] != app.curPlayer:
                    app.startToAskForToll = time.time()
                    app.askToPayToll = True
                    app.payToll = True
            
            if ((not app.askBuy) and 
                (not app.askUpgrade) and 
                (not app.askToPayToll) and
                (not app.payToll)):
                app.curPlayerIndex = (app.curPlayerIndex + 1) % app.playerNum
                app.curPlayer.myTurn = 'False'
                nextPlayer = app.playerInfoKeysList[app.curPlayerIndex-1]
                app.curPlayer = nextPlayer
                app.curPlayer.myTurn = 'True'
                app.whoseTurn = nextPlayer

        
    if ((app.askBuy or app.askUpgrade) and 
        (event.key == 'y' or event.key == 'n')):
        row, col = app.row, app.col
        if event.key == 'y':
            if ((app.myBoard.map[row][col] != 0) and 
                (app.myBoard.map[row][col] != 1) and
                (app.myBoard.map[row][col].name != None) and
                (app.myBoard.map[row][col].name != 'prison')): #eligible properties
                # buy 
                if app.askBuy:
                    # curRow, curCol = app.playerInfo[app.curPlayer]['loc']
                    # print('want to buy')
                    app.curPlayer.buyProperty(app)
                    app.myBoard.map[row][col].buying(app.curPlayer)
                    app.askBuy = False
                elif app.askUpgrade:
                    app.curPlayer.upgradeProperty(app)
                    app.askUpgrade = False
                    # grid upgrade()
        elif event.key == 'n':
            app.askBuy = False
            app.askUpgrade = False

        app.curPlayerIndex = (app.curPlayerIndex + 1) % app.playerNum
        app.curPlayer.myTurn = 'False'
        nextPlayer = app.playerInfoKeysList[app.curPlayerIndex-1]
        app.curPlayer = nextPlayer
        app.curPlayer.myTurn = 'True'
        app.whoseTurn = nextPlayer
        
    

       

def updateDetailedInfoDict(app):
    rows, cols = app.myBoard.getDims()
    for row in range(rows):
        for col in range(cols):
            if (isinstance(app.myBoard.map[row][col], Grid) and 
                app.myBoard.map[row][col] != 1 and 
                app.myBoard.map[row][col].name != 'prison'):
                # print(app.myBoard.map[row][col])

                grid = app.myBoard.map[row][col]
                coord = (row, col)
                # print(app.boardDetailedInfo[coord])
                app.boardDetailedInfo[coord]['price to buy'] = grid.priceToBuy
                app.boardDetailedInfo[coord]['owner'] = grid.owner
                app.boardDetailedInfo[coord]['cost to upgrade'] = (
                grid.priceToUpgrade)
                app.boardDetailedInfo[coord]['toll'] = grid.toll


###########
#draw map
###########
# the concept of the calculation of isometric x and y is from 
# https://gamedevelopment.tutsplus.com/tutorials/
# creating-isometric-worlds-a-primer-for-game-developers--gamedev-6511
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
                
                if app.boardDetailedInfo[(row, col)] == 'prison':
                    placePrisonGrid(app, canvas, cx, cy)
                elif app.boardDetailedInfo[(row, col)] == None:
                    placeNoneGrid(app, canvas, cx, cy)
                else:
                    placeGrid(app, canvas, cx, cy)
                    

def placeGrid(app, canvas, cx, cy):
    Isocx, Isocy = twoDToIso(cx, cy)

    isox0, isoy0 = Isocx, Isocy - app.gridHeight/2
    isox1, isoy1 = Isocx + app.gridWidth, Isocy
    isox2, isoy2 = Isocx, Isocy + app.gridHeight/2
    isox3, isoy3 = Isocx - app.gridWidth, Isocy
    coord = isox0, isoy0, isox1, isoy1, isox2, isoy2, isox3, isoy3
    canvas.create_polygon(coord, fill='#BFEFFF', outline='black')


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
    canvas.create_polygon(coord, fill='#8B8970', outline='black')



###########
#click map
###########
# the concept of the calculation of twoD x and twoD y is from 
# https://gamedevelopment.tutsplus.com/tutorials/
# creating-isometric-worlds-a-primer-for-game-developers--gamedev-6511
def isoToTwoD(isoX, isoY):
    twoDx = (2 * isoY + isoX) / 2
    twoDy = (2 * isoY - isoX) / 2
    return twoDx, twoDy

##################
# Instruction Canvas
##################

def gameMode_drawInstruction(app, canvas):
    x0, y0 = app.width * 0.2, app.height * 0.2
    x1, y1 = app.width * 0.8, app.height * 0.8
    canvas.create_rectangle(x0, y0, x1, y1, fill='#FFC125', outline='#FFC125')

##########################################
# Special cards Mode
##########################################

def specialCardsMode_redrawAll(app, canvas):
    font = 'Baloo 28'
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
    app.playerNum = 0
    app.message = 'Press any key to add a player!'
    app.playerNameList = list()
    app.playerInfo = dict()
    app.curPlayerIndex = 1

    app.dice = 'Please roll the dice.'
    app.gridInfo = None
    app.clickGrid = False # keep track of whether the player clicked grids
    app.wantToReturn = False
    app.openInstruction = False

    app.askBuy = False
    app.askUpgrade = False
    app.askToPayToll = False
    app.payToll = False


def timerFired(app):
    if app.mode == 'gameMode':
        gameMode_timerFired(app)


runApp(width=900, height=600)
