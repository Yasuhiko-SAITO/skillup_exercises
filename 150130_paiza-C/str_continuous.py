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

input_1num = int(raw_input())
Hel = ["Hello"]
inp_list = []
for inp_rep in range(input_1num):
    inp_str = raw_input()
    inp_list.append(inp_str)
ans = ",".join(map(str, inp_list)) + "."
Hel.append(ans)

print " ".join(map(str, Hel))