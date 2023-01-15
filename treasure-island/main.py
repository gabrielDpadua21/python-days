from banner import render
from island import way, swim, door

if __name__=="__main__":
    render()
    print("Welcome to the tresure island")
    print("Your misson is to find the tresure")
    direction = input("Choose direction left(l) or rigth(r) ")
    if way(direction):
        action = input("Choose a action swim(s) or await(a) ")
        if swim(action):
            chose = input("Choose a door Red(d), Blue(b), Yellow(y) ")
            print(door(chose))