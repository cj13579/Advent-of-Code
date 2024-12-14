from collections import Counter

with open('data/01', 'r') as file:
    lines = file.readlines()
    la = []
    lb = []
    for line in lines:
        l = line.split()
        la.append(int(l[0]))
        lb.append(int(l[1]))

la.sort()
lb.sort()

i=0
d = []

for k, v in enumerate(la):
    if la[k] <= lb[k]:
        d.append((lb[k] - la[k]))
    else:
        d.append((la[k] - lb[k]))

print(f"Part 1: {sum(d)}")

s = []
counts = dict(Counter(lb).items())

for item in la:
    if item in lb:
        s.append((item * counts[item]))

print(f"Part 2: {sum(s)}")
