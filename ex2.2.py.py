"""
Babylonian
Author: Anirudha Verma [20128760] ~ 18AV8

This program calculates a non-negative square root of a non-negative number, without using the square root function inbuilt

"""

def babylonian():

    # The non-negative number chosen is 25, as the square root is 5
    numberChosen = 25
    keyValue = numberChosen
    placeHolder = -9999

    while True:

        # placeHolder keeps the value before the keyValue is evaluated
        placeHolder = keyValue
        keyValue = (keyValue + numberChosen / keyValue) / 2.0

        if placeHolder == keyValue:
            return keyValue

babylonian()