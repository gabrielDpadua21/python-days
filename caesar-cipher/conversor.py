
def position_to_letter(letter, shift):
    return chr((ord(letter) + shift - 97) % 26 + 97)