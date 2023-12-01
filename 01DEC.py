import re

total = 0
numbers = { "one": 1,"two": 2, "three": 3,"four": 4,"five": 5,"six" : 6,"seven": 7,"eight": 8,"nine": 9 }

def checkFirstLast(d: int, n: int):
    global first
    global first_pos
    global last
    global last_pos

    if n < first_pos:
        first = d
        first_pos = n

    if n > last_pos:
        last = d
        last_pos = n

    return first, last

with open('data/01DEC.txt') as input:
    for line in input:
        ln = dict()

        first = None
        first_pos = 1e7
        last = None
        last_pos = -1

        for n in numbers:
            text = n
            digit = numbers[n]

            result = [m.start() for m in re.finditer(str(digit), line)]
            if len(result) > 0:
                for r in result:
                    first, last = checkFirstLast(digit, r)

            ## Uncomment this to solve part 2
            # result = [m.start() for m in re.finditer(str(text), line)]
            # if len(result) > 0:
            #     for r in result:
            #         first, last = checkFirstLast(digit, r)

        combined = f"{first}{last}"
        lt = int(combined)
        total = total + lt

print(f"Total: {total}")