from collections import defaultdict

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


grid = {}

with open("input.txt") as f:
    for row, l in enumerate(f.read().splitlines()):
        for col, c in enumerate(l):
            grid[(row, col)] = c

gears = defaultdict(list)

for row in range(max(grid.keys())[0] + 1):
    current_number = ""
    part_number = False
    gear = None

    for col in range(max(grid.keys())[1] + 1):
        c = grid[row, col]

        if c.isdigit():
            current_number += c

            for n in NEIGHBORS:
                cneighbor = grid.get((row + n[0], col + n[1]), None)

                if (
                    cneighbor is not None
                    and cneighbor != "."
                    and not cneighbor.isdigit()
                ):
                    if cneighbor == "*":
                        gear = (row + n[0], col + n[1])

                    part_number = True

        cnext = grid.get((row, col + 1), None)

        if cnext is None or not cnext.isdigit():
            if part_number and current_number.isdigit():
                if gear is not None:
                    gears[gear].append(current_number)

            current_number = ""
            part_number = False
            gear = None

s = 0

for g in gears:
    gear = gears[g]

    if len(gear) == 2:
        s += int(gear[0]) * int(gear[1])

print(s)
