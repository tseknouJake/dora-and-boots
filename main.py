gameSetup()

def gameSetup():
    userName = input("Enter your name: ")

    while userName.isalpha() == False or userName == "":
        print("Please enter a valid name")
        userName = input("Enter your name: ")


    # Ask the user how many coins they want to play with
    gameSize = input(f"Hi {userName}! Enter how many coins you want to play with: ")

    # Check if the input is a number
    while gameSize.isnumeric() == False or int(gameSize) <= 0:
        print("Please enter a positive number")
        gameSize = input("Enter how many coins you want to play with: ")






