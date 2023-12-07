p1 = None
p2 = None

with open("data/05DEC.txt") as input:
    data = input.read()

s, *maps = data.split("\n\n")
seeds = s.split(":")[1].strip().split()

def findDest(x, line):
    data = line.split()
    d, s, r = int(data[0]), int(data[1]), int(data[2])
    e = s+r
    if s <= x <= e:
        return d+(x-s), True
    else:
        return x, False
    
def getLocation(seed):
    n = seed
    # print(f"\n\nSeed: {n}")
    for mmap in maps:
        mitems = mmap.split(":")[1].split("\n")
        item = mmap.split(":")[0].split("-")[2].split()[0]
        match = False
        for items in mitems:
            if items != "" and not match:
                n, match = findDest(n, items)

        # print(f"{item} = {n}")
    
    return n

# part 1
for seed in seeds:
    location = getLocation(int(seed))
    if p1 is not None:
        if location < p1:
            p1 = location
    else:
        p1 = location
print(f"Part 1: {p1}")

# part 2
for i, s in enumerate(range(0, len(seeds), 2)):
    start = int(seeds[s])
    stop = start + int(seeds[s+1])
    for seed in range(start, stop):
        location = getLocation(int(seed))
        if p2 is not None:
            if location < p2:
                p2 = location
        else:
            p2 = location

print(f"Part 2: {p2}")