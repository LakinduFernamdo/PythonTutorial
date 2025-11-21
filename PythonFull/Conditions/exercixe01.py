import random

name = input("Enter name: ")
number = int(input("Enter number you guess: "))  # convert to int

randomNumber = random.randrange(1, 10)

if number == randomNumber:
    print(name + " wohoo! you won the game")
elif number == randomNumber - 1 or number == randomNumber + 1:
    print("Near to value!")
else:
    print("Sorry, try again")