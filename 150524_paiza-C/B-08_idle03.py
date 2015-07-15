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

# 実行時間は短縮できたが、ランタイムエラーが増えてしまった。なんでだろ？
#-------------------------------------------------------------------------------

inp_list = raw_input().split(" ")

human_all_num = int(inp_list[0])    # 来場者n
live_all_num = int(inp_list[1])     # ライブ開催可能数m

if human_all_num != 0 and live_all_num != 0:
    price_list = []                     # 利益合計額
    for live_rep in range(live_all_num):
        hoge_price_list = raw_input().split(" ")
        price = 0                       # 損益合計額
        # そのライブでの損益合計額を算出
        for human_rep in range(human_all_num):
            price += int(hoge_price_list[human_rep])
        # 損益合計額が0以上なら
        if price > 0:
            price_list.append(price)

price_list.append(0)
print sum(price_list)