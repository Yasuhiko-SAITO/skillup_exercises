#-------------------------------------------------------------------------------
# coding: utf-8
##あいえう
#-------------------------------------------------------------------------------

receipt_all_num = int(raw_input())

receipt_list_str = []
for i in range(receipt_all_num):
    hoge_each_list = raw_input().split(" ")
    receipt_list_str.append(hoge_each_list)

percent_price_list = []
for rep in range(receipt_all_num):
    date_discri = int(receipt_list_str[rep][0])
    if date_discri / 10 == 3 or date_discri % 10 == 3:
        each_percent = 3
    elif date_discri / 10 == 5 or date_discri % 10 == 5:
        each_percent = 5
    else:
        each_percent = 1
    hoge_each_list = [each_percent, int(receipt_list_str[rep][1])]
    percent_price_list.append(hoge_each_list)

ans = 0
for j in range(receipt_all_num):
    ans += percent_price_list[j][0] * percent_price_list[j][1] / 100

print ans






#print "".join(map(str, ans_list))
