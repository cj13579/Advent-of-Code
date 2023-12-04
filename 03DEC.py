import sys
grid = []

with open('data/03DEC.txt') as input:
    for l in input:
        line = []
        for char in list(l):
            if char != '\n':
                line.append(char)
        grid.append(line)


def getNumberAndPartStatus(row: int, column: int):

    def checkPartAndGears(row: int, column: int):

        part = False
        for row_neighbor in [-1,0,1]:
            if row+row_neighbor<rows and row+row_neighbor>0:
                for column_neighbor in [-1,0,1]:
                    if 0<=r+row_neighbor<rows and 0<=column+column_neighbor<columns:
                        pc = grid[row+row_neighbor][column+column_neighbor]
                        if not pc.isdigit() and pc != '.':
                            part = True
                        if pc == "*":
                            gear_positions.append((r+row_neighbor, column+column_neighbor))

        return part
    
    is_part = False
    num = True
    n = [grid[row][column]]
    pc = checkPartAndGears(r, c)
    if pc:
        is_part = True

    i = 1
    while num:
        if column+i<columns:
            nc = grid[r][column+i]
            if nc.isdigit():
                n.append(nc)
                pc = checkPartAndGears(r, column+i)
                if pc:
                    is_part = True

                i +=1 
            else:
                break
        else:
            break
    
    part_number = int(''.join(n))

    return part_number, is_part, i

columns = len(grid[0])
rows = len(grid)
parts_total = 0
gear_positions = []

for r in range(rows):
    c = 0
    while c < columns:
        if grid[r][c].isdigit():
            number, is_part, position = getNumberAndPartStatus(r, c)
            if is_part:
                parts_total += number
            c += position
            n=[]
            continue
        else:
            c += 1

print(f"Parts total: {parts_total}")