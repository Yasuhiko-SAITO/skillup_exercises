#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      admin
#
# Created:     30/01/2015
# Copyright:   (c) admin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

inp_str = raw_input()
alph_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph_list = list(alph_str)

for num in range(len(alph_list)):
    if alph_list[num] == inp_str:
        break
    else:
        continue


print num + 1