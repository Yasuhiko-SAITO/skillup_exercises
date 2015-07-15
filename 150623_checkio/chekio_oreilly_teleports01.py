#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# N
# N
# N
# N
# N
# N
# N
# N
# N
# N
# N
# N
# N
# N
# N
#-------------------------------------------------------------------------------

a = 0
if a==0:

    teleports_string = "12,15,16,23,24,28,83,85,86,87,71,74,56"

    teleList = []
    for tele in teleports_string.split(","):
        tensValue = int(tele[0])
        onesValue = int(tele[1])
        if tensValue > onesValue:
            root = [onesValue, tensValue]
        else:
            root = [tensValue, onesValue]

        if not(root in teleList):
            teleList.append(root)

    teleList.sort()
    print teleList

    """
    teleSetList = [set(),]
    for ind in range(1, 9):
        setInd = set()
        for tele in teleList:
            if set([ind]) & set(tele):
                setInd |= set(tele)

        setInd.remove(ind)
        teleSetList.append(setInd)


    passList = [1]
    for i in teleSetList[1]:
        index = i
        passList.append(index)
        setSearch = teleSetList[index]

        while:
            index = set(passList).difference

    """








