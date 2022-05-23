example_deck = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16}


def simple(own_hand, dealer_hand, cards_in_deck):
    chances = calc_chances(cards_in_deck)
    dealer_end_hand = likeliest_dealer_hand(dealer_hand, cards_in_deck)
    if own_hand <= 11:
        return "Hit"

    if dealer_end_hand > 21:
        return "Stand"

    if own_hand >= dealer_end_hand:
        return "Stand"

    chance_of_winning = 0.5
    for key, value in chances.items():
        if (own_hand + key) < dealer_end_hand:
            chance_of_winning -= value
        else:
            chance_of_winning += value
    if chance_of_winning > 0.5:
        return "Hit"
    else:
        return "Stand"


def calc_chances(cards_in_deck):
    total_cards = sum(cards_in_deck.values())
    chances = {}
    for key, value in cards_in_deck.items():
        chances[key] = cards_in_deck[key]/total_cards
    return chances


def likeliest_dealer_hand(dealer_hand, cards_in_deck):
    while dealer_hand < 17:
        new_card, cards_in_deck = likeliest_card(cards_in_deck)
        dealer_hand += new_card
    return dealer_hand


def likeliest_card(cards_in_deck):
    most_likely = max(cards_in_deck, key=cards_in_deck.get)
    cards_in_deck[most_likely] -= 1
    return most_likely, cards_in_deck


#print(likeliest_dealer_hand(7, example_deck))
#simple(18, 7, example_deck)
