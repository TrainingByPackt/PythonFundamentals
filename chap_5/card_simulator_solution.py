from itertools import product

suits = {'hearts', 'clubs', 'spades', 'diamonds'}
numbers = set([i for i in range(2,15)])

def create_standard_deck():
    deck = list(product(suits, numbers))
    return sorted(deck)

def get_all_cards(deck):
    return sorted([i for i in deck])

def get_all_twos(deck):
    return sorted([i for i in deck if i[1] == 2])

def get_all_aces(deck):
    return sorted([i for i in deck if i[1] == 14])

def get_card_number(deck, card_number):
    return sorted([i for i in deck if i[1] == card_number])

def get_card_suit(deck, suit):
    return sorted([i for i in deck if i[0] == suit])

def get_number_and_suit(deck, num, suit):
    return sorted([i for i in deck if i[0] == suit and i[1] == num])

def remove_card_from_deck(deck, suit, num):
    deck.remove((suit, num))
    return get_all_cards(deck)

def remove_suit_from_deck(deck, suit):
    deck_copy = list(deck)

    for i in deck_copy:
        if i[0] == suit:
            deck.remove((suit, i[1]))
    return sorted(deck)

def remove_number_from_deck(deck, number):
    deck_copy = list(deck)

    for i in deck_copy:
        if i[0] == number:
            deck.remove((i[1], number))
    return sorted(deck)


def add_card_to_deck(deck, suit, num):
    if suit in suits and num in numbers:
        deck.append((suit, num))
    return sorted(deck)

def add_suit_to_deck(deck, suit):
    if suit in suits:
       additional_cards = list(product(suit, numbers))
       deck.extend(additional_cards)
    return sorted(deck)
    
def add_number_to_deck(deck, number):
    if number in numbers:
       additional_cards = list(product(suits, number))
       deck.extend(additional_cards)
    return sorted(deck)


if __name__ == '__main__':
    pass



