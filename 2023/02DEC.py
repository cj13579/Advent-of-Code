import re
import math

model = {
    "red": {
        "limit": 12,
        "search": re.compile(r".*\s(?P<rc>\d+)\sred.*")
    },
    "green": {
        "limit": 13,
        "search": re.compile(r".*\s(?P<rc>\d+)\sgreen.*")
    },
    "blue": {
        "limit": 14,
        "search": re.compile(r".*\s(?P<rc>\d+)\sblue.*")
    },
}

total = 0
total_power = 0

with open("data/02DEC.txt") as input:
    for line in input:
        valid = True
        line_data = line.split(":")
        game = re.search(r"^Game\s(?P<id>\d+)", line_data[0])
        game_id = game.group('id')
        data = line_data[1].split(";")
        minimums = { 'red': 0, 'green': 0, 'blue': 0 } # part 2
        for match in data:
            for color in model:
                check = re.search(model[color]['search'], match)
                if check:
                    count = int(check.group('rc'))
                    if count > model[color]['limit']:
                        valid = False

                    if count > minimums[color]: # part 2
                        minimums[color] = count

        if valid:
            total = total + int(game_id)

        power = math.prod(dict.values(minimums)) # part 2
        total_power = total_power + power

print(f"Part 1 answer is {str(total)}")
print(f"Part 2 answer is {str(total_power)}")