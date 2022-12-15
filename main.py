from cmu_112_graphics import *

from classes import *

from helper import *

from mode import *


def gameMode_keyPressed(app, event):
    if app.askNewGame and event.key == 'y':
        appStarted(app)

    if ((app.instructionButton.enabled or app.cardsButton.enabled or
         app.propertiesButton.enabled) and event.key == 'Escape'):
        app.instructionButton.enabled = False
        app.cardsButton.enabled = False
        app.propertiesButton.enabled = False

    if ((app.askBuy or app.askUpgrade or app.askToPayToll 
         or app.askToUseJailCard) and 
        (type(app.dice) != str)):
        app.dice = ''
        app.lastPlayer = app.curPlayer
    if ((app.askBuy or app.askUpgrade or app.askToUseJailCard) and 
        (event.key == 'y' or event.key == 'n')):
        row, col = app.row, app.col
        if event.key == 'y':
            if ((app.myBoard.map[row][col] != 0) and 
                (app.myBoard.map[row][col] != 1) and
                (app.myBoard.map[row][col].name != None) and
                (app.myBoard.map[row][col].name != 'jail')): #eligible properties
                # buy 
                if app.askBuy:
                    app.curPlayer.buyProperty(app)
                    app.myBoard.map[row][col].buying(app.curPlayer)
                    app.askBuy = False
                elif app.askUpgrade:
                    app.curPlayer.upgradeProperty(app)
                    app.askUpgrade = False
                    app.myBoard.map[row][col].upgrading()
                    app.showSellButton = False
                    
        elif event.key == 'n':
            app.askBuy = False
            app.askUpgrade = False

        gameMode_changeTurn(app)

##########################################
# Main App
##########################################
        
def appStarted(app):
    app.mode = 'splashScreenMode'
    app.gridHeight = app.height*0.038
    app.gridWidth = app.height*0.038
    app.gridThickness = app.height*0.018
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

    app.askBuy = False
    app.askUpgrade = False
    app.askToPayToll = False
    app.payToll = False

    cxIns = app.width * 0.9
    cyIns = app.height * 0.25
    app.instructionButton = Button('Inst', (cxIns, cyIns))

    cxCards = app.width * 0.9
    cyCards = app.height * 0.4
    app.cardsButton = Button('Cards', (cxCards, cyCards))

    cxPro = app.width * 0.9
    cyPro = app.height * 0.55
    app.propertiesButton = Button('Properties', (cxPro, cyPro))
    
    cxSellButton = app.width*0.9
    cySellButton = app.height*0.7
    app.sellButton = Button('Sell', (cxSellButton, cySellButton))

    cxDieButton = app.width*0.9
    cyDieButton = app.height*0.89
    app.dieButton = Button('Throw a die', (cxDieButton, cyDieButton))

    cxNextButton = app.width*0.85
    cyNextButton = app.height*0.8
    app.nextButton = Button('Next', (cxNextButton, cyNextButton))


    app.displayChanceCards = False
    app.playChanceCards = False

    app.criminals = dict()
    app.bankrupcy = False
    app.bannedPlayerIndex = set()

    app.winner = False
    app.displayWinnerMsg = False

    app.askToUseJailCard = False
    app.isGameOver = False
    app.askNewGame = False
    # set up for save game state function
    app.boardDetailedInfo = dict()
    app.row = 0
    app.col = 0

    app.showSellButton = False
    app.sellProperty = False


def timerFired(app):
    if app.mode == 'gameMode':
        gameMode_timerFired(app)

runApp(width=900, height=600)