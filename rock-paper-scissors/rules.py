
def rock(machine):
    if machine == "paper":
        return "You Lose"
    elif machine == "scissors":
        return "You Win"
    return "a tie"

def paper(machine):
    if machine == "scissors":
        return "You Lose"
    elif machine == "rock":
        return "You Win"
    return "a tie"

def scissors(machine):
    if machine == "rock":
        return "You Lose"
    elif machine == "paper":
        return "You Win"
    return "a tie"