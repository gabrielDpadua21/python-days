from conversor import position_to_letter

def decode(message, shift):
    decript_message = ""
    for letter in message.lower():
        if letter.isspace():
            decript_message += letter
        else:
            decript_message += position_to_letter(letter, -shift)
    return decript_message
