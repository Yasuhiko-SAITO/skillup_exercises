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

# N = 9959677は処理が多すぎて無理。


def FCTR_AND_ZEROCOUNT(number):
    import math

    fctr_str = str(math.factorial(number))

    fctr_idx = -1
    zero_count = 0
    while fctr_str[fctr_idx] == "0":
        zero_count += 1
        fctr_idx -= 1


    return str(len(fctr_str)) + " " + str(zero_count)


import math
print u"N = 0 のとき、", FCTR_AND_ZEROCOUNT(0), u"。"
print u"N = 1 のとき、", FCTR_AND_ZEROCOUNT(1), u"。"
print u"N = 2 のとき、", FCTR_AND_ZEROCOUNT(2), u"。"
print u"N = 5 のとき、", FCTR_AND_ZEROCOUNT(5), u"。"
print u"N = 10 のとき、", FCTR_AND_ZEROCOUNT(10), u"。"
print u"N = 20 のとき、", FCTR_AND_ZEROCOUNT(20), u"。"
print u"N = 50 のとき、", FCTR_AND_ZEROCOUNT(50), u"。"



