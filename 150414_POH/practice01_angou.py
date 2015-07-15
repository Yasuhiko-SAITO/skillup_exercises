#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     14/04/2015
# Copyright:   (c) admin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#入力された文字列の奇数番目を抽出して返す

inp_str = raw_input()
ans = ""
rep = len(inp_str) / 2  #繰り返し回数

for i in range(rep):
    ans = ans + inp_str[2 * i]

if len(inp_str) % 2 == 1:   #長さが奇数の時、最後の文字を付け加える
    ans = ans + inp_str[-1]

print ans

