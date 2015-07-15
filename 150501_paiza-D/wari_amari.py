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

inp_list = raw_input().split(" ")

m = int(inp_list[0]) / int(inp_list[1])
n = int(inp_list[0]) % int(inp_list[1])

print str(m) + " " + str(n)