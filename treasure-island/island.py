
def way(direction):
    if direction.lower() != "l":
        print("Fall into a hole. Game Over")
        return False
    return True
    
def swim(action):
    if action.lower() != "a":
        print("Attack by trout. Game Over")
        return False
    return True
    
def door(chose):
    if chose.lower() == "y":
        return "You Win!"
    if chose.lower() == "b":
        return "Eaten by beats. Game Over"
    if chose.lower() == "r":
        return "Burned by fired. Gamer Over"
    return "Game Over"
        