'''
Anirudha Verma ~ 20128760 ~ 1st Oct. 2018
Assignment #1

This program creates a word game in which 2 random letters are generated. The user much create a word that starts and
ends with those 2 letters. It must first clean a word list that is given to remove nonsense words such as 'aaa'.

'''

import random
import urllib.request  # This loads a library you will need - put this at top of file.
import string # Used for the string.ascii_lowercase which presents all the letters in the alphabet

'''
This function allows the word list to be read and created into a list in order for it to be cleansed and used.
'''
def readWordList():
    response = urllib.request.urlopen("http://www.mit.edu/~ecprice/wordlist.10000")
    html = response.read()
    data = html.decode('utf-8').split()
    return data

'''
This function cleans the list given. It removes 'words' that are made up of the same letter multiple times and returns
a cleansed list
E.g. 'aaaa'
'''
def cleanse():
    # Calls the function readWordList() so that it is not called upon multiple times while going through the for loop
    wordList = readWordList()

    # Creates an empty list for the cleansed words to be appended into
    cleansed_list = []

    # For loop that iterates through the entire word list
    for count in range(len(wordList)):
        # Nested for loop that iterates through each letter of the word
        for countLetter in range(len(wordList[count])):
            # If the word is 1 letter, it is submitted into the cleansed list or if the letters are not repeated
            if len(wordList[count]) == 1 or wordList[count][countLetter] != wordList[count][0]:
                # Appending to the new clean list
                cleansed_list.append(wordList[count])
                break

    # Returns the cleansed list for it to be used
    return cleansed_list

'''
This is a testing function I used to check if the cleanse function is working or not
THIS IS NOT RUN OR USED 
'''
def testingCleanse():

    # Using the small list created
    response = urllib.request.urlopen("http://www.cs.queensu.ca/home/cords2/shortList.txt")
    html = response.read()
    data = html.decode('utf-8').split()


    # Creates an empty list for the cleansed words to be appended into
    cleansed_list = []

    # For loop that iterates through the entire word list
    for count in range(len(data)):
        # Nested for loop that iterates through each letter of the word
        for countLetter in range(len(data[count])):
            # If the word is 1 letter, it is submitted into the cleansed list or if the letters are not repeated
            if len(data[count]) == 1 or data[count][countLetter] != data[count][0]:
                # Appending to the new clean list
                cleansed_list.append(data[count])
                break

    # Returns the cleansed list for it to be used
    return cleansed_list

'''
This function takes the word that is submitted in each round and calculates how many points to give or take.
It takes in the parameters from the play() function of the inputted answer, random start and end letters and the word 
list that is being used. It returns the scoring of the word inputted.
'''
def scoring(answerInput, letter1, letter2, wordList):
    
    # Initializes the score of this particular round to be 0
    score = 0
    
    # Dictionary that gives each letter a value
    letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 5, 'g': 2, 'h': 3, 'i': 1, 'j': 9, 'k': 5, 'l': 1,
                     'm': 2, 'n': 2, 'o': 1, 'p': 4, 'q': 15, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 8, 'w': 4, 'x': 15,
                     'y': 4, 'z': 15}

    
    # Checks to see if the the answer given matches the random letters chosen in the particular round
    # (As per Prof. Poweley's: score will -2 than -10 if a word is not in the dictionary and does not match the letters)
    if answerInput[0] != letter1 or answerInput[-1] != letter2:
        score -= 2

    # If the answer is not in the given word list they will loose 10 points
    elif answerInput not in wordList:
        score -= 10

    # If the answer is in the word list and equals the random letters at the start and end it will calculate the score
    elif answerInput[0] == letter1 and answerInput[-1] == letter2 and answerInput in wordList:

        # Uses the dictionary as it iterates through each letter to add to the score
        for wordLength in range(len(answerInput)):
            score += letter_values[answerInput[wordLength]]

        # If the start and end letter is the same then they get a bonus 10 points
        if answerInput[0] == answerInput[-1]:
            score += 10

        # If the word is 6 characters long they get a bonus of 3 points
        if len(answerInput) == 6:
            score += 3

        # If the word is 7 characters long they get a bonus of 4 points
        elif len(answerInput) == 7:
            score += 4

        # If the word is 8 characters long they get a bonus of 5 points
        elif len(answerInput) == 8:
            score += 5

        # If the word is  greater than 8 characters they get a bonus of 6 points
        elif len(answerInput) > 8:
            score += 6

    # Returns the score as per the round
    return score


'''
This function checks if the user wants to continue playing for another round or if they wish to quit after a particular
round.
'''
def anotherRound():

    # Takes and input from the user
    anotherRound = input("Do you wish to play another round? [Y/N]: ")

    # Boolean
    yes = True

    # If they want to play, it will do nothing and return true
    if anotherRound == "Y" or anotherRound == "y":
        pass

    # If they want to stop playing, it will make the boolean yes False and will stop the loop in the play() function
    elif anotherRound == "N" or anotherRound == "n":
        yes = False

    return yes

'''
This function essentially initializes the game.
It takes the cleansed list, creates 2 random letters for the start and end letters and takes the input of the user.
It then calls on the scoring() function in order to give the score for that particular round which is then added on to 
the total score that the user has gained or lost.
It also then checks if they want to continue playing.
'''
def play():
    wordList = cleanse()
    finalScore = 0

    # As there are 5 rounds it loops the process 5 times.
    for round in range(5):
        # Generates the random letter (no need for another function as it is 2 lines)
        letter1 = string.ascii_lowercase[random.randint(0, 25)]
        letter2 = string.ascii_lowercase[random.randint(0, 25)]
        
        # Takes an input from the user
        answerInput = input("Make a word that starts and ends with " + letter1 + " and " + letter2 + ": ")
        
        # Makes the answer lowercase in order for the scoring function to work
        answerInput = answerInput.lower()
        
        # Parses the required variables for the scoring function to work
        finalScore += scoring(answerInput, letter1, letter2, wordList)

        # Checks if they wamt to play another round
        if round < 4:
            print("Your current score is: " + str(finalScore) + " ")
            if anotherRound() == False:
                break

    # Returns the finalScore in order for it to be displayed
    return finalScore

'''
This calls for the game to be played. It has a little introduction to the game and then outputs the score the user 
obtains after playing the 5 rounds.
'''
def mainGame():
    # Introduction
    print("Hello, welcome to the best word game you will ever play!")
    print("In this game you will try to find a word that starts and ends with a random letter")
    print("Be careful! You can loose points if your answer is not a word!\n")

    # Runs the actual game and casts the score to a string in order for it to be displayed
    finalScore = str(play())

    # Outputs the total score the user has gotten
    print("Your final score is: " + finalScore)

mainGame()