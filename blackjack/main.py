import random
from banner import logo

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


cards_point = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}


PLAYER = {
    'cards': [],
    'total': 0
}


DEELER = {
    'cards': [],
    'total': 0
}

def player_hand():
    print(f'Your cards: {PLAYER["cards"]} - Poits: {PLAYER["total"]}')


def deeler_shadow_hands():
     print(f'Deeler cards: {DEELER["cards"][0]}')


def deeler_hands():
     print(f'Deeler cards: {DEELER["cards"]} - Poits: {DEELER["total"]}')


def first_hand():
    counter = 0;
    while counter < 2:
        player_draw()
        deeler_draw()
        counter += 1


def player_draw():
    card_player = random.choice(cards)
    PLAYER['cards'].append(card_player)
    PLAYER['total'] += cards_point[card_player]


def deeler_draw():
     deeler_card = random.choice(cards)
     DEELER['cards'].append(deeler_card)
     DEELER['total'] += cards_point[deeler_card]


def player_draws():
    while True:
        op = input('You want draw (y) or pass (n)? ')
        if op == 'y':
            player_draw()
            player_hand()
        else:
            break


def deeler_draws():
    while DEELER['total'] < 17:
        deeler_draw()


def points():
    print(f'Deeler points: {DEELER["total"]} - Cards: {DEELER["cards"]}')
    print(f'Your points: {PLAYER["total"]} - Cards: {PLAYER["cards"]}')


def score():
    if PLAYER['total'] > 21:
        print('You lose - score burst')
    elif PLAYER['total'] == 21:
        print('You win - blackjack')
    elif PLAYER['total'] > DEELER['total']:
        print('You win - best score')
    elif DEELER['total'] > 21:
        print('You win - deeler score burst')
    else:
        print('You lose!!!')


def clear_hands():
    PLAYER['cards'] = []
    PLAYER['total'] = 0
    DEELER['cards'] = []
    DEELER['total'] = 0


def game():
    logo()
    clear_hands()
    first_hand()
    player_hand()
    deeler_shadow_hands()
    player_draws()
    deeler_draws()
    score()
    points()


if __name__ == "__main__":
    print('Black Jack')
    while int(input('You want to play(1) or exit(0)? ')) == 1:
        game()
    else:
        print('Bye!!!')
    
    

    
    
