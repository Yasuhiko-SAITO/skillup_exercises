#-------------------------------------------------------------------------------
# coding: utf-8
# 必ずn人来るアイドルライブの収益を最大化せよ
# N M                           来場者n人、ライブ開催可能数m
# e_{1,1} e_{1,2} ... e_{1,N}   1回目のライブの、1人目からn人目までの損益
# e_{2,1} e_{2,2} ... e_{2,N}   2回目のライブの、1人目からn人目までの損益
# ...
# e_{M,1} e_{M,2} ... e_{M,N}   m回目のライブの、1人目からn人目までの損益
# 来場者の損益合計が利益となるライブのみを行い、
# このアイドルの利益の最大値を表示せよ。
#-------------------------------------------------------------------------------

inp_list = raw_input().split(" ")

human_all_num = int(inp_list[0])
live_all_num = int(inp_list[1])

price_list = []
for live_rep in range(live_all_num):
    hoge_price_list = raw_input().split(" ")
    hogege_price_list = []
    for human_rep in range(human_all_num):
        hogege_price_list.append(int(hoge_price_list[human_rep]))
    price_list.append(sum(hogege_price_list))


price_list.append(0)
price_list.sort()
ans_list = price_list[price_list.index(0):]
print sum(ans_list)