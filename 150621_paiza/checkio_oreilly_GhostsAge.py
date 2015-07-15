#-------------------------------------------------------------------------------
# -*- coding:utf-8 -*-
# Ghosts age：幽霊の年齢を出力せよ
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
# 幽霊の年齢を出力せよ。
#
#-------------------------------------------------------------------------------

# 【方針】
# 10000以下のフィボナッチ数列リストを作成する。
# i歳の透明度と入力された透明度が一致するまで、
# 0 ~ i歳までの透明度を計算する。

def checkio(opacity):

    # フィボナッチ数列リストの作成。
    # 最後から2番目と1番目の和が、新しいフィボナッチ数。
    # 故に数列リストの-1番目と-2番目の和を足し続ける。
    fibo_list = [0, 1, 2]
    fibo = 0
    while fibo < 10000:
        fibo = fibo_list[-2] + fibo_list[-1]
        fibo_list.append(fibo)

    # 0歳の透明度は10000
    age = 0
    age_opacity = 10000
    # 引数の透明度opacityと、i歳の透明度age_opacityが一致するまで繰り返す。
    while age_opacity != opacity and (age < 5000):
        # 年齢がフィボナッチ数列リストに含まれる場合
        if age in fibo_list:
            age_opacity -= age
        # 年齢がフィボナッチ数列リストに含まれない場合
        else:
            age_opacity += 1
        age += 1

    if age != 0:    # 最後に足した分を引く
        age -= 1

    return age

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"



