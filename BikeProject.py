"""
Anirudha Verma ~ 20128760
Bike Share Application


"""
import urllib.request    #this loads a library you will need
import pprint
import math

def getData():
    """
    - This function will use the 'url' parameter to be : http://research.cs.queensu.ca/home/cords2/bikes.txt
    - It will then cleanse the data using the cleanseData function and input it into a list
    - It will return a list with the cleansed data
    """

    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/bikes.txt")
    html = response.readlines()  # reads one line
    data = []
    for htmlLine in html:
        data.append(htmlLine.decode('utf-8').split('\t'))

    return data

def cleanseData(uncleanedList):
    """
    - This function will take the uncleanedList and cleanse the data so that it can be sorted into a correct and
    formatted list
    - It will return the cleansed data
    """

    for stationIndex in range(1, len(uncleanedList)):
        stationData = uncleanedList[stationIndex]
        uncleanedList[stationIndex] = [int(stationData[0]), stationData[1].rstrip(), float(stationData[2]),
                                       float(stationData[3]), int(stationData[4]), int(stationData[5]),
                                       int(stationData[6])]

    uncleanedList[0][6] = uncleanedList[0][6].rstrip()

    return uncleanedList

def convertData(cleansedList):
    """
    - This will take the cleansedList in and convert it into a dictionary for an ease in programming functions
    - It will be dictionaries of dictionaries or a list within a dictionary
    - It will return a dictionary with the cleansed data
    """
    keyTemp = [key for key in cleansedList[0][1:]]
    cleanDictionary = {}
    for stationData in cleansedList[1:]:
        stationID = stationData[0]
        cleanDictionary[stationID] = {}
        for keyIndex in range(len(keyTemp)):
            cleanDictionary[stationID][keyTemp[keyIndex]] = stationData[keyIndex + 1]
    return cleanDictionary

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

    if stationID not in dataList:
        return False
    else:
        if dataList[stationID]['num_bikes_available'] > 0:
            dataList[stationID]['num_bikes_available'] = dataList[stationID]['num_bikes_available'] - 1
            dataList[stationID]['num_docks_available'] = dataList[stationID]['num_docks_available'] + 1
            return True
        else:
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

    if stationID not in dataList:
        return False
    else:
        if dataList[stationID]['num_docks_available'] > 0:
            dataList[stationID]['num_bikes_available'] = dataList[stationID]['num_bikes_available'] + 1
            dataList[stationID]['num_docks_available'] = dataList[stationID]['num_docks_available'] - 1
            return True
        else:
            return False

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
            userInput = int(input("\nEnter Your Choice Here: "))
        except ValueError:
            userInput = 0
            print("Enter a valid number from 1-5")

        # Rent Option
        if userInput == 1:
            print("If you have a station ID please enter it")
            print("Enter 0 to EXIT to the main page")

            while True:
                try:
                    rentOption = int(input("\nPlease enter a station ID:"))
                except ValueError:
                    print("Sorry, the station you have entered is invalid")
                    continue

                if rentOption == 0:
                    print("You will now be redirected back to the main menu!\n\n")
                    break

                rentTF = bikeRent(rentOption, dataList)

                if rentTF is True:
                    print("Your bike rent was successful! :D")
                    print("You will now be redirected back to the rent menu!\n\n")
                    break

                if rentTF is False:
                    print("Your bike rent was unsuccessful please use another station! :(")
                    print("You will now be redirected back to the rent menu!\n\n")
                    break

        # Return Option
        elif userInput == 2:
            print("If you have a station ID please enter it")
            print("Enter 0 to EXIT to the main page")

            while True:
                try:
                    returnOption = int(input("Please enter a station ID:"))
                except ValueError:
                    print("Sorry, the station you have entered is invalid")
                    continue

                if returnOption == 0:
                    print("You will now be redirected back to the main menu!\n\n")
                    break

                returnTF = bikeReturn(returnOption, dataList)

                if returnTF is True:
                    print("Your bike return was successful! :D ")
                    print("You will now be redirected back to the main menu!\n\n")
                    break

                if returnTF is False:
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

                # Rent
                if rentOrReturn == 1:
                    pprint.pprint(availableStations(dataList, rentOrReturn))
                    break

                # Return
                elif rentOrReturn == 2:
                    pprint.pprint(availableStations(dataList, rentOrReturn))
                    break

                # Exit
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
                except ValueError:
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
        if int(userInput) < 0 or int(userInput) > 5 and userInput != 0:
            print("Please enter a valid choice")

def stationDirection(stationID1, stationID2, dataList):
    """
    - This will take in 2 stationIDs and use the dictionary to get the latitude and longitude. It will then compare the 2 locations.
    - It will return where the location of the 2nd station is by returning a value such as “north”, “northeast”, etc.
    """

    # Assigning LL values
    A1 = dataList[stationID1]['lon']
    A2 = dataList[stationID2]['lon']
    B1 = dataList[stationID1]['lat']
    B2 = dataList[stationID2]['lat']

    # Radian direction
    y = math.sin(A2 - A1) * math.cos(B2)
    x = math.cos(B1) * math.sin(B2) - math.sin(B1) * math.cos(B2) * math.cos(A2 - A1)

    bearing = math.atan2(y, x)

    # Conditions
    if bearing < 0:
        bearing = 2*math.pi + bearing

    if bearing == 0 or bearing == 2*math.pi:
        return "EAST"
    elif bearing >= 0 and bearing < math.pi/2:
        return "NORTHEAST"
    elif bearing == math.pi/2:
        return "NORTH"
    elif bearing < math.pi and bearing > math.pi/2:
        return "NORTHWEST"
    elif bearing == math.pi:
        return "WEST"
    elif bearing > math.pi and bearing < ((3*math.pi)/2):
        return "SOUTHWEST"
    elif bearing == ((3*math.pi)/2):
        return "SOUTH"
    elif bearing > ((3*math.pi)/2) and bearing < 2*math.pi:
        return "SOUTHEAST"

def availableStations(dataList, rentOrReturn):
    """
    - This will take the cleansed dictionary and iterate through the entire dictionary and output which stations have
    available bikes that can be rented or stations that have available docks that bikes can be returned at.
        - It will list it from the station with the most number of bikes to the station with the least number and
        will not print any that are unavailable
        - This will be done for available bikes to rent or docks free to return, depending on what is asked.
    - It will return a list will both outputs.
    """

    # Rent
    if rentOrReturn == 1:
        rentList = []
        for key, value in dataList.items():
            if value['num_bikes_available'] > 0:
                rentList.append([key, value['num_bikes_available']])

        rentList.sort(key=lambda x: x[1], reverse=True)
        return rentList

    # Return
    elif rentOrReturn == 2:
        returnList = []
        for key, value in dataList.items():
            if value['num_docks_available'] > 0:
                returnList.append([key, value['num_docks_available']])

        returnList.sort(key=lambda x: x[1], reverse=True)
        return returnList

def main():
    """
    Runs the dataList collection and then the main function userInput that will then run the rest of the program
    """

    uncleanedList = getData()
    cleansedList = cleanseData(uncleanedList)
    dataList = convertData(cleansedList)
    userInput(dataList)


if __name__ == '__main__':
    main()