with open('data/02', 'r') as file:
    lines = file.readlines()
    reports = []
    for line in lines:
        reports.append([int(l) for l in line.split()])

def is_safe(increasing: bool, report: list):
    for l in range(len(report)-1):
        t = (report[l+1] - report[l])
        if increasing:
            if t < 4 and t > 0:
                continue
            else:
                return False, l+1
        else:
            if t > -4 and t < 0:
                continue
            else:
                return False, l+1
    return True, 0

p1=0
p2=0

for report in reports:
    if report[1] > report[0]:
        increasing=True
    elif report[1] < report[0]:
        increasing=False
    else:
        continue

    safe, position = is_safe(increasing, report)
    if safe:
        p1 += 1
    else:
        del report[position]
        safe, position = is_safe(increasing, report)
        if safe:
            p2 += 1

print(f"Part 1: {p1}")
print(f"Part 2: {(p1 + p2)}")
