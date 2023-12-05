with open("input.txt") as f:
    s = 0

    for i, l in enumerate(f.read().splitlines()):
        winning_numbers, numbers = l.split(": ")[1].split(" | ")

        winning_numbers = set(map(int, filter(None, winning_numbers.split(" "))))
        numbers = set(map(int, filter(None, numbers.split(" "))))

        points = 2 ** (len(numbers.intersection(winning_numbers)) - 1)

        s += points if points >= 1 else 0

print(s)
