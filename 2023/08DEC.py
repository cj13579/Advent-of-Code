import re
with open("data/08DEC.txt") as input:
    lines = input.read().splitlines()

order = list(lines[0].strip())
map = {}

for i, line in enumerate(lines):
    if line == '':
        continue
    else:
        match = re.search(r'^(?P<point>\w+)\s=\s\((?P<left>\w+),\s(?P<right>\w+)\)', line)
        if match:
            map[match.group('point')] = {
                'L': match.group('left'),
                'R' :match.group('right')
            }

np = len(list(map.keys())) # number of points
start = 'AAA'
end = 'ZZZ'
location = start # set starting location
p1 = 0

while location != end:
    for l in order:
        location = map[location][l]
        p1 +=1

print(f"Part 1: {p1}")