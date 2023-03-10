from random import randint
from game_data import data
from art import logo, vs

SCORE = 0


def print_person(compare_item, person):
    print(f'{compare_item}: {person["name"]}, a {person["job"]}, from {person["country"]}')


def compare(person_a, person_b):
    compare_persons = {
        'a': person_a['followers'],
        'b': person_b['followers']
    }
    option = input('Who has more followers? type "a" or "b": ')
    selection = compare_persons[option]
    for score in compare_persons:
        if (selection > compare_persons[score]):
            print(f'Correct answers: your score is: {SCORE+1}')
            return 1
        elif (selection < compare_persons[score]):
            print(f'Wrong answers: You Lose!!!')
            return -1
    

def game():
    compare_a = randint(0, 1)
    compare_b = randint(0, 1)
    while compare_a == compare_b:
        compare_b = randint(0, 1)
    person_a = data[compare_a]
    person_b = data[compare_b]
    print_person("Compare A", person_a)
    print(vs)
    print_person("Compare B", person_b)
    return compare(person_a, person_b)


if __name__ == "__main__":
    print(logo)
    while SCORE >= 0 and SCORE < 4:
        score = game()
        if score > 0:
            SCORE += score
        else:
            SCORE = score