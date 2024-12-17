import re

with open('data/03', 'r') as file:
    lines = file.readlines()

mt = 0
for line in lines:
    results = re.findall("mul\((\d+)\,(\d+)\)", line)
    for result in results:
        v = (int(result[0]) * int(result[1]))
        mt += v

print(f"Part 1 {mt}")
