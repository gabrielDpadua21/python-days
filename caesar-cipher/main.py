from encoder import encode
from decoder import decode
from banner import render

if __name__ == '__main__':
    print(render())
    exit = True
    while exit:
        direction = input("Type (e) to encode, (d) to decode a message or s to exit (e/d/s): ")
        if direction == "s":
            print("Goodbye")
            break
        text = input("Type you message: ")
        shift = int(input("Type the shift value: "))
        if direction == "e":
            message = encode(text, shift)
            print(f"The encripted message is: {message}")
        elif direction == "d":
            message = decode(text, shift)
            print(f"The decripted message is: {message}")
        else:
            print("Invalid input, try again!!!")
