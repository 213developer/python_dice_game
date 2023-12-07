# import modules
import random
import sys

# start the game
a = input("Ready to start? Type 'yes' or 'no'\n")
if a.lower() == "no":
    sys.exit()
else:
    print("Good luck!")


#game logic
if a.lower() == "yes":
    print('''Player 1''')

elif a.lower() == "no":
    print("Ok then")


# Function for dice throw
def diceNumber():
    _ = input("press enter to roll ")

    # Get random number 1-6
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)

    # this returns the dice number as a tuple
    return (die1, die2)


# This is a function to get the sum of the dice roll
def twoDice(dices):
    die1, die2 = dices
    print("the sum of the dice is: {} + {} = {}".format(die1, die2, sum(dices)))


# Here we will call the dice throw function to get a value. We will return the roll and store it
value = diceNumber()
twoDice(value)

# Here we will use the sum function in value to get the sum of two outcomes
sum_of_dices = sum(value)

# Here we will check if the player is a winner when the sum equals 7 or 11 to
if sum_of_dices in (7, 11):
    result = "congratulations you won"

# Here we will check if the player lost if the sum equals 2 3 or 12
elif sum_of_dices in (2, 3, 12):
    result = "you lost, \ntry again next time"

# Here we will keep playing until the player wins or loses.
else:
    result = "continue your game please"
    currentpoint = sum_of_dices
    print("Your current dice total is", currentpoint)

# Here the game will continue until the player wins or loses.
while result == "continue your game please":
    value = diceNumber()
    twoDice(value)
    sum_of_dices = sum(value)


    if sum_of_dices in (7, 11):
        result = "congratulations you won"

    # Here we will check if the player lost if the sum equals 2 3 or 12
    elif sum_of_dices in (2, 3, 12):
        result = "you lost, \ntry again next time"


# When the player wins or loses the outcome will be printed here
if result == "congratulations you won":
    print("You Win")
    print("You have a total of 1 Win")

else:
    print("You Lose")
    print("You have a total of 1 Lose")
