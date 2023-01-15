from generate import bandName

print("Welcome to the band name generator!!!")
city = input("What is the city that you grew up? ")
pet = input("What is the name of you pet? ")

name = bandName(city, pet)

print(f"Your band name could be {city} {pet}")
