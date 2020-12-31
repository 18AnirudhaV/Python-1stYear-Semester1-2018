"""
Machine Epsilon
Author: Anirudha Verma [20128760] ~ 18AV8

This program calculates the smallest value that is greater than 1.0 but is distinguishable from 1.0 on a given machine.

"""

def machineEpsilon():
    keyValue = 1.0
    placeHolder = -9999

    # This while loop continues to divide the keyValue until it hits 1.1110e-16, which is the closest value to 0 in a 64-bit computer
    while True:

        # placeHolder for the last value of the keyValue in order for it to be as close as possible to the value 0
        placeHolder = keyValue

        keyValue = keyValue / 2.0

        if 1.0 + keyValue == 1.0:
            # As the placeHolder holds the value that is closest to 0, adding 1 allows for the smallest value greater than 1 to be printed
            return placeHolder + 1

machineEpsilon()
