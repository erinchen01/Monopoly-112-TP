from cmu_112_graphics import *

from classes import *

from helper import *

from mode import *

import random, tkinter, time, decimal



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
    # app.openInstruction = False
    

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

    cxDieButton = app.width*0.9
    cyDieButton = app.height*0.89
    app.dieButton = Button('Throw a die', (cxDieButton, cyDieButton))

    app.displayChanceCards = False
    app.playChanceCards = False

    app.criminals = dict()
    app.bankrupcy = False
    app.bannedPlayerIndex = set()

    app.winner = False
    app.displayWinnerMsg = False

    app.askToUseJailCard = False




def timerFired(app):
    if app.mode == 'gameMode':
        gameMode_timerFired(app)


runApp(width=900, height=600)