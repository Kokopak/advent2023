from collections import Counter

cards = Counter()
match = {}

with open("input.txt") as f:
    for i, l in enumerate(f.read().splitlines()):
        cards[i] += 1

        winning_numbers, numbers = l.split(": ")[1].split(" | ")

        winning_numbers = set(map(int, filter(None, winning_numbers.split(" "))))
        numbers = set(map(int, filter(None, numbers.split(" "))))

        matching_numbers = len(numbers.intersection(winning_numbers))
        match[i] = matching_numbers


for i in range(max(cards)):
    for ii in range(match[i]):
        cards[i + ii + 1] += cards[i]


print(cards.total())
