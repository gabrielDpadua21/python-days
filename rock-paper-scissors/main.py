from random import randint
from rules import rock, paper, scissors
from hands import rock_hand, paper_hand, scissors_hand

if __name__ == '__main__':
    print("Welcome to the rock, paper, scissors game")
    choises = ["rock", "paper", "scissors"]
    sinals = [rock_hand(), paper_hand(), scissors_hand()]
    my_choice_int = int(input("What do you choose? Type 0 to rock, 1 to paper and 2 scissors "))
    machine_choice_int = randint(0, 2)
    try:
        print("You choose: ")
        print(sinals[my_choice_int])
        print("Machine choose: ")
        print(sinals[machine_choice_int])
        if choises[my_choice_int] == "rock":
            print(rock(choises[machine_choice_int]))
        elif choises[my_choice_int] == "paper":
            print(paper(choises[machine_choice_int]))
        else:
            print(scissors(choises[machine_choice_int]))
    except:
        print("Invalid choice")




