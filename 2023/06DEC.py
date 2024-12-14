p1 = 0
p2 = 0

with open("data/06DEC.txt") as input:
    data = input.readlines()

times = list(map(int, data[0].split(":")[1].strip().split()))
distances = list(map(int, data[1].split(":")[1].strip().split()))
for i in range(len(times)):
    p=0
    h = 0
    while h < times[i]:
        l = times[i] - h
        s = h * l
        if s > distances[i]:
            p += 1
        h +=1
    if p1 == 0:
        p1 = p
    else:
        p1 = p * p1
print(f"Part 1: {p1}")

ts = ''
ds = ''
for x in times: ts = ts + str(x)
for x in distances: ds = ds + str(x)

t = int(ts)
d = int(ds)
h = 0
while h < t:
    l = t - h
    s = h * l
    if s > d:
        p2 += 1
    h +=1

print(f"Part 2: {(p2)}")