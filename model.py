class Tetromino:
    def __init__(self, name, tiles0, tiles90, tiles180, tiles270):
        self.name = name
        self.currentTiles = tiles0
        self.tiles = [
            tiles0,
            tiles90,
            tiles180,
            tiles270
        ]
        self.rotation = 0
    def rotateClockwise(self):
        newRotation = self.rotation + 90
        if newRotation == 360:
            newRotation = 0
        self.rotation = newRotation
        self.currentTiles = self.tiles[int(newRotation / 90)]
    def rotateCounterClockwise(self):
        newRotation = self.rotation - 90
        if newRotation == -90:
            newRotation = 0
        self.rotation = newRotation
        self.currentTiles = self.tiles[int(newRotation / 90)]
    def printTile(self):
        print('Name=' + self.name)
        print('Rotation=' + str(self.rotation))
        for x in range(4):
            for y in range(4):
                printed = False
                for p in self.currentTiles:
                    if p[0] == x and p[1] == y:
                        printed = True
                        print(self.name, end='')
                        break
                if (not printed):
                    print(' ', end='')
            print('')
        print('--------')

Tetrominos = [
    Tetromino('O',
        [[0,0],[0,1],[1,0],[1,1]], # 0
        [[0,0],[0,1],[1,0],[1,1]], # 90
        [[0,0],[0,1],[1,0],[1,1]], # 180
        [[0,0],[0,1],[1,0],[1,1]]  # 270
    ),
    Tetromino('I',
        [[0,0],[1,0],[2,0],[3,0]], # 0
        [[0,0],[0,1],[0,2],[0,3]], # 90
        [[0,0],[1,0],[2,0],[3,0]], # 180
        [[0,0],[0,1],[0,2],[0,3]]  # 270
    ),
    Tetromino('L',
        [[1,0],[1,1],[1,2],[0,2]], # 0
        [[0,0],[1,0],[2,0],[2,1]], # 90
        [[0,0],[1,0],[0,1],[0,2]], # 180
        [[0,1],[1,1],[2,1],[0,0]], # 270
    ),
    Tetromino('J',
        [[0,0],[0,1],[0,2],[1,2]], # 0
        [[2,0],[0,1],[1,1],[2,1]], # 90
        [[0,0],[1,0],[1,1],[1,2]], # 180
        [[0,0],[1,0],[2,0],[0,1]], # 270
    ),
    Tetromino('Z',
        [[1,0],[2,0],[0,1],[1,1]], # 0
        [[0,0],[0,1],[1,1],[1,2]], # 90
        [[1,0],[2,0],[0,1],[1,1]], # 180
        [[0,0],[0,1],[1,1],[1,2]], # 270
    ),
    Tetromino('S',
        [[0,0],[1,0],[1,1],[2,1]], # 0
        [[1,0],[0,1],[1,1],[0,2]], # 90
        [[0,0],[1,0],[1,1],[2,1]], # 180
        [[1,0],[0,1],[1,1],[0,2]], # 270
    ),
    Tetromino('T',
        [[0,0],[1,0],[2,0],[1,1]], # 0
        [[0,0],[0,1],[1,1],[0,2]], # 90
        [[1,0],[0,1],[1,1],[2,1]], # 180
        [[1,0],[0,1],[1,1],[1,2]], # 270
    ),
]

class Tile:
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.piece = piece

PieceTypes = [
    0, # Space
    1, # Stone
    2, # O
    3, # I
    4, # L
    5, # J
    6, # S
    7, # Z
    8, # T
]

class Piece:
    def __init__(self, type):
        self.type = type

from random import randrange
class Game:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.status = 'reset'
        self.points = 0
        self.time = 0
        self.tiles = []
        for x in range(width):
            for y in range(height):
                self.tiles.append(Tile(x, y, Piece(randrange(9))))
    def addPoints(self, points):
        self.points += points
    def moveTime(self):
        self.time += 1
        for i in range(len(self.tiles)):
            self.tiles[i] = Tile(self.tiles[i].x, self.tiles[i].y, Piece(randrange(9)))
    def reset(self):
        self.time = 0
        self.status = 'reset'
    def run(self):
        self.status = 'running'
