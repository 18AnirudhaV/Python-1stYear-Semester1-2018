"""
Threshold
Author: Anirudha Verma [20128760] ~ 18AV8

This program takes a list of names and calculates which name has more than 6 characters

"""

def theThreshold():

    # The list of names are from the TV show, The Office
    theOfficeList = ["Micheal", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert", "Stanley", "Kevin", "Meredith", "Angela", "Oscar", "Phyllis", "Toby", "Creed", "Kelly"]

    # A count that goes through the list for the while loop to work
    listCount = 0

    # A count that calculates how many names have more than 6 characters
    thresholdCount = 0

    # Goes through the entire list
    while listCount < len(theOfficeList):

        # Calcutates if the name in the list is greater than 6 characters
        if len(theOfficeList[listCount]) > 6:
              thresholdCount += 1

        listCount += 1

theThreshold()
