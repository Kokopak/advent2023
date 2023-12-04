import math

with open("input.txt") as f:
    s = 0

    for i, l in enumerate(f.read().splitlines()):
        game = l.split(": ")[1]
        game = game.replace(";", ",")

        game_fewest = {}

        for cube in game.split(", "):
            n, color = cube.split(" ")

            if int(n) > game_fewest.get(color, 0):
                game_fewest[color] = int(n)

        s += math.prod(game_fewest.values())

    print(s)
