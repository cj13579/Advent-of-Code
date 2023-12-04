import re
import math

points_total = 0
total_cards_won = 0
cards = []
card_dict = {}

with open("data/04DEC.txt") as input:
    for line in input:

        card_points = 0
        cards_won = 0
        winning_numbers = []
        has_numbers = []

        c = line.split(":")
        cid = re.search(r"^Card\s+(?P<id>\d+)", c[0])
        card_id = int(cid.group('id'))
        if card_id not in card_dict: card_dict[card_id] = 1
        else: card_dict[card_id] += 1
        card_numbers = c[1].rstrip('\n').split("|")

        for n in card_numbers[0].split(): winning_numbers.append(n)
        for n in card_numbers[1].split(): has_numbers.append(n)

        #part 1
        for n in has_numbers:
            if n in winning_numbers:
                cards_won += 1
                if card_points == 0:
                    card_points = 1
                else:
                    card_points = card_points * 2 
        points_total += card_points

        # part 2
        card_modifier = card_dict[card_id]
        for c in range(0, cards_won):
            cw = card_id + c + 1
            if cw in card_dict:
                card_dict[cw] += card_modifier
            else:
                card_dict[cw] = card_modifier
        total_cards_won += card_dict[card_id]

    print(f"Total points: {points_total}")
    print(f"Total cards won: {total_cards_won}")