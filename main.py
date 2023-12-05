#Here I'm importing the random function
#This enables me to call the function later
import random

#Here I'm generating 10 random numbers and assigning them as variables
random1 = random.randint(1, 500)
random2 = random.randint(1, 500)
random3 = random.randint(1, 500)
random4 = random.randint(1, 500)
random5 = random.randint(1, 500)
random6 = random.randint(1, 500)
random7 = random.randint(1, 500)
random8 = random.randint(1, 500)
random9 = random.randint(1, 500)
random10 = random.randint(1, 500)
random11 = random.randint(1, 500)
random12 = random.randint(1, 500)
random13 = random.randint(1, 500)
random14 = random.randint(1, 500)
random15 = random.randint(1, 500)
random16 = random.randint(1, 500)
random17 = random.randint(1, 500)
random18 = random.randint(1, 500)
random19 = random.randint(1, 500)
random20 = random.randint(1, 500)

random1string = str(random1)
random2string = str(random2)
random3string = str(random3)
random4string = str(random4)
random5string = str(random5)
random6string = str(random6)
random7string = str(random7)
random8string = str(random8)
random9string = str(random9)
random10string = str(random10)
random11string = str(random11)
random12string = str(random12)
random13string = str(random13)
random14string = str(random14)
random15string = str(random15)
random16string = str(random16)
random17string = str(random17)
random18string = str(random18)
random19string = str(random19)
random20string = str(random20)


#Here I'm getting the student to input their name
studentName = input("Type your name here")

#Now I'm going to get the student tp input the answers
questionOne = input("What is " + random1string + " + " + random2string + " ?")
questionTwo = input("What is " + random3string + " + " + random4string + " ?")
questionThree = input("What is " + random5string + " + " + random6string + " ?")
questionFour = input("What is " + random7string + " + " + random8string + " ?")
questionFive = input("What is " + random9string + " + " + random10string + " ?")
questionSix = input("What is " + random11string + " + " + random12string + " ?")
questionSeven = input("What is " + random13string + " + " + random14string + " ?")
questionEight = input("What is " + random15string + " + " + random16string + " ?")
questionNine = input("What is " + random17string + " + " + random18string + " ?")
questionTen = input("What is " + random19string + " + " + random20string + " ?")




# then I am converting the string to integer with the int function
answerOne = int(questionOne)
answerTwo = int(questionTwo)
answerThree = int(questionThree)
answerFour = int(questionFour)
answerFive = int(questionFive)
answerSix = int(questionSix)
answerSeven = int(questionSeven)
answerEight = int(questionEight)
answerNine = int(questionNine)
answerTen = int(questionTen)



#Question 1 Logic
if answerOne == random1 + random2:
    score1 = 1
    print("answerOne is True")
else:
    print("answerOne is False")
    score1 = 0

#Question 2 Logic
if answerTwo == random3 + random4:
    score2 = 1
    print("answerTwo is True")
else:
    print("answerTwo is False")
    score2 = 0

#Question 3 Logic
if answerThree == random5 + random6:
    score3 = 1
    print("answerThree is True")
else:
    print("answerThree is False")
    score3 = 0

#Question 4 Logic
if answerFour == random7 + random8:
    score4 = 1
    print("answerFour is True")
else:
    print("answerFour is False")
    score4 = 0

#Question 5 Logic
if answerFive == random9 + random10:
    score5 = 1
    print("answerFive is True")
else:
    print("answerFive is False")
    score5 = 0

#Question 6 Logic
if answerSix == random11 + random12:
    score6 = 1
    print("answerSix is True")
else:
    print("answerSix is False")
    score6 = 0

#Question 7 Logic
if answerSeven == random13 + random14:
    score7 = 1
    print("answerSeven is True")
else:
    print("answerSeven is False")
    score7 = 0

#Question 8 Logic
if answerEight == random15 + random16:
    score8 = 1
    print("answerEight is True")
else:
    print("answerEight is False")
    score8 = 0

#Question 9 Logic
if answerNine == random17 + random18:
    score9 = 1
    print("answerNine is True")
else:
    print("answerNine is False")
    score9 = 0

#Question 10 Logic
if answerTen == random19 + random20:
    score10 = 1
    print("answerTen is True")
else:
    print("answerTen is False")
    score10 = 0

# Here I'm going to total up the score from each answers
totalScore = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10
# The convert the integer to a string
totalScoreString = str(totalScore)
#crate a decimal score
decimalScore = totalScore/10
#convert to string
decimalScoreString = str(decimalScore)
#convert a percentage score
percentageScore = (totalScore/10)*100
percentageScoreString = str(percentageScore)
# Then concatenate the string to print the students score
print("Chris scored " + totalScoreString + " Out of 10 correct, with a decimal score of " + decimalScoreString + " and a percentage score of " + percentageScoreString + "%")
