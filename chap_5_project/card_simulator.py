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


def display_opponent(opponent, start=False):
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
    # Dont do anything with user_input, its just for automated testing.
    # This function essentially requires no input and just runs the simulation.
    # setup players, deck and deal initial cards
    opponent = []
    player = []
    deck = create_standard_deck()

    # implement code to draw two cards for each player using the draw_card function and store in appropriate list

    # get a count for each player
    player_count = get_count(player)
    dealer_count = get_count(opponent)

    # displays board
    display_opponent(opponent, start=True)
    display_player(player)

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
            # implement logic for the player hitting

            display_opponent(opponent, start=True)
            display_player(player)

            player_result = check_cards(player)
            player_count = get_count(player)

            # implement logic for checking if player won or lost.
        else:
            while get_count(opponent) < 17:
                print('Dealer hits!')
                opponent.append(draw_card(deck))
                display_opponent(opponent)
                display_player(player)
                dealer_result = check_cards(opponent)
                dealer_count = get_count(opponent)
                if dealer_result == 'WIN':
                    print('Dealer wins.')
                    return -1
                elif dealer_result == 'BUST':
                    print('Dealer Busts, you win.')
                    return 1

            print('Player: {}, Dealer: {}'.format(player_count, dealer_count))
            # implement logic for checking who had the highest count of no one busted.

        if not user_input:
            player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
            while player_action not in ('s', 'h', 'q'):
                player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
            if player_action == 'q':
                return 0
        else:
            player_action = user_input.pop(0)

