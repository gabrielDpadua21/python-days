from generator import password, password_strong, password_strong_simple

if __name__ == '__main__':
    print("Walcome to the password generator!!!")
    letters = int(input("How many letter would you like in your password? "))
    simbols = int(input("How many simbols would you like in your password? "))
    numbers = int(input("How many numbers would you like in your password? "))
    print("The new password is: ", password_strong_simple(letters, simbols, numbers))

