# from card_simulator import *
from card_simulator_solution import *

suits = {'hearts', 'clubs', 'spades', 'diamonds'}
numbers = set([i for i in range(2,15)])

def test_get_all_cards():
    d1 = create_standard_deck()
    result = get_all_cards(d1)
    answer = [('clubs', 2), ('clubs', 3), ('clubs', 4), ('clubs', 5), ('clubs', 6), ('clubs', 7), ('clubs', 8), ('clubs', 9), ('clubs', 10), ('clubs', 11), ('clubs', 12), ('clubs', 13), ('clubs', 14), ('diamonds', 2), ('diamonds', 3), ('diamonds', 4), ('diamonds', 5), ('diamonds', 6), ('diamonds', 7), ('diamonds', 8), ('diamonds', 9), ('diamonds', 10), ('diamonds', 11), ('diamonds', 12), ('diamonds', 13), ('diamonds', 14), ('hearts', 2), ('hearts', 3), ('hearts', 4), ('hearts', 5), ('hearts', 6), ('hearts', 7), ('hearts', 8), ('hearts', 9), ('hearts', 10), ('hearts', 11), ('hearts', 12), ('hearts', 13), ('hearts', 14), ('spades', 2), ('spades', 3), ('spades', 4), ('spades', 5), ('spades', 6), ('spades', 7), ('spades', 8), ('spades', 9), ('spades', 10), ('spades', 11), ('spades', 12), ('spades', 13), ('spades', 14)]
    assert result == answer  

def test_get_all_twos():
    d1 = create_standard_deck()
    result = get_all_twos(d1)
    answer = [('clubs', 2), ('diamonds', 2), ('hearts', 2), ('spades', 2)]
    assert result == answer

def test_get_all_aces():
    d1 = create_standard_deck()
    result = get_all_aces(d1)
    answer = [('clubs', 14), ('diamonds', 14), ('hearts', 14), ('spades', 14)]
    assert result == answer

def test_get_card_number():
    d1 = create_standard_deck()
    result = get_card_number(d1, 5)
    answer = [('clubs', 5), ('diamonds', 5), ('hearts', 5), ('spades', 5)]
    assert result == answer

def test_get_card_suit_clubs():
    d1 = create_standard_deck()
    result = get_card_suit(d1, 'clubs')
    answer = [('clubs', 2), ('clubs', 3), ('clubs', 4), ('clubs', 5), ('clubs', 6), ('clubs', 7), ('clubs', 8), ('clubs', 9), ('clubs', 10), ('clubs', 11), ('clubs', 12), ('clubs', 13), ('clubs', 14)]
    assert result == answer

def test_get_card_suit_hearts():
    d1 = create_standard_deck()
    result = get_card_suit(d1, 'hearts')
    answer = [('hearts', 2), ('hearts', 3), ('hearts', 4), ('hearts', 5), ('hearts', 6), ('hearts', 7), ('hearts', 8), ('hearts', 9), ('hearts', 10), ('hearts', 11), ('hearts', 12), ('hearts', 13), ('hearts', 14)]
    assert result == answer
    
def test_get_card_suit_diamonds():
    d1 = create_standard_deck()
    result = get_card_suit(d1, 'diamonds')
    answer = [('diamonds', 2), ('diamonds', 3), ('diamonds', 4), ('diamonds', 5), ('diamonds', 6), ('diamonds', 7), ('diamonds', 8), ('diamonds', 9), ('diamonds', 10), ('diamonds', 11), ('diamonds', 12), ('diamonds', 13), ('diamonds', 14)]
    assert result == answer 

def test_get_card_suit_spades():
    d1 = create_standard_deck()
    result = get_card_suit(d1, 'spades')
    answer = [('spades', 2), ('spades', 3), ('spades', 4), ('spades', 5), ('spades', 6), ('spades', 7), ('spades', 8), ('spades', 9), ('spades', 10), ('spades', 11), ('spades', 12), ('spades', 13), ('spades', 14)]
    assert result == answer 

def test_get_number_and_suit_9s():
    d1 = create_standard_deck()
    result = get_number_and_suit(d1, 9,'spades')
    answer = [('spades', 9)]
    assert result == answer 

def test_get_number_and_suit_10h():
    d1 = create_standard_deck()
    result = get_number_and_suit(d1, 10,'hearts')
    answer = [('hearts', 10)]
    assert result == answer
    
def test_get_number_and_suit_14c():
    d1 = create_standard_deck()
    result = get_number_and_suit(d1, 14,'clubs')
    answer = [('clubs', 14)]
    assert result == answer
    
def test_get_number_and_suit_2d():
    d1 = create_standard_deck()
    result = get_number_and_suit(d1, 2,'diamonds')
    answer = [('diamonds', 2)]
    assert result == answer

def test_get_number_and_suit():
    d1 = create_standard_deck()
    for suit,num in product(suits, numbers):
        result = get_number_and_suit(d1, num, suit)
        answer = [(suit, num)]
        assert result == answer

def test_remove_card_from_deck():
    d1 = create_standard_deck()
    deleted_set = set()
    base = set([('clubs', 2), ('clubs', 3), ('clubs', 4), ('clubs', 5), ('clubs', 6), ('clubs', 7), ('clubs', 8), ('clubs', 9), ('clubs', 10), ('clubs', 11), ('clubs', 12), ('clubs', 13), ('clubs', 14), ('diamonds', 2), ('diamonds', 3), ('diamonds', 4), ('diamonds', 5), ('diamonds', 6), ('diamonds', 7), ('diamonds', 8), ('diamonds', 9), ('diamonds', 10), ('diamonds', 11), ('diamonds', 12), ('diamonds', 13), ('diamonds', 14), ('hearts', 2), ('hearts', 3), ('hearts', 4), ('hearts', 5), ('hearts', 6), ('hearts', 7), ('hearts', 8), ('hearts', 9), ('hearts', 10), ('hearts', 11), ('hearts', 12), ('hearts', 13), ('hearts', 14), ('spades', 2), ('spades', 3), ('spades', 4), ('spades', 5), ('spades', 6), ('spades', 7), ('spades', 8), ('spades', 9), ('spades', 10), ('spades', 11), ('spades', 12), ('spades', 13), ('spades', 14)])
    for suit, num in product(suits, numbers):
        deleted_set.add((suit, num))
        result = list(remove_card_from_deck(d1, suit, num))
        answer = base-deleted_set
        assert result == list(sorted(answer))

def test_remove_suit_from_deck_hearts():
    d1 = create_standard_deck()
    deleted_set = set()
    base = set([('clubs', 2), ('clubs', 3), ('clubs', 4), ('clubs', 5), ('clubs', 6), ('clubs', 7), ('clubs', 8), ('clubs', 9), ('clubs', 10), ('clubs', 11), ('clubs', 12), ('clubs', 13), ('clubs', 14), ('diamonds', 2), ('diamonds', 3), ('diamonds', 4), ('diamonds', 5), ('diamonds', 6), ('diamonds', 7), ('diamonds', 8), ('diamonds', 9), ('diamonds', 10), ('diamonds', 11), ('diamonds', 12), ('diamonds', 13), ('diamonds', 14), ('hearts', 2), ('hearts', 3), ('hearts', 4), ('hearts', 5), ('hearts', 6), ('hearts', 7), ('hearts', 8), ('hearts', 9), ('hearts', 10), ('hearts', 11), ('hearts', 12), ('hearts', 13), ('hearts', 14), ('spades', 2), ('spades', 3), ('spades', 4), ('spades', 5), ('spades', 6), ('spades', 7), ('spades', 8), ('spades', 9), ('spades', 10), ('spades', 11), ('spades', 12), ('spades', 13), ('spades', 14)])
    for num in numbers:
        deleted_set.add(('hearts', num))
    result = list(remove_suit_from_deck(d1, 'hearts'))
    answer = base-deleted_set
    assert result == list(sorted(answer))

def test_remove_suit_from_deck():
    for suit in suits:
        d1 = create_standard_deck()
        deleted_set = set()
        base = set([('clubs', 2), ('clubs', 3), ('clubs', 4), ('clubs', 5), ('clubs', 6), ('clubs', 7), ('clubs', 8), ('clubs', 9), ('clubs', 10), ('clubs', 11), ('clubs', 12), ('clubs', 13), ('clubs', 14), ('diamonds', 2), ('diamonds', 3), ('diamonds', 4), ('diamonds', 5), ('diamonds', 6), ('diamonds', 7), ('diamonds', 8), ('diamonds', 9), ('diamonds', 10), ('diamonds', 11), ('diamonds', 12), ('diamonds', 13), ('diamonds', 14), ('hearts', 2), ('hearts', 3), ('hearts', 4), ('hearts', 5), ('hearts', 6), ('hearts', 7), ('hearts', 8), ('hearts', 9), ('hearts', 10), ('hearts', 11), ('hearts', 12), ('hearts', 13), ('hearts', 14), ('spades', 2), ('spades', 3), ('spades', 4), ('spades', 5), ('spades', 6), ('spades', 7), ('spades', 8), ('spades', 9), ('spades', 10), ('spades', 11), ('spades', 12), ('spades', 13), ('spades', 14)])
        for num in numbers:
            deleted_set.add((suit, num))
        result = list(remove_suit_from_deck(d1, suit))
        answer = base-deleted_set
        assert result == list(sorted(answer))

def test_black_jack_player_win():
    seed(551)
    user_input = ['h', 's']
    result = create_blackjack_game(user_input)
    assert result == 1


def test_black_jack_dealer_win():
    seed(551)
    user_input = ['h', 'h', 's']
    result = create_blackjack_game(user_input)
    assert result == -1


def test_black_jack_dealer_wins2():
    seed(551)
    user_input = ['s']
    result = create_blackjack_game(user_input)
    assert result == -1


def test_black_jack_quit():
    seed(551)
    user_input = ['q']
    result = create_blackjack_game(user_input)
    assert result == 0
