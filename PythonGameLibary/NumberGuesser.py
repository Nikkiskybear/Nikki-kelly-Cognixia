import random


def pickNumber():
    number = random.randint(0, 1000)
    return number

def getGuess():
    guess = -1
    while guess == -1:
        try:
            guess = input("Please enter your guess enter save to quit and save your progress: ")
            if guess != "save":
                guess = int(guess)
            else:
                guess = -5

        except:
            print("Not a int")
        else:
            if guess == -5:
                print("saving")
            elif guess < 0 or guess > 1000:
                print("Not in range")
                guess = -1
    return guess

def loadSave():

    try:
        save = open("save.txt")
        lines = save.readlines()

        lastGuess = lines[0]
        highLow = lines[1]
        target = lines[2]
    except:
        print("there is no vaild save starting a new game")
        lastGuess = -1
        highLow = "low"
        target = pickNumber()

    return lastGuess, highLow, target



def NumberGuesser():
    targetNum = pickNumber()

    load = ""
    while load != "yes" and load != "no":
        load = input("Do you want to load the last saved game Yes or No: ")
        print(load)
    if load == "yes":
        lastGuess, highLow, targetNum = loadSave()
        targetNum = int(targetNum)
        print("Your last guess was " + str(lastGuess) + " It was to " + str(highLow))


    guessNum = -1

    while guessNum != targetNum:
        lastGuess = guessNum
        guessNum = getGuess()

        if guessNum == -5:
            save = open("save.txt", "w")
            save.write(str(lastGuess) + "\n")
            if lastGuess > targetNum:
                save.write("high\n")
            elif lastGuess < targetNum:
                save.write("low\n")
            save.write(str(targetNum) + "\n")
            save.close()
            break
        else:
            if guessNum > targetNum:
                print("Your Guess of " + str(guessNum) + " is to high")
            elif guessNum < targetNum:
                print("Your Guess of " + str(guessNum) + " is to low")
            elif guessNum == targetNum:
                print("Congratz you guessed the number! ")

