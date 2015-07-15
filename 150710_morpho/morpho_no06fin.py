#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 株式会社モルフォ　新卒採用チャレンジ問題No.6
# http://www.morphoinc.com/careers/challengeTest_6.html
# 正の整数Nの階乗(N!)の桁数、及び、末尾に続く0の個数を出力せよ。
#
# 【入力】
# N     0 <= N <= 10^7
#
# 【出力】
# keta count_zero   N!の桁数ketaと末尾に続く0の個数count_zero
#
# 【例題と回答】
# N = 0 のとき、0! = 1のため、出力は 1 0
# N = 1 のとき、1! = 1のため、出力は 1 0
# N = 2 のとき、2! = 2のため、出力は 1 0
# N = 5 のとき、5! = 120のため、出力は 3 1
# N = 10 のとき、10! = 1のため、出力は 7 2
# N = 20 のとき、20! = 1のため、出力は 19 4
# N = 50 のとき、50! = 1のため、出力は 65 12
# N = 9959677 のとき、出力は 65374834 2489916
#
#-------------------------------------------------------------------------------

# math.factorialを使って階乗の計算すると、
# 10＾5以上は処理過多となる。
# 処理過多ではなかったら、文字列に変換して、
# 桁数＝長さ、末尾の0はインデックス-1から調べれば良かったのだが・・・。
#   そこで、対数を用いる。
# logN! = logN + log(N-1) + ... + log1であり、
# 10^i <= N! <= 10^(i + 1)とすると、log10を取ると、
# i <= logN! <= i + 1。
# つまり対数の和の整数部分が、桁数i + 1に等しくなる。
#   また、末尾の0の個数は、10が関係していて、
# 10の素材(= 2 * 5)から、5の個数を考える。
# N / 5の商がjの時、Nに含まれる5は、[5 * 1, 5 * 2, ..., 5 * j]のj個である。
# 更にjに含まれる5の数、それに含まれる5の数・・・という形で調べていけば、
# N!を素因数分解した際の5の指数(すなわち5の個数)が算出できる。


def FCTR_AND_ZEROCOUNT(number):
    # 対数の計算のため、mathをインポート
    import math

    # 桁数のカウント
    digit_count = 0
    for i in range(1, number + 1):
        digit_count += math.log10(i)

    # 数値を割っていくための変数を設定
    number_to_zero = number
    zero_count = 0
    while number_to_zero > 0:
        # 5で割った時の個数を算出
        zero_count += number_to_zero / 5
        number_to_zero /= 5

    # 10^i <= N!を考えていて、iは左辺の0の個数に等しい。すなわち桁数はi + 1。
    # logN!は小数型なので、整数型に。
    return str(int(digit_count) + 1) + " " + str(zero_count)


import math
print u"N = 0 のとき、", FCTR_AND_ZEROCOUNT(0), u"。"
print u"N = 1 のとき、", FCTR_AND_ZEROCOUNT(1), u"。"
print u"N = 2 のとき、", FCTR_AND_ZEROCOUNT(2), u"。"
print u"N = 5 のとき、", FCTR_AND_ZEROCOUNT(5), u"。"
print u"N = 10 のとき、", FCTR_AND_ZEROCOUNT(10), u"。"
print u"N = 20 のとき、", FCTR_AND_ZEROCOUNT(20), u"。"
print u"N = 50 のとき、", FCTR_AND_ZEROCOUNT(50), u"。"
print u"N = 9959677 のとき、", FCTR_AND_ZEROCOUNT(9959677), u"。"
print u"N = 10^7 のとき、", FCTR_AND_ZEROCOUNT(10 ** 7), u"。"

