from itertools import product
from random import choice, seed
from os import linesep

suits = {'hearts', 'clubs', 'spades', 'diamonds'}
numbers = set([i for i in range(2,15)])
# seed(0)
# seed(6)
# seed(322) # dealer wins
# seed(1000) # player stay dealer hits and wins
# seed(817) # player stays multiple hits from dealer
# seed(885) # interesting play
# seed(551) # very interesting play (try stay, hit stay, and hit hit stay)



# Simplified rules:
# 1. Ace is always worth 11.
# 2. You always go first, i.e. no blackjack check for dealer before player has completed their turn.
# 3. If you get 21, you automatically win.
# 4. On draws, dealer wins (i.e. if you both end up with 18)

# a = randint(0,1000)
# print(a)
a = 551
seed(a)




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


def draw_card(deck):
    card = choice(deck)
    remove_card_from_deck(deck, *card)
    return card


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
    count = 0
    for cards in player:
        if cards[1] == 14:
            count += 11
        elif cards[1] >= 10:
            count += 10
        else:
            count += cards[1]
    return count


def check_cards(player):
    count = get_count(player)
    if count == 21:
        return 'WIN'
    elif count > 21:
        return 'BUST'
    else:
        return 'OK'



def create_blackjack_game(user_input):
    opponent = []
    player = []
    deck = create_standard_deck()
    opponent.append(draw_card(deck))
    opponent.append(draw_card(deck))
    player.append(draw_card(deck))
    player.append(draw_card(deck))

    player_count = get_count(player)
    dealer_count = get_count(opponent)
    display_dealer(opponent, start=True)
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
            player.append(draw_card(deck))
            display_dealer(opponent, start=True)
            display_player(player)
            player_result = check_cards(player)
            player_count = get_count(player)
            if player_result == 'WIN':
                print('You win!')
                return 1
            elif player_result == 'BUST':
                print('You Bust, dealer wins.')
                return -1
        else:
            while get_count(opponent) < 17:
                print('Dealer hits!')
                opponent.append(draw_card(deck))
                display_dealer(opponent)
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
            if player_count > dealer_count:
                print('You win!')
                return 1
            else:
                print('Dealer wins.')
                return -1

        if not user_input:
            player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
            while player_action not in ('s', 'h', 'q'):
                player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
            if player_action == 'q':
                return 0
        else:
            player_action = user_input.pop(0)


if __name__ == '__main__':
    pass
    # create_blackjack_game(None)






