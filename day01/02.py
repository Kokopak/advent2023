DIGIT_SPELL = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("input.txt") as f:
    s = 0

    for l in f.read().splitlines():
        for d in DIGIT_SPELL:
            l = l.replace(d, d[0] + DIGIT_SPELL[d] + d[-1])

        digits = [c for c in l if c.isdigit()]
        number = int(digits[0] + digits[-1])

        s += number

    print(s)
