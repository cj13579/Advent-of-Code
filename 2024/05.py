rules = []
updates = []
fine = []
total = 0

with open('data/05', 'r') as file:
    lines = file.read().split("\n")
    for line in lines:
        if line == '':
            continue
        if '|' in line:
            rules.append([int(l) for l in line.split('|')])
        else:
            updates.append([int(l) for l in line.split(',')])

def isOk(update: list):
    i = 0
    while i < len(update):
        if i == len(update) -1:
            return True

        for rule in rules:
            if rule[0] == update[i+1] and rule[1] == update[i]:
                return False
        i += 1
    
    return True

for update in updates:
    if isOk(update):
        total += update[int((len(update) / 2))]

print(f"Part 1: {total}")
