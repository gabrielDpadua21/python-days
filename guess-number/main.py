from random import randint


dificults = {
    'easy': 10,
    'hard': 5
}


def generate_number():
    return randint(1, 100)


def input_guess(trys):
    print(f'You have {trys} attempts remaining to guess the number')
    guess = int(input('Make a guess: '))
    return guess


def validate_guess_size(guess, number):
    if guess > number:
        print('To high')
    else:
        print('To low')


def game(dificult):
    trys = dificults[dificult]
    number = generate_number()
    guess = 0
    while number != guess:
        guess = input_guess(trys)
        if guess == number:
            print(f'You got it! the answer is {number}')
            break
        elif trys <= 1:
            print('You lose')
            break
        validate_guess_size(guess, number)
        print('Guess Again')
        trys -= 1


if __name__ == '__main__':
    print('Welcome to the number Guessing game')
    print('Iam thinking of the number between 1 and 100')
    dificult = input('Choose a dificult. Type "easy" or "hard": ')
    game(dificult)