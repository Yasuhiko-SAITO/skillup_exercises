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
ip_list = []
ans = []
ans_TFflag = []
for inp_rep in range(input_1num):
    inp_ip = raw_input()
    ip_list.append(inp_ip)

# print ip_list

for inp_rep in range(input_1num):
    TF_flag = 0
    ip_4test = ip_list[inp_rep].split(".")
    ## 長さ判定
    ip_length = len(ip_4test)
    if ip_length == 4:
        TF_flag += 0
    else:
        TF_flag += 1

##     空欄判定
    for py_test in range(ip_length):
        if ip_4test[py_test] == "":
            TF_flag += 10
        else:
            TF_flag += 0

    ## 数値判定
    for num_test in range(ip_length):
        if ip_4test[py_test] == "":
            break
        if int(ip_4test[py_test]) > 256:
            TF_flag += 100
        else:
            TF_flag += 0

    ## 正誤判定
    if TF_flag == 0:
        ans.append("True")
    else:
        ans.append("False")

    ans_TFflag.append(TF_flag)


print "\n".join(map(str, ans))
##print ans_TFflag
##print ip_list