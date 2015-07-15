#-------------------------------------------------------------------------------
# coding:utf-8
# モンテカルロ法から、円周率piを計算する。

# 原点から(1, 1)の範囲に複数の点をランダムに打つ。
# そして円内に入っている個数の割合を計算する。
# 打つ点の個数が多いほど、その割合はpi / 4に近づく
# すなわち、円内の点の個数の割合に4をかければ、円周率を求められる。

# 点の個数は10の累乗数分だけ自由に設定し、
# 点の個数、計算された円周率、実際の誤差を
# 改行で答えよ。
#-------------------------------------------------------------------------------

import random
import math

print "桁数を入力せよ(8桁以上は時間がかかりすぎて非推奨) "

# 計算する点のリストを作成。
# 今回は桁数毎にリストを作る。
posi_all_list = []
for rep in range(int(raw_input())): # 桁数を設定
    posi_list = []
    for i in range(10 ** rep):  # 10^(0～n-1)回繰り返す
        posi_x = random.random()
        posi_y = random.random()
        posi = [posi_x, posi_y]
        posi_list.append(posi)
    posi_all_list.append(posi_list)

# 計算パート
ans_list = []
for rep in range(len(posi_all_list)):
    discri_posi_list = posi_all_list[rep]   # 計算用に、点の全リストから抽出
    cul = 0
    for discri_rep in range(len(discri_posi_list)):
        discri_num = discri_posi_list[discri_rep][0] ** 2 + discri_posi_list[discri_rep][1] ** 2
        # 円内に入っているか判別
        if discri_num > 1:  #入ってない時
            cul += 0
        else:
            cul += 1
    pi_cul = cul / float(len(discri_posi_list)) * 4 #入っている個数 / 計算した個数
    error = pi_cul - math.pi
    ans_list.append(["n = %d" %(10 ** rep),"calculated pi = %f" %pi_cul, "error = %f" %error])

print "\n".join(map(str, ans_list))

