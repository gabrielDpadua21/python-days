from random import randint

def for_print_twenty():
    for i in range(1, 21):
        if i == 20:
            print('You got it')



def random_values():
    dice_numbers = ['1', '2', '3', '4', '5', '6']
    dice = randint(0, 5)
    print(dice_numbers[dice])


def you_generarion():
    year = int(input("What's your year of birth? "))
    if year > 1980 and year <= 1994:
        print("You ara a millennial")
    elif year > 1994:
        print("You are generation Z")


you_generarion()
