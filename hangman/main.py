from random import choice
from stages import lifes
from logo import title

words_list = ['cat', 'dog', 'ship', 'house']

if __name__ == '__main__':
    print(title())
    print("Lets start the game")
    aleatory_word = choice(words_list)
    blank_words = "".rjust(len(aleatory_word), "_")
    stages = lifes()
    end_game = False
    trys = 6
    while not end_game:
        guessLetter = input("Guess a letter: ").lower()
        lettersIndex = []
        haveLetter = False
        for index, letter in enumerate(aleatory_word):
            if letter == guessLetter:
                lettersIndex.append(index)
                haveLetter = True
        if haveLetter:
            for index in lettersIndex:
                blank_words = blank_words[:index] + guessLetter + blank_words[index + 1:]
            print(blank_words)
            print("-------------------")
            print(stages[trys])
        else:
            trys -= 1
            print("Wrong answer you lose a life!!!")
            print("-----------------------------")
            print(stages[trys])

        if trys < 1 or "_" not in blank_words:
            end_game = True

    print("--------------------------------")

    if trys > 0:
        print("You Win")
    else:
        print("You Lose!!!")

