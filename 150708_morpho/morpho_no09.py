#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 1 ~ 4^n まで全ての数を4進数表記する。その際の"3"の個数を出力せよ。
#
# 【入力】
# N     指数N
#
#   0 <= N <= 30
#
# 【出力】
# 全ての4進数表記に現れる、"3"の個数を、数値で出力せよ。
#
#-------------------------------------------------------------------------------

a = 0
if a == 0:
    # N = 11で15秒ほどかかるため、設定に注意
    N = 9

    threeCountNum = 0
    for num in range(1, 4 ** N + 1):
        cal_num = num
        hoge_list = []

        while cal_num / 4 != 0:
            hoge_list.append(cal_num % 4)
            cal_num /= 4

        hoge_list.append(cal_num)

        threeCountNum += hoge_list.count(3)

        #"""
        print "num =", num
        print "threeCountNum =", threeCountNum
        print hoge_list
        #"""
    print threeCountNum