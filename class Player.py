#commit 
import random

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
factoryNameList = ['airport', 'airport', 'airport', 'airport', 'airport',
                   'airport', 'airport', 'airport', 'airport', 'airport',
                   'airport', 'airport', 'airport', 'airport', 'airport',
                   'airport', 'airport', 'airport', 'airport', 'airport']
nameList = npNameList + cpNameList + npUKNameList + factoryNameList

# print(len(nameList))
class Grid:
    def __init__(self):
        self.name = random.choice(nameList)
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
        
# g1 = Grid()
# print(f'before upgrade {g1.toll}, level = {g1.level}')
# g1.upgradeProperty()
# print(f'after upgrade {g1.toll}, level = {g1.level}')
# g1.upgradeProperty()
# print(f'after upgrade {g1.toll}, level = {g1.level}')
# g1.upgradeProperty()
# print(f'after upgrade {g1.toll}, level = {g1.level}')


# g1 = Grid()
# print(g1.name)
# print(nameList)





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
count = 0
for row in range(len(board1)):
    for col in range(len(board1[0])):
        if board1[row][col]:
            count += 1
# print(count)


board2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0.0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


board3 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0.0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

board4 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0.0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
                    detailedInfo[coord]['property name'] = grid.name
                    detailedInfo[coord]['price to buy'] = grid.priceToBuy
                    if grid.owner != None:
                        detailedInfo[coord]['owner'] = grid.owner
                        detailedInfo[coord]['cost to upgrade'] = (
                                                        grid.priceToUpgrade)
                        detailedInfo[coord]['toll'] = (grid.toll)
                    detailedInfo[coord]['owner'] = 'No Owner'
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
myBoard = Board(board1)  ## do not comment out
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
 
















player1 = Player("Xinyi")
# player2 = Player("Lynne")
print(player1.loc)
print(player1.myProperties)
print(f'my money = {player1.money}')

player1.buyProperty()
print(f'my money = {player1.money}')

player1.move(5)
player1.buyProperty()
print(f'my money = {player1.money}')
print(player1.myProperties)
row, col = player1.loc
print(f'the toll is {myBoard.map[row][col].toll}')

player1.upgradeProperty()
print(f'my money = {player1.money}')
row, col = player1.loc
print(f'the toll is {myBoard.map[row][col].toll}')

print(player1.sellProperty())
print(f'my money = {player1.money}')
row,col = player1.loc
print(f'the toll is {myBoard.map[row][col].toll}')
print(player1.myProperties)


# print(player1.ori)
# player1.move(5)
# print(player1.loc)
# # print(board1[5][1])
# print(myBoard.detailedInfo)