from conversor import position_to_letter

def encode(message, shift):
    encode_message = "";
    for letter in message.lower():
        if letter.isspace():
            encode_message += letter
        else:
            encode_message += position_to_letter(letter, shift)
    return encode_message