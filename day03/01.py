NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


grid = {}
with open("input.txt") as f:
    for row, l in enumerate(f.read().splitlines()):
        for col, c in enumerate(l):
            grid[(row, col)] = c

s = 0

for row in range(max(grid.keys())[0] + 1):
    current_number = ""
    part_number = False

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
                    part_number = True

        cnext = grid.get((row, col + 1), None)

        if cnext is None or not cnext.isdigit():
            if part_number and current_number.isdigit():
                s += int(current_number)

            current_number = ""
            part_number = False

print(s)
