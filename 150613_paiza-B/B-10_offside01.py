#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# オフサイドかどうかを判定して、その選手の番号を出力せよ
#
# 【ルール】
# AチームとBチームがサッカーで対戦する。
# Aチームのゴール座標を0、センターラインの座標を55、Bチームのゴール座標を110とし、
# ゴール座標からセンターラインを含まない範囲を自陣、
# センターラインや相手ゴール座標を含めた範囲を敵陣とする。
#
# 以下の4条件を同時に満たした時に、オフサイドと判定されることとする。
# (1)味方からパスを受ける
# (2)パスを受ける人(passee)が敵陣地に居る
# (3)パスを出した人(passer)よりも、passeeが敵ゴールに近い位置にいる。
#   　ただし、passerとpasseeが同位置の場合は、オフサイドにならない。
# (4)キーパーを除く、最もゴールに近い敵(最終ライン)よりも、passeeがゴールに近い位置にいる
#   　ただし、その敵とpasseeが同位置の場合は、オフサイドにならない。
#
# 【入力】
# Name_T Num        チーム名と番号
# A_1 A_2 ... A_11  Aの1番目から11番目までの選手の、それぞれの座標
# B_1 B_2 ... B_11  Bの1番目から11番目までの選手の、それぞれの座標
# ただし、Name_Tは"A"か"B"のいずれか、1 <= Num <= 11、
# 0 <= (A_i and B_j) <= 110 (1 <= (i and j) <= 11)とする。
#
# 【出力】
# オフサイド判定される選手が、チーム内で何番目の選手かなのか、数値で出力せよ。
# 複数人いる場合は、改行で出力し、該当者が居ない場合は"None"を出力せよ。
#
# 【初採点】
# 境界値データでミス87点、問題文が悪い。
# センターライン上を敵陣に含むかどうか書いていなかった。
# (「チームAの陣はx座標が0以上55以下の位置で、
#  チームBの陣はx座標が55以上110以下の位置」という表記。
# これではセンターライン上はどちらなのか、判断できない。)
#-------------------------------------------------------------------------------

first_inp_list = raw_input().split(" ")
A_posi_hoge = raw_input().split(" ")    # Aチームのポジションの文字列のリスト
B_posi_hoge = raw_input().split(" ")    # Bチームのポジションの文字列のリスト

passer = int(first_inp_list[1])         # パスを出す人(passer)のインデックス+1


# 攻撃側と防御側の各選手の座標をリストにする
# このとき、攻撃チームによって判定条件が変わらないようにするため、
# Bチームが攻撃の時は、全ての座標を負にする。
# これによって、どちらのチームが攻撃でも、大小判定が変わらなくなる。
attack_posi = []
defence_posi = []

if first_inp_list[0] == "A":        # 攻撃側がAチームだった場合
    for i in range(11):
        attack_posi.append(int(A_posi_hoge[i]))
        defence_posi.append(int(B_posi_hoge[i]))
        center_line = 55

else:                               # 攻撃側がBチームだった場合
    for i in range(11):
        attack_posi.append(int(B_posi_hoge[i]) * -1)
        defence_posi.append(int(A_posi_hoge[i]) * -1)
        center_line = -55


# パスを受ける人で条件3に該当する者を選び、
# その後条件2と条件4に該当する者を選ぶ
passee_index = []   # 条件3に該当するパスを受ける人(passee)のインデックスのリスト
for passer_rep in range(11):
    # passerの座標がpasseeの座標より小さい時、passeeのインデックスをリストに加える。
    if attack_posi[passer - 1] < attack_posi[passer_rep]:
        passee_index.append(passer_rep)

# キーパーを除く、最終ディフェンスを探す。
defence_posi.sort()
last_defence = defence_posi[-2]

ans_list = []
for passee_rep in passee_index:
    # 条件2と条件4を満たすpasseeのインデックスを加える。
    if (center_line <= attack_posi[passee_rep]) and \
    (last_defence < attack_posi[passee_rep]):
        ans_list.append(passee_rep + 1)

# 誰も条件に該当しない時。
if ans_list == []:
    ans_list = ["None"]

print "\n".join(map(str, ans_list))