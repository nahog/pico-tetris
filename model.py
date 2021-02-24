class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tetromino:
    def __init__(self, type: int, tiles0, tiles90, tiles180, tiles270, x=0, y=0):
        self.type = type
        self.currentTiles = tiles0
        self.tiles = [
            tiles0,
            tiles90,
            tiles180,
            tiles270
        ]
        self.position = Point(x, y)
        self.rotation = 0
        self.transformed_tiles = []
        for i in range(len(self.currentTiles)):
            self.transformed_tiles.append([
                self.currentTiles[i][0] + self.position.x,
                self.currentTiles[i][1] + self.position.y
            ])
    def _update_transformed_tiles(self):
        for i in range(len(self.currentTiles)):
            self.transformed_tiles[i][0] = self.currentTiles[i][0] + self.position.x
            self.transformed_tiles[i][1] = self.currentTiles[i][1] + self.position.y
    def new_position(self, x, y):
        self.position.x = x
        self.position.y = y
        self._update_transformed_tiles()
    def move_time(self):
        self.position.x += 1
        self._update_transformed_tiles()
    def move_left(self, width, height):
        self.position.y -= 1
        self._update_transformed_tiles()
        if self.is_out_of_bounds(width, height):
            self.position.y += 1
            self._update_transformed_tiles()
    def move_right(self, width, height):
        self.position.y += 1
        self._update_transformed_tiles()
        if self.is_out_of_bounds(width, height):
            self.position.y -= 1
            self._update_transformed_tiles()
    def move_down(self, width, height):
        self.position.x += 1
        self._update_transformed_tiles()
        if self.is_out_of_bounds(width, height):
            self.position.x -= 1
            self._update_transformed_tiles()
    def can_move_time(self, width, height):
        self.position.x += 1
        self._update_transformed_tiles()
        result = self.is_out_of_bounds(width, height)
        self.position.x -= 1
        self._update_transformed_tiles()
        return not result
    def is_out_of_bounds(self, width, height):
        for i in range(len(self.transformed_tiles)):
            if self.transformed_tiles[i][0] >= width:
                return True
            if self.transformed_tiles[i][0] < 0:
                return True
            if self.transformed_tiles[i][1] >= height:
                return True
            if self.transformed_tiles[i][1] < 0:
                return True
        return False
    def in_position(self, x, y):
        for i in range(len(self.transformed_tiles)):
            if self.transformed_tiles[i][0] == x and self.transformed_tiles[i][1] == y:
                return True
        return False
    def rotate(self, width, height):
        self._rotate_clockwise()
        if self.is_out_of_bounds(width, height):
            self._rotate_counter_clockwise()
    def _rotate_clockwise(self):
        newRotation = self.rotation + 90
        if newRotation == 360:
            newRotation = 0
        self.rotation = newRotation
        self.currentTiles = self.tiles[int(newRotation / 90)]
        self._update_transformed_tiles()
    def _rotate_counter_clockwise(self):
        newRotation = self.rotation - 90
        if newRotation == -90:
            newRotation = 0
        self.rotation = newRotation
        self.currentTiles = self.tiles[int(newRotation / 90)]
        self._update_transformed_tiles()

Tetrominos = [
    Tetromino(2, # 'O',
        [[0,0],[0,1],[1,0],[1,1]], # 0
        [[0,0],[0,1],[1,0],[1,1]], # 90
        [[0,0],[0,1],[1,0],[1,1]], # 180
        [[0,0],[0,1],[1,0],[1,1]]  # 270
    ),
    Tetromino(3, # 'I',
        [[0,0],[1,0],[2,0],[3,0]], # 0
        [[0,0],[0,1],[0,2],[0,3]], # 90
        [[0,0],[1,0],[2,0],[3,0]], # 180
        [[0,0],[0,1],[0,2],[0,3]]  # 270
    ),
    Tetromino(4, # 'L',
        [[1,0],[1,1],[1,2],[0,2]], # 0
        [[0,0],[1,0],[2,0],[2,1]], # 90
        [[0,0],[1,0],[0,1],[0,2]], # 180
        [[0,1],[1,1],[2,1],[0,0]], # 270
    ),
    Tetromino(5, # 'J',
        [[0,0],[0,1],[0,2],[1,2]], # 0
        [[2,0],[0,1],[1,1],[2,1]], # 90
        [[0,0],[1,0],[1,1],[1,2]], # 180
        [[0,0],[1,0],[2,0],[0,1]], # 270
    ),
    Tetromino(6, # 'Z',
        [[1,0],[2,0],[0,1],[1,1]], # 0
        [[0,0],[0,1],[1,1],[1,2]], # 90
        [[1,0],[2,0],[0,1],[1,1]], # 180
        [[0,0],[0,1],[1,1],[1,2]], # 270
    ),
    Tetromino(7, # 'S',
        [[0,0],[1,0],[1,1],[2,1]], # 0
        [[1,0],[0,1],[1,1],[0,2]], # 90
        [[0,0],[1,0],[1,1],[2,1]], # 180
        [[1,0],[0,1],[1,1],[0,2]], # 270
    ),
    Tetromino(8, # 'T',
        [[0,0],[1,0],[2,0],[1,1]], # 0
        [[0,0],[0,1],[1,1],[0,2]], # 90
        [[1,0],[0,1],[1,1],[2,1]], # 180
        [[1,0],[0,1],[1,1],[1,2]], # 270
    ),
]

PieceTypes = [
    0, # Space
    1, # Stone
    2, # O
    3, # I
    4, # L
    5, # J
    6, # Z
    7, # S
    8, # T
]

class Piece:
    def __init__(self, type: int):
        self.type = type

class Tile:
    def __init__(self, x: int, y: int, piece: Piece, fixed=False):
        self.x = x
        self.y = y
        self.piece = piece
        self.fixed = fixed

from random import randrange
class Game:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self._init()
    def _init(self):
        self.status = 'reset'
        self.points = 0
        self.level = 1
        self.level_speed = 1.0
        self.time = 0
        self.move_time = 0
        self.tiles = []
        self.changed_tiles = []
        self.fixed_tiles = []
        for x in range(self.width):
            self.tiles.append([])
            self.fixed_tiles.append([])
            for y in range(self.height):
                self.tiles[x].append(Tile(x, y, Piece(0)))
                self.changed_tiles.append(Tile(x, y, Piece(0)))
                self.fixed_tiles[x].append(None)
        self._create_next_piece()
    def _create_next_piece(self):
        next_tetronimo = Tetrominos[randrange(len(Tetrominos))]
        next_tetronimo.new_position(0, 4)
        self._active_tetronimo = next_tetronimo
    def move_left(self):
        self._active_tetronimo.move_left(self.width, self.height)
    def next_level(self):
        self.level_speed -= 0.1
        if self.level_speed < 0.3:
            self.level_speed = 0.3
    def move_right(self):
        self._active_tetronimo.move_right(self.width, self.height)
    def move_down(self):
        self._active_tetronimo.move_down(self.width, self.height)
    def rotate(self):
        self._active_tetronimo.rotate(self.width, self.height)
    def move_game(self, delta_time):
        self.time += delta_time
        self.move_time += delta_time
        if self.move_time > self.level_speed:
            self.move_time = self.move_time % self.level_speed
            if not self._active_tetronimo.can_move_time(self.width, self.height):
                for tile in self._active_tetronimo.transformed_tiles:
                    self.fixed_tiles[tile[0]][tile[1]] = Tile(tile[0], tile[1], Piece(self._active_tetronimo.type))
                self._create_next_piece()
            else:
                self._active_tetronimo.move_time()
            for x in range(self.width):
                for y in range(self.height):
                    piece = Piece(0)
                    if self.fixed_tiles[x][y] != None:
                        piece = self.fixed_tiles[x][y].piece
                    if self._active_tetronimo.in_position(x, y):
                        piece = Piece(self._active_tetronimo.type)
                    self.tiles[x][y] = Tile(self.tiles[x][y].x, self.tiles[x][y].y, piece)
            postition = self._active_tetronimo.position
            init_x = postition.x - 1 if postition.x - 1 > 0 else 0
            init_y = postition.y - 1 if postition.y - 1 > 0 else 0
            limit_x = postition.x + 4 if postition.x + 4 < self.width else self.width
            limit_y = postition.y + 4 if postition.y + 4 < self.height else self.height
            self.changed_tiles.clear()
            for x in range(init_x, limit_x):
                for y in range(init_y, limit_y):
                    self.changed_tiles.append(self.tiles[x][y])
    def reset(self):
        self._init()
    def run(self, delta_time):
        self.status = 'running'
        self.move_game(delta_time)
