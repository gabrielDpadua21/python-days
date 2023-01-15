from random import choice, shuffle

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
SIMBOLS = ['@', '#', '$', '%', 'ˆ', '&', '*', '!']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def password(letters, simbols, numbers):
    new_password = ""
    for letter in range(0, letters):
        new_password += choice(LETTERS)
    for simbol in range(0, simbols):
        new_password += choice(SIMBOLS)
    for number in range(0, numbers):
        new_password += choice(NUMBERS)
    return new_password;

def password_strong(letters, simbols, numbers):
    count_letters = 0
    count_simbols = 0
    count_numbers = 0
    new_password = ""
    for letter in range(0, (letters + simbols + numbers)):
        password_chars = [];
        if count_numbers < numbers:
            password_chars.append(NUMBERS)
        if count_simbols < simbols:
            password_chars.append(SIMBOLS)
        if count_letters < letters:
            password_chars.append(LETTERS)
        list = choice(password_chars)
        char = choice(list)
        new_password += char
        if char in LETTERS: count_letters+=1
        if char in SIMBOLS: count_simbols+=1
        if char in NUMBERS: count_numbers+=1
    return new_password

def password_strong_simple(letters, simbols, numbers):
    new_password = [];
    for letter in range(0, letters):
        new_password.append(choice(LETTERS))

    for simbol in range(0, simbols):
        new_password.append(choice(SIMBOLS))

    for number in range(0, numbers):
        new_password.append(choice(NUMBERS))

    shuffle(new_password)
    password_string = ""
    for char in new_password:
        password_string += char

    return password_string


