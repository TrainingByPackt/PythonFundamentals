from itertools import product
from random import choice, seed
from os import linesep


suits = {'hearts', 'clubs', 'spades', 'diamonds'}
numbers = set([i for i in range(2,15)])
a = 551
seed(a)

def create_standard_deck():
    pass


def get_all_cards(deck):
    pass


def get_all_twos(deck):
    pass


def get_all_aces(deck):
    pass


def get_card_number(deck, card_number):
    pass


def get_card_suit(deck, suit):
    pass


def get_number_and_suit(deck, num, suit):
    pass


def remove_card_from_deck(deck, suit, num):
    pass


def remove_suit_from_deck(deck, suit):
    pass


def remove_number_from_deck(deck, number):
    pass


def add_card_to_deck(deck, suit, num):
    pass


def add_suit_to_deck(deck, suit):
    pass


def add_number_to_deck(deck, number):
    pass


def draw_card(deck):
    # replace this with your implementation
    pass


def display_dealer(opponent, start=False):
    print('Dealer:')
    if start:
        the_output = [opponent[0], ('?', '?')]
        print(the_output)
    else:
        print(opponent)


def display_player(player):
    print('Player:')
    print(player)


def get_count(player):
    # replace this with your implementation
    return 0


def check_cards(player):
    # replace this with your implementation
    pass


def create_blackjack_game(user_input):
    # FIRST SECTION INSERT YOUR CODE HERE
    # REPLACE WITH YOUR CODE


    if not user_input:
        player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
        while player_action not in ('s', 'h', 'q'):
            player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
    else:
        player_action = user_input.pop(0)

    if player_action == 'q':
        return 0
    while player_action != 'q':

        if player_action == 'h':
            pass
            # SECOND SECTION INSERT YOUR CODE HERE
            # REPLACE WITH YOUR CODE
        else:
            while True:
                # THIRD SECTION INSERT YOUR CODE HERE
                # REPLACE WITH YOUR CODE

                pass

        if not user_input:
            player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
            while player_action not in ('s', 'h', 'q'):
                player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
            if player_action == 'q':
                return 0
        else:
            player_action = user_input.pop(0)

