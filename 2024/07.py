from itertools import product

with open('data/07', 'r') as file:
    lines = file.read().split("\n")

total = 0

for line in lines:
    split = line.split(":")
    result = int(split[0])
    vars =  [int(x) for x in split[1].strip().split(" ")]

    for i in product("*+", repeat=len(vars)-1):
        p = vars[0]
        for j in range(1, len(vars)):
            if i[j-1] == "+":
                p += vars[j]
            else:
                p *= vars[j]
        
        if p == result:
            total += p
            break

print(f"Part 1: {total}")
