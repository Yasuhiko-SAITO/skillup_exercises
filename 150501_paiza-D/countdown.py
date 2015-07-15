#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     01/05/2015
# Copyright:   (c) admin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

inp_num = int(raw_input())
ans_list = []

for i in range(inp_num):
    ans_list.append(inp_num - i)

print "\n".join(map(str, ans_list))
