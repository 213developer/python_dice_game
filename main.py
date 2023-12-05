#Dice Game
import random


dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print(dice1)
print(dice2)
winlose = ""

dicetotal = dice1 +dice2
print(dicetotal)

#Question 1 Logic
if dicetotal == 7:
    winlose = "Win"
    print(winlose)
else:
    print(winlose)

if dicetotal == 11:
    winlose = "Win"
    print(winlose)
else:
    print(winlose)

if dicetotal == 2:
    winlose = "Lose"
    print(winlose)
else:
    print(winlose)

if dicetotal == 3:
    winlose = "Lose"
    print(winlose)
else:
    print(winlose)

if dicetotal == 12:
    winlose = "Lose"
    print(winlose)
else:
    print(winlose)



while (winlose == "Lose"):
    leftOrRight = input("Enter an L if you are left-handed,a R if you are right-handed or X to quit.")
    if leftOrRight == "L":
        leftTotal = leftTotal + 1
    elif leftOrRight == "R":
        rightTotal = rightTotal + 1





#
# while (leftOrRight== "L" or leftOrRight == "R"):
#     leftOrRight = input("Enter an L if you are left-handed,a R if you are right-handed or X to quit.")
#     if leftOrRight == "L":
#         leftTotal = leftTotal + 1
#     elif leftOrRight == "R":
#         rightTotal = rightTotal + 1

