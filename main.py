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
        # print(coinsArr[i])

    return coinsArr


def ArrtoStr(coinsArr):
    coinsArr_str = [str(num) for num in coinsArr]
    return " ".join(coinsArr_str)


userName, gameSize = gameSetup()
coinsArr = initiateArray(gameSize)
coinStr = ArrtoStr(coinsArr)


def playing():
    print()
    print("Select either the leftmost or rightmost coin")

    print(ArrtoStr(coinsArr))

    decision = input("Enter 'L' for leftmost or 'R' for rightmost: ")

    while decision != "L" and decision != "R" and decision != "l" and decision != "r":
        print("Please enter a valid choice")
        decision = input("Enter 'L' for leftmost or 'R' for rightmost: ")

    if decision == "L" or decision == "l":
        print("You selected the leftmost coin")
        coinsArr.pop(0)

    if decision == "R" or decision == "r":
        print("You selected the rightmost coin")
        coinsArr.pop()

    print(ArrtoStr(coinsArr))

    return len(coinsArr) > 0


flag = True

while flag:
    flag = playing()
