with open("input.txt") as f:
    s = 0

    for l in f.read().splitlines():
        digits = [c for c in l if c.isdigit()]
        number = int(digits[0] + digits[-1])

        s += number

    print(s)
