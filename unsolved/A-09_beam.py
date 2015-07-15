#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# N
# N
# N
# N
# N
# N
# N
# 60点。基本データ4つでランタイムエラー。
#-------------------------------------------------------------------------------

inpNumList = raw_input().split(" ")

boxMtx = []
for i in range(int(inpNumList[0])):
    boxMtx.append(list(raw_input()))


colIdx = 0
rowIdx = 0

DrtList = ["r", "d", "l", "u"]
currDrtIdx = 0
currDrt = DrtList[currDrtIdx]
count = 0
while (colIdx < int(inpNumList[0]) and colIdx >= 0) and \
(rowIdx < int(inpNumList[1]) and rowIdx >= 0):

    if boxMtx[colIdx][rowIdx] == "/":
        if currDrt == "r" or currDrt == "l":
            currDrtIdx -= 1
        else:
            currDrtIdx += 1
    elif boxMtx[colIdx][rowIdx] == "\\":
        if currDrt == "r" or currDrt == "l":
            currDrtIdx += 1
        else:
            currDrtIdx -= 1

    currDrt = DrtList[currDrtIdx]
    if currDrt == "r":
        rowIdx += 1
    elif currDrt == "l":
        rowIdx -= 1
    elif currDrt == "d":
        colIdx += 1
    elif currDrt == "u":
        colIdx -= 1

    count += 1

print count





