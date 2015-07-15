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

card_max = int(inp_list[0])     # 1ページあたりに入る枚数
bind_num = int(inp_list[1])     # バインド番号

# 【方針】
# バインド番号bind_numが入っている「紙番号paper_num(表裏2ページで1紙番号)」を求め、
# そのpaper_numに入るbind_numをリスト化
# その後bind_numのインデックスを調べ、
# その反対面に当たるインデックスをターゲット番号target_indexとして返す。

# 紙番号(0 <= paper_num)を算出する
# paper_numには、card_maxの2倍の量が入り、
# そのカード番号は、2 * card_max * paper_num + 1 <= bind_num <= 2 * card_max * (paper_num + 1)である。
paper_num = (bind_num - 1) / (card_max * 2)
page_list = range(card_max * 2 * paper_num + 1, card_max * 2 * (paper_num + 1) + 1)
# このリストは2つの性質を持つ
# (1)必ず長さが偶数
# (2)ルールを満たす時に、バインド番号とターゲット番号の和が、リストの長さ-1となる。
target_index = (len(page_list) - 1) - page_list.index(bind_num)

print page_list[target_index]

