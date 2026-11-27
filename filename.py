
# LAB 1 - Hello, World
print("Hello, World")


# LAB 2 - Numeric Data Types
print("Python has three numeric types: int, float, and complex")

myValue = 1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the dados type " + str(type(myValue)))

myValue = 3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the dados type " + str(type(myValue)))

myValue = 5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the dados type " + str(type(myValue)))

myValue = True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the dados type " + str(type(myValue)))

myValue = False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the dados type " + str(type(myValue)))


# LAB 3 - String Data Types
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the dados type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name, color, animal))


# LAB 4 - Lists, Tuples and Dictionaries
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2] = "orange"
print(myFruitList)

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

myFavoriteFruitDictionary = {
    "Akua": "apple",
    "Saanvi": "banana",
    "Paulo": "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

# LAB 5 - CONDITIONALS: IF AND ELSE

userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

# LAB 5 - CONDITIONALS: IF, ELIF AND ELSE

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")

# LAB 6 - WHILE LOOP

import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1, 10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")

    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))

    # LAB 6 - FOR LOOP

    print("Count to 10!")

    for x in range(0, 11):
        print(x)