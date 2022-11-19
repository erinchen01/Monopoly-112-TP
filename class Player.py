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
nameList = npNameList + cpNameList

# print(len(nameList))
class Grid:
    def __init__(self):
        self.name = random.choice(nameList)
        nameList.remove(self.name)
        self.owner = []
        self.priceToBuy = random.randint(3000, 6000)
        self.priceToUpgrade = 0.4 * self.priceToBuy
        
        self.level = 0
        self.toll = int(random.randint(2, 5) * 0.1 * self.priceToBuy)
        self.priceToSell = self.priceToBuy * 0.7
    
    def buyProperty(self, player):
        self.owner = player
        self.level = 1
    
    def upgradeProperty(self):
        self.level += 1
        index = random.randint(2, 6)
        self.toll = (self.toll + 
                     int(index * 0.1 * self.priceToBuy))
        
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
myBoard = Board(board1)
# print(myBoard.getRandomPlace())


# dice = random.randint(1, 6)

class Player:
    def __init__(self):
        self.loc = myBoard.getRandomPlace()
        self.cards = []
        self.myTurn = False
        self.myProperties = []
        self.money = 50000
        self.ori = self.checkOri()
 
    def isLegalMove(self, checkingMove):
        # print(f'self.loc = {self.loc}')
        curLocRow, curLocCol = self.loc
        dRow, dCol = checkingMove
        boardRows, boardCols = myBoard.getDims()
        if ((0 <= curLocRow + dRow < boardRows) and 
            (0 <= curLocCol + dCol < boardCols) and
            (myBoard.map[curLocRow + dRow][curLocCol + dCol] == 1)):
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
        # dx, dy = self.ori
        for i in range(dice):
            if not self.isLegalMove(self.ori):
                self.changeOri()
            curLocRow += self.ori[0]
            curLocCol += self.ori[1]
            self.loc = curLocRow, curLocCol
    
    def changeMyTurn(self):
        self.myTurn = True
        
    def buyProperty(self, grid):
        self.owner = self
        self.level = 1
        self.myProperties.append(grid)

    def upgradeProperty(self, grid):
        if self.money < grid.priceToUpgrade:
            return "No enough money to upgrade!"
        if self.money >= grid.priceToUpgrade:
            return "Successfully upgraded the property."

    def sellProperty(self, grid):
        self.money += grid.priceToSell
        self.property.remove(grid)
        return f"Successfully sold {grid.name}.\
                 Now you have {self.money} dollars left."
 
player1 = Player()
print(player1.loc)
print(player1.ori)
player1.move(5)
# print(board1[5][1])