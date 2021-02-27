from random import randrange

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

class Tetromino:
    def __init__(self, type: int, tiles0, tiles90, tiles180, tiles270, x=0, y=0):
        self.type = type
        self.current_tiles = tiles0
        self.tiles = [ tiles0, tiles90, tiles180, tiles270 ]
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
    def move_left(self):
        self.position.y -= 1
        self._update_transformed_tiles()
    def move_right(self):
        self.position.y += 1
        self._update_transformed_tiles()
    def move_down(self):
        self.position.x += 1
        self._update_transformed_tiles()
    def move_up(self):
        self.position.x -= 1
        self._update_transformed_tiles()
    def rotate_clockwise(self):
        new_rotation = self.rotation + 90
        if new_rotation == 360:
            new_rotation = 0
        self.rotation = new_rotation
        self.current_tiles = self.tiles[int(new_rotation / 90)]
        self._update_transformed_tiles()
    def rotate_counter_clockwise(self):
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
        self.changed_next = True
        self.next_tetronimo = Tetrominos[randrange(len(Tetrominos))]
        self._move_left_triggered = False
        self._move_right_triggered = False
        self._move_down_triggered = False
        self._rotate_triggered = False
        self._create_next_piece()
        for x in range(self.width):
            self.tiles.append([])
            self.fixed_tiles.append([])
            for y in range(self.height):
                self.tiles[x].append(Tile(x, y, Piece(0)))
                self.changed_tiles.append(Tile(x, y, Piece(0)))
                self.fixed_tiles[x].append(None)
        self._create_next_piece()

    # Update positions (consider collisions)
    def _process_triggers(self):
        if self._move_right_triggered:
            self._active_tetronimo.move_right()
            if self._has_collision():
                self._active_tetronimo.move_left()
            self._move_right_triggered = False
        if self._move_left_triggered:
            self._active_tetronimo.move_left()
            if self._has_collision():
                self._active_tetronimo.move_right()
            self._move_left_triggered = False
        if self._move_down_triggered:
            self._active_tetronimo.move_down()
            if self._has_collision():
                self._active_tetronimo.move_up()
            self._move_down_triggered = False
        if self._rotate_triggered:
            self._active_tetronimo.rotate_clockwise()
            if self._has_collision():
                self._active_tetronimo.rotate_counter_clockwise()
            self._rotate_triggered = False
    def _has_collision(self):
        for tile in self._active_tetronimo.transformed_tiles:
            if tile[0] < 0 or tile[1] < 0:
                return True
            if tile[0] >= self.width or tile[1] >= self.height:
                return True
            if self.fixed_tiles[tile[0]][tile[1]] != None:
                return True
        return False

    # Process external inputs (button presses)
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
        if not self._rotate_triggered:
            self._rotate_triggered = True

    # Game loop
    def _game_loop(self, delta_time):
        if self.status != 'running':
            return False
        self.time += delta_time
        self.move_time += delta_time
        if self.move_time > self.level_speed:
            self.move_time = self.move_time % self.level_speed

            # Save current position to changed tiles to ensure we can erase them if needed
            changed_tetronimo = self._active_tetronimo
            self.changed_tiles.clear()
            possible_clears = []
            for tile in changed_tetronimo.transformed_tiles:
                possible_clears.append(Point(tile[0], tile[1]))

            # Process triggers
            self._process_triggers()

            # Automatic move piece down
            self._active_tetronimo.move_down()
            if self._has_collision():
                self._active_tetronimo.move_up()
                self._fix_tetronimo()
                lines_to_clear = self._check_full_lines()
                self._add_points(len(lines_to_clear))
                self._clear_lines(lines_to_clear)
                if self._check_game_over():
                    self.status = 'stopped'
                else:
                    self._create_next_piece()

            # Update fixed tiles and changed tiles
            for tile in changed_tetronimo.transformed_tiles:
                self.changed_tiles.append(Tile(tile[0], tile[1], Piece(changed_tetronimo.type)))
            for clear in possible_clears:
                found_changed = False
                for tile in self.changed_tiles:
                    if clear.x == tile.x and clear.y == tile.y:
                        found_changed = True
                        break
                if not found_changed:
                    self.changed_tiles.append(Tile(clear.x, clear.y, Piece(0)))
        return True
    def _clear_lines(self, lines):
        return
    def _add_points(self, lines):
        if lines == 0:
            return
        elif lines == 1:
            self.points += 100 * self.level
        elif lines == 2:
            self.points += 300 * self.level
        elif lines == 3:
            self.points += 500 * self.level
        elif lines == 4:
            self.points += 800 * self.level
    def _check_full_lines(self):
        lines_to_clear = []
        line_number = 0
        for line in self.fixed_tiles:
            full_line = True
            for tile in line:
                if tile.piece.type != 0:
                    full_line = False
                    break
            if full_line:
                lines_to_clear.append(line_number)
            line_number += 1
        return lines_to_clear
    def _fix_tetronimo(self):
        for tile in self._active_tetronimo.transformed_tiles:
            new_tile = Tile(tile[0], tile[1], Piece(self._active_tetronimo.type))
            self.fixed_tiles[tile[0]][tile[1]] = new_tile
            self.changed_tiles.append(new_tile)
    def _check_game_over(self):
        for tile in self._active_tetronimo.transformed_tiles:
            if tile[0] == 0:
                return True
            return False
    def _create_next_piece(self):
        self.next_tetronimo.new_position(0, 4)
        self._active_tetronimo = self.next_tetronimo
        self.next_tetronimo = Tetrominos[randrange(len(Tetrominos))]

    # Game state
    def reset(self):
        self._init()
    def run(self, delta_time):
        self.status = 'running'
        self._game_loop(delta_time)
