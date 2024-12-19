puzzle = []

with open('data/06', 'r') as file:
    lines = file.read().split("\n")
    for line in lines:
        puzzle.append(list(line))

rows = len(puzzle)
columns = len(puzzle[0])

# get the start position
for y, v in enumerate(puzzle): # y
    for x,j in enumerate(v): # x
        if j in ('^', 'V', '<', '>'):
            pos = (y,x)
            break

while pos[0] < (rows -1) and pos[1] < (columns - 1):
    pos_char = puzzle[pos[0]][pos[1]]
    if pos_char == '^':
        next_char = puzzle[pos[0]-1][pos[1]]
        puzzle[pos[0]][pos[1]] = 'X'
        if next_char == "#":
            pos = (pos[0], pos[1] + 1)
            puzzle[pos[0]][pos[1]] = '>'
            continue
        else:
            pos = (pos[0]- 1, pos[1])
            puzzle[pos[0]][pos[1]] = '^'
            continue
    if pos_char == '>':
        next_char = puzzle[pos[0]][pos[1]+1]
        puzzle[pos[0]][pos[1]] = 'X'
        if next_char == '#':
            pos = (pos[0] + 1, pos[1])
            puzzle[pos[0]][pos[1]] = 'V'
            continue
        else:
            pos = (pos[0], pos[1] + 1)
            puzzle[pos[0]][pos[1]] = '>'
            continue
    if pos_char == 'V':
        next_char = puzzle[pos[0] + 1][pos[1]]
        puzzle[pos[0]][pos[1]] = 'X'
        if next_char == "#":
            pos = (pos[0], pos[1] - 1)
            puzzle[pos[0]][pos[1]] = '<'
            continue
        else:
            pos = (pos[0] + 1, pos[1])
            puzzle[pos[0]][pos[1]] = 'V'
            continue
    if pos_char == '<':
        next_char = puzzle[pos[0]][pos[1] -1]
        puzzle[pos[0]][pos[1]] = 'X'
        if next_char == "#":
            pos = (pos[0] - 1, pos[1])
            puzzle[pos[0]][pos[1]] = '^'
            continue
        else:
            pos = (pos[0] , pos[1] - 1)
            puzzle[pos[0]][pos[1]] = '<'
            continue

total = 1
for line in puzzle:
    for p in line:
        if p == 'X':
            total += 1

print(f"Part 1: {total}")
