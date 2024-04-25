import random


def gameSetup():
    userName = input("Enter your name: ")

    while userName.isalpha() == False or userName == "":
        print("Please enter a valid name")
        userName = input("Enter your name: ")

    gameSize = None

    # Ask the user how many coins they want to play with
    gameSize = input(f"Hi {userName}! Enter how many coins you want to play with: ")

    # Check if the input is a number
    while gameSize is None or gameSize.isnumeric() == False or int(gameSize) <= 0:
        print("Please enter a positive number")
        gameSize = input("Enter how many coins you want to play with: ")

    return userName, int(gameSize)


def initiateArray(gameSize):

    coinsArr = [0] * gameSize

    for i in range(gameSize):
        random_num = random.randint(1, 100)
        coinsArr[i] = random_num
        print(coinsArr[i])

    return coinsArr


userName, gameSize = gameSetup()
coinsArr = initiateArray(gameSize)

print(coinsArr)
