"""
Anirudha Verma ~ 20128760
Bike Share UI Implementation

This is the user implementation phase of the Toronto Bike Share Application
It includes all the UI functionality and stub functionality as well.

Assumptions:
- Anything that needs to be checked with the dataList will not be there as there is no dataList created

"""

def getData():
    """
    - This function will use the 'url' parameter to be : http://research.cs.queensu.ca/home/cords2/bikes.txt
    - It will then cleanse the data using the cleanseData function and input it into a list
    - It will return a list with the cleansed data
    """
    pass

def cleanseData(uncleanedList):
    """
    - This function will take the uncleanedList and cleanse the data so that it can be sorted into a correct and
    formatted list
    - It will return the cleansed data
    """
    pass

def convertData(cleasnedList):
    """
    - This will take the cleansedList in and convert it into a dictionary for an ease in programming functions
    - It will be dictionaries of dictionaries or a list within a dictionary
    - It will return a dictionary with the cleansed data
    """
    pass

def bikeRent(stationID, dataList):
    """
    - This function allows the user to rent a bike
    - It checks if a bike is available(bikesAvailable) at the station (stationID/Name) they have chosen
	- It will return a true or false signaling if they can rent or can’t rent a bike at the chosen station
	- If true it will allow them to take a bike and it will reduce the number of bikes at a certain station and all
	other values that correspond to a bike being rented (docksAvailable, etc)
	    - Done through the checkStation function
	- If false it will direct them to the closest available station through stationDirection() and checkStation()
    """

    # For a stub, this will return false and show the closest available station that they can rent a bike at
    checkStation(stationID, dataList)
    return False

def bikeReturn(stationID, dataList):
    """
    - This function allows the user to return a bike they have rented
    - It checks if a dock is available at the station they have chosen or going to
	- It will return a true or false signaling if they can rent or can’t return a bike at the chosen station
	(as they can return at any station available)
	- If they can return the bike at the chosen station it will reduce the amount of docks available at that station
	and all other values that correspond to a bike being returned such as bikesAvailable, etc.
	    - Done through the checkStation function
	- If false it will direct them to the closest available station through stationDirection() and checkStation()
    """

    # For a stub, this will return false and show the closest available station that they can return a bike at
    checkStation(stationID, dataList)
    return False

def checkStation(stationID, cleansedDict):
    """
    - This will be used in most functions to return the values of each station that is asked to be checked.
    However, this function can be called on in order to check beforehand the amount of available bikes
    and docks at the station.
    - It will take in the stationID that needs to be checked as well as the cleansed dictionary as parameters.
    - It will return what is inside dictionary at the chosen stationID and the function it is implemented inside
    will take the necessary values for its own calculations
    """

    # For the stub, it will return sample station that is available

    return "Station 7031, Station 7234"

def userInput(dataList):
    """
    - This will control the user's commands and what they wish to do
    """
    while True:

        dataList = dataList

        # Instructions / Main Page
        print("\nTo RENT a bike ENTER 1")
        print("To RETURN a bike ENTER 2")
        print("To see all AVAILABLE STATIONS a bike ENTER 3")
        print("To check where the NEAREST STATION is ENTER 4")
        print("To EXIT the program ENTER 5")

        try:
            userInput = int(input("\n"))
        except ValueError:
            userInput = 0
            print("Enter a valid number from 1-5")

        # Rent Option
        if userInput == 1:
            print("If you have a station ID please enter it, otherwise enter 0 and check all available stations")

            while True:
                try:
                    rentOption = int(input("Please enter a station ID:"))
                except ValueError:
                    print("Sorry, the station you have entered is invalid")
                    continue

                if rentOption == 0:
                    print("You will now be redirected back to the main menu!\n\n")
                    break
                elif bikeRent(rentOption, dataList) == True:
                    print("Your bike rent was successful! :D")
                    print("You will now be redirected back to the main menu!\n\n")
                    break
                elif bikeRent(rentOption, dataList) == False:
                    print("Your bike rent was unsuccessful please use another station! :(")
                    print("You will now be redirected back to the main menu!\n\n")
                    break

        # Return Option
        elif userInput == 2:
            print("If you have a station ID please enter it, otherwise enter 0 and check all available stations")

            while True:
                try:
                    returnOption = int(input("Please enter a station ID:"))
                except ValueError:
                    print("Sorry, the station you have entered is invalid")
                    continue

                if returnOption == 0:
                    print("You will now be redirected back to the main menu!\n\n")
                    break
                if bikeRent(returnOption, dataList) == True:
                    print("Your bike return was successful! :D ")
                    print("You will now be redirected back to the main menu!\n\n")
                    break
                elif bikeRent(returnOption, dataList) == False:
                    print("Your bike return was unsuccessful please use another station! :(")
                    print("You will now be redirected back to the main menu!\n\n")
                    break

        # Check Available Option
        elif userInput == 3:
            print("If you want to check the available stations to rent enter 1")
            print("If you want to check the available stations to return enter 2")
            print("If you want to exit and go back enter 0")

            while True:
                try:
                    rentOrReturn = int(input("What do you wish to do: "))
                except ValueError:
                    print("Invalid choice, please try again.")
                    continue

                if rentOrReturn == 1:
                    rentOrReturn = "rent"
                    availableStations(dataList, rentOrReturn)
                    break
                elif rentOrReturn == 2:
                    rentOrReturn = "return"
                    availableStations(dataList, rentOrReturn)
                    break
                elif rentOrReturn == 0:
                    break

        # Nearest Station
        elif userInput == 4:
            print("Please enter the current station you are at and then the station you wish to go to.")
            print("If you wish to exit please enter 0 for both stations")

            while True:
                try:
                    stationID1 = int(input("1st Station ID: "))
                    stationID2 = int(input("2nd Station ID: "))
                except:
                    print("Invalid station, please try again")
                    continue

                if stationID1 and stationID2 == 0:
                    break

                #Will check if station is in list and then proceed and be in an if statement
                print("Please proceed: " + stationDirection(stationID1, stationID2, dataList))
                break

        # Exit program
        elif userInput == 5:
            print("THANK YOU AND HAVE A GREAT DAY!! :D")
            break

        # Correct values
        if int(userInput) < 0 or int(userInput) > 3 and userInput != 0:
            print("Please enter a valid choice")

def stationDirection(stationID1, stationID2, cleansedDict):
    """
    - This will take in 2 stationIDs and use the dictionary to get the latitude and longitude. It will then compare the 2 locations.
    - It will return where the location of the 2nd station is by returning a value such as “north”, “northeast”, etc.
    """
    return "NORTHEAST"

def availableStations(cleansedDict, rentOrReturn):
    """
    - This will take the cleansed dictionary and iterate through the entire dictionary and output which stations have
    available bikes that can be rented or stations that have available docks that bikes can be returned at.
        - It will list it from the station with the most number of bikes to the station with the least number and
        will not print any that are unavailable
        - This will be done for available bikes to rent or docks free to return, depending on what is asked.
    - It will return a list will both outputs.
    """

    return "Station 7031: 5 bikes free, 4 docks free, latitude is 5, longitude is 10"

def main():
    """
    Runs the dataList collection and then the main function userInput that will then run the rest of the program
    """

    uncleanedList = getData()
    cleansedList = cleanseData(uncleanedList)
    dataList = convertData(cleansedList)
    userInput(dataList)

main()