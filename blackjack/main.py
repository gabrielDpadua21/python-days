import random

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


def first_hand():
    counter = 0;
    while counter < 2:
        player_draw()
        deeler_draw()
        counter += 1


def player_draw():
    random_card = random.randint(0, 12)
    card_player = cards[random_card]
    PLAYER['cards'].append(card_player)
    PLAYER['total'] += cards_point[card_player]


def deeler_draw():
     random_card = random.randint(0, 12)
     deeler_card = cards[random_card]
     DEELER['cards'].append(deeler_card)
     DEELER['total'] += cards_point[deeler_card]


def player_hand():
    print(f'Your cards: {PLAYER["cards"]} - Poits: {PLAYER["total"]}')


def deeler_shadow_hands():
     print(f'Deeler cards: {DEELER["cards"][0]}')


def deeler_hands():
     print(f'Deeler cards: {DEELER["cards"]} - Poits: {DEELER["total"]}')


def points():
    print(f'Deeler points: {DEELER["total"]}')
    print(f'Your points: {PLAYER["total"]}')


def verify_points():
    game_status = True
    if DEELER['total'] >= 17:
        if PLAYER['total'] > 21:
            print('You lose!!!')
        elif PLAYER['total'] == 21:
            print('You Win!!!')
        elif PLAYER['total'] <= 21 and PLAYER['total'] > DEELER['total']:
            print('You Win!!!')
        game_status = False
    points()
    return game_status


def clear_hands():
    PLAYER['cards'] = []
    PLAYER['total'] = 0
    DEELER['cards'] = []
    DEELER['total'] = 0


def game():
    start = int(input('You want to play(1) or exit(0)? '))
    game_status = False
    clear_hands()
    if start == 1:
        game_status = True
        first_hand()
        player_hand()
        deeler_shadow_hands()
        while game_status:
            op = input('You want draw (y) or pass (n)? ')
            if op == 'y':
                player_draw()
                deeler_draw()
            else:
                deeler_draw()

            player_hand()
            deeler_shadow_hands()
            game_status = verify_points()
        game()
    else:
        print('Bye')


if __name__ == "__main__":
    print('Black Jack')
    game()
    
    

    
    
