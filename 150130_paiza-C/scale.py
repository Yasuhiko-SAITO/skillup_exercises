#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      admin
#
# Created:     30/01/2015
# Copyright:   (c) admin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

inp_list = raw_input().split(" ")

if inp_list[1] == "cm":
    scale = 10
elif inp_list[1] == "m":
    scale = 1000
elif inp_list[1] == "km":
    scale = 1000 * 1000


ans = int(inp_list[0]) * scale
print ans