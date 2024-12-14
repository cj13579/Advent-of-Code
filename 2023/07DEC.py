from collections import Counter
hands = []
p1 = 0

def getType(cards: str):
    # https://www.youtube.com/watch?v=22IrAlrWqu4&t=1s
    cards = cards.replace('T', chr(ord('9')+1))
    cards = cards.replace('J', chr(ord('9')+2))
    cards = cards.replace('Q', chr(ord('9')+3))
    cards = cards.replace('K', chr(ord('9')+4))
    cards = cards.replace('A', chr(ord('9')+5))
    
    c = Counter(cards)
    if list(c.values()) == [5]: return (10, cards)
    elif sorted(c.values()) == [1,4]: return (9, cards)
    elif sorted(c.values()) == [2,3]: return (8, cards)
    elif sorted(c.values()) == [1,1,3]: return (7, cards)
    elif sorted(c.values()) == [1,2,2]:return (6, cards)
    elif sorted(c.values()) == [1,1,1,2]: return (5, cards)
    elif sorted(c.values()) == [1,1,1,1,1]: return (4, cards)
    else: return 0
 
with open("data/07DEC.txt") as input:
    for line in input:
        hand, bid = line.split()
        hands.append((hand, bid))

by_rank = sorted(hands, key=lambda hb:getType(hb[0]))
i=1
for k,v in by_rank:
    p1 += int(v) * i
    i+=1

print(f"Part 1: {p1}")