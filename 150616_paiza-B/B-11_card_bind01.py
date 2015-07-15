#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 名刺バインダーの表(裏)面の番号を回答せよ
#
# 【ルール】
# 左綴じの名刺バインダーで、1ページに複数枚入り、左からバインド番号を数える。
# 例えば1ページ3枚入るとすると、左から順に1,2,3、めくって4,5,6番目とする。
# この時1番目の裏が6、2番目の裏が5、3番目の裏が4番目となる。
#
# 【入力】
# n m       1ページあたりに入る枚数と、バインド番号
#
# 【出力】
# m番目の名刺の表(裏)面の番号を数字で出力せよ
#
#-------------------------------------------------------------------------------

inp_list = raw_input().split(" ")

card_max = int(inp_list[0])
outside = int(inp_list[1])


i = (outside - 1) / (card_max * 2)
page_list = range(card_max * 2 * i + 1, card_max * 2 * (i + 1) + 1)

if page_list.index(outside) < len(page_list) / 2:
    target_index = page_list.index(outside) * (-1) - 1
else:
    target_index = (len(page_list) - 1) - page_list.index(outside)


print page_list[target_index]