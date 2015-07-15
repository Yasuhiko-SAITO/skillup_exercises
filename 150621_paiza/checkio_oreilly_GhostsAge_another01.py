#-------------------------------------------------------------------------------
# -*- coding:utf-8 -*-
# Ghosts age：幽霊の年齢を出力せよ 別バージョン
#
# 【ルール】
# 幽霊の透明度は10000 ~ 0で表され、
# 透明度10000が最も新しい生まれたての幽霊
# 透明度0が年齢不詳の完全透明な幽霊とする。
#
# 幽霊の年齢と透明度には以下の関係性が存在する。
# (1)幽霊の年齢がフィボナッチ数列に該当しない時、
#    今年の透明度は、前年の透明度に1を加えたものとする。
# (2)幽霊の年齢がフィボナッチ数列に該当する時、
#    今年の透明度は、前年の透明度から今年の年齢を引いた値とする。
#
# 【入力】
# opacity   透明度
#
# 【出力】
# age < 5000の間に現れない透明度を出力せよ
#
#-------------------------------------------------------------------------------

# 【方針】
# 10000以下のフィボナッチ数列リストを作成する。
# age < 5000までの透明度を、特別セットとしてまとめる。
# 0～10000のセットの中から特別セットを引いた時の残りを出力する

a = 0
if a == 0:

    opacity = 9996
    age_upper = 5000
    opacity_lower = 6000

    # フィボナッチ数列リストの作成。
    # 最後から2番目と1番目の和が、新しいフィボナッチ数。
    # 故に数列リストの-1番目と-2番目の和を足し続ける。
    fibo_list = [0, 1, 2]
    fibo = 0
    while fibo < 10000:
        fibo = fibo_list[-2] + fibo_list[-1]
        fibo_list.append(fibo)

    zeroToTenThousantOpSet = set(range(opacity_lower, 10001))

    # 0歳の透明度は10000
    age = 0
    age_opacity = 10000
    # 引数の透明度opacityと、i歳の透明度age_opacityが一致するまで繰り返す。
    zeroToFiveThousantAgeSet = set()
    while age_opacity != opacity and (age < age_upper):
        # 年齢がフィボナッチ数列リストに含まれる場合
        if age in fibo_list:
            age_opacity -= age
        # 年齢がフィボナッチ数列リストに含まれない場合
        else:
            age_opacity += 1
        zeroToFiveThousantAgeSet.add(age_opacity)
        age += 1

    if age != 0:
        age -= 1

print len(zeroToFiveThousantAgeSet)
print len(zeroToTenThousantOpSet)

"""
# ageの上限を下げた時の透明度の最小値を算出
a = list(zeroToFiveThousantAgeSet)
a.sort()
print a[0]
"""
print sorted(list(zeroToTenThousantOpSet - zeroToFiveThousantAgeSet))
print sorted(list(zeroToFiveThousantAgeSet))[0]
#"""









