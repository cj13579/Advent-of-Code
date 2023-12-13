import numpy as np
p1 = 0

with open("data/09DEC.txt") as input:
    data = input.read().splitlines()

for d in data:

    start = list(map(int, d.split()))
    items = [start]
    array = np.array(start)
    while array.any():
        array = np.diff(array)
        items.append(array.tolist())

    end = len(items)-1
    p = 0
    for i, item in reversed(list(enumerate(items))):
        if i == end:
            item.append(p)
        elif i == 0:
            p = item[len(item)-1] + p
            item.append(p)
            p1 += p            
        else:
            p = item[len(item)-1] + p
            item.append(p)

print(f"Part 1: {p1}")