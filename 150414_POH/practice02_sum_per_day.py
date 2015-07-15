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
#各曜日ごとの売上を合計して改行出力する
#入力値はn s_1 s_2 ... s_nで、
#nは7の倍数

rep_num = int(raw_input())
sales_inp_list = []
sum_monday = 0
sum_tuesday = 0
sum_wednesday = 0
sum_thursday = 0
sum_friday = 0
sum_saturday = 0
sum_sunday = 0
sum_all = [sum_monday, sum_tuesday, sum_wednesday, sum_thursday, sum_friday, sum_saturday, sum_sunday]

for i in range(rep_num):
    sales_inp_list.append(int(raw_input()))


for i in range(7):
    sum_hoge = 0
    for j in range(rep_num / 7):
        sum_hoge += sales_inp_list[j * 7 + i]
    sum_all[i] = sum_hoge

print "\n".join(map(str, sum_all))


