class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tetromino:
    def __init__(self, type: int, tiles0, tiles90, tiles180, tiles270, x=0, y=0):
        self.type = type
        self.current_tiles = tiles0
        self.tiles = [
            tiles0,
            tiles90,
            tiles180,
            tiles270
        ]
        self.position = Point(x, y)
        self.rotation = 0
        self.transformed_tiles = []
        for i in range(len(self.current_tiles)):
            self.transformed_tiles.append([
                self.current_tiles[i][0] + self.position.x,
                self.current_tiles[i][1] + self.position.y
            ])
    def _update_transformed_tiles(self):
        for i in range(len(self.current_tiles)):
            self.transformed_tiles[i][0] = self.current_tiles[i][0] + self.position.x
            self.transformed_tiles[i][1] = self.current_tiles[i][1] + self.position.y
    def new_position(self, x, y):
        self.position.x = x
        self.position.y = y
        self._update_transformed_tiles()
    def revert_time(self):
        self.position.x -= 1
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
        new_rotation = self.rotation + 90
        if new_rotation == 360:
            new_rotation = 0
        self.rotation = new_rotation
        self.current_tiles = self.tiles[int(new_rotation / 90)]
        self._update_transformed_tiles()
    def _rotate_counter_clockwise(self):
        new_rotation = self.rotation - 90
        if new_rotation == -90:
            new_rotation = 0
        self.rotation = new_rotation
        self.current_tiles = self.tiles[int(new_rotation / 90)]
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
        self.level_speed = 300.0
        self.level_step = 50
        self.level_max_speed = 100
        self.time = 0
        self.move_time = 0
        self.tiles = []
        self.changed_tiles = []
        self.fixed_tiles = []
        self.next_tetronimo = Tetrominos[randrange(len(Tetrominos))]
        self._move_left_triggered = False
        self._move_right_triggered = False
        self._move_down_triggered = False
        self._create_next_piece()
        for x in range(self.width):
            self.tiles.append([])
            self.fixed_tiles.append([])
            for y in range(self.height):
                self.tiles[x].append(Tile(x, y, Piece(0)))
                self.changed_tiles.append(Tile(x, y, Piece(0)))
                self.fixed_tiles[x].append(None)
        self._create_next_piece()
    def _create_next_piece(self):
        self.next_tetronimo.new_position(0, 4)
        self._active_tetronimo = self.next_tetronimo
        self.next_tetronimo = Tetrominos[randrange(len(Tetrominos))]
    def next_level(self):
        self.level_speed -= 0.1
        if self.level_speed < 0.3:
            self.level_speed = 0.3
        self.level += 1
    def _process_move_triggers(self):
        if self._move_right_triggered:
            self._active_tetronimo.move_right(self.width, self.height)
            self._move_right_triggered = False
        if self._move_left_triggered:
            self._active_tetronimo.move_left(self.width, self.height)
            self._move_left_triggered = False
        if self._move_down_triggered:
            self._active_tetronimo.move_down(self.width, self.height)
            self._move_down_triggered = False
    def move_left(self):
        if not self._move_left_triggered:
            self._move_left_triggered = True
    def move_right(self):
        if not self._move_right_triggered:
            self._move_right_triggered = True
    def move_down(self):
        if not self._move_down_triggered:
            self._move_down_triggered = True
    def rotate(self):
        self._active_tetronimo.rotate(self.width, self.height)
    def move_game(self, delta_time):
        self.time += delta_time
        self.move_time += delta_time
        if self.move_time > self.level_speed:
            self.move_time = self.move_time % self.level_speed
            self._process_move_triggers()
            if self._has_collision(self._active_tetronimo.transformed_tiles):
                self._active_tetronimo.revert_time()
                for tile in self._active_tetronimo.transformed_tiles:
                    self.fixed_tiles[tile[0]][tile[1]] = Tile(tile[0], tile[1], Piece(self._active_tetronimo.type))
                self._create_next_piece()
                # self.next_level()
            else:
                #print('move down ' + str(self.time))
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
    def _has_collision(self, tiles):
        for tile in tiles:
            if tile[0] >= self.width:
                return True
            if self.fixed_tiles[tile[0]][tile[1]] != None:
                return True
        return False
    def _has_collision_old(self, tiles):
        min_x = min_y = max_x = max_y = 0
        for tile in tiles:
            min_x = tile[0] if tile[0] < min_x else min_x
            min_y = tile[1] if tile[1] < min_y else min_y
            max_x = tile[0] if tile[0] > max_x else max_x
            max_y = tile[1] if tile[1] > max_y else max_y
        if max_x == self.width - 1:
            return True
        min_x -= 1
        min_y -= 1
        max_x += 1
        max_y += 1
        min_x = 0 if min_x < 0 else min_x
        min_y = 0 if min_y < 0 else min_y
        max_x = self.width if max_x > self.width else max_x
        max_y = self.height if max_y > self.height else max_y
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if self.fixed_tiles[x][y] != None:
                    return True
        return False
