RULES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("input.txt") as f:
    s = 0

    for i, l in enumerate(f.read().splitlines()):
        game = l.split(": ")[1]
        game = game.replace(";", ",")

        for cube in game.split(", "):
            n, color = cube.split(" ")

            if int(n) > RULES[color]:
                break
        else:
            s += i + 1

    print(s)
