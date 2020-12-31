"""
Anirudha Verma ~ 20128760
Short Assignment 6
"""

def squareAndSum(sampleList, i=0):
    """
    Squares all the elements of a list and then returns sum of the numbers squared
    """

    if i > len(sampleList) - 1:
        return sum(sampleList)
    sampleList[i] **= 2

    return squareAndSum(sampleList, i+1)

def compareLists(list1, list2, i=0):
    """
    Returns:
    - False: list1 and list2 have different lengths
    - True: list1 and list2 are identical
    - the index of the first mismatched elements between the lists
    """

    if len(list1) != len(list2):
        return False
    elif i == len(list1):
        return True
    elif list1[i] != list2[i]:
        return False
    else:
        i = i + 1
        return compareLists(list1, list2, i)

def machineEpsilon(sample = 1):
    """
    Returns machine epsilon
    """

    if 1 + sample == 2:
        return sample * 2
    else:
        return machineEpsilon(sample/2)