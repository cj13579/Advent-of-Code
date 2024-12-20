with open('data/09', 'r') as file:
    lines = file.read().split("\n")

line = list(lines[0])

layout = []
file_id = 0
for i, char in enumerate(line):
    length = int(char)
    if i % 2 == 0:  # File block
        layout.extend([file_id] * length)
        file_id += 1
    else:  # Free space
        layout.extend(['.'] * length)

ordered = list(layout)

dots = []
for i, block in enumerate(ordered):
    if block == '.':
        dots.append(i)

for i in range(len(ordered) - 1, -1, -1):
    if ordered[i] != '.':  # File block
        if dots and dots[0] < i:
            swap_index = dots.pop(0)
            ordered[swap_index], ordered[i] = ordered[i], '.'

total = 0 
for idx, block in enumerate(ordered):
    if block != '.':
        total += idx * block

print(f"Part 1: {total}")