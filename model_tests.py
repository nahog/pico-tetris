from model import Game, Tetromino

game = Game()

print("\n - Test: Next tetronimo ... ", end="")
if isinstance(game.next_tetronimo, Tetromino):
    print("OK")
else:
    print(game.next_tetronimo)

print("\n - Test: Active tetronimo ... ", end="")
if isinstance(game._active_tetronimo, Tetromino):
    print("OK")
else:
    print(game._active_tetronimo)

print("\n - Test: Empty initial fixed ... ", end="")
for i in game.fixed_tiles:
    for tile in i:
        if tile != None:
            print(i)
print("OK")

print("\n - Test: All initial changed ... ", end="")
if len(game.changed_tiles) == game.width * game.height:
    print("OK")
else:
    print(game.changed_tiles)

print("\n - Test: Next initial changed ... ", end="")
if game.changed_next:
    print("OK")
else:
    print(game.changed_next)

