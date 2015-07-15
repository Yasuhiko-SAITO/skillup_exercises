#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 株式会社モルフォ　新卒採用チャレンジ問題No.8
# http://www.morphoinc.com/careers/challengeTest_8.html
# あるルールに従って、数直線上の0からNまで移動するときの、移動回数を算出せよ。
#
# 【ルール】
# 移動のルールは以下の通りとする。
# (1)移動1回目は移動量1
# (2)移動2回目以降の移動量は、前回の移動量と同じ、あるいはその2倍とする。
# (3)移動量を減らすことはできない。
# (4)移動方向は正のみである。
# (5)ゴールのNを通りすぎてはいけない。
#
# 【入力】
# N         目的地(ただし1 <= N <= 10^18)
#
# 【出力】
# 最短の移動回数を算出せよ。
#
# 【例題と回答】
# N = 7 のとき、一回目に1、二回目に2、三回目に4移動すれば、移動回数は3回。
# N=32766のとき、最小の移動回数は28。
# N=32767のとき、最小の移動回数は15。
# N=1000000000000000000(= 10^18)のとき、最小の移動回数は83。
#
#-------------------------------------------------------------------------------


def MOVING_TIME(N):

    # 10^3 ≈ 2^10より、10^18 = (10^3)^6 ≈ 2^60
    arithmetic_list = [0]   # 移動量
    geometric_list = [0]    # 総移動量
    for i in range(1, 61):
        arithmetic_list.append(2 ** (i - 1))
        geometric_list.append(2 ** i - 1)

    sbtr_n = N
    mov_count = 0
    roop_count = 0

    # 総移動量から最大移動量を算出
    if sbtr_n in geometric_list:
        trg_idx = geometric_list.index(sbtr_n)
    else:
        trg_idx = sorted(geometric_list + [sbtr_n]).index(sbtr_n) - 1
    mov_count += len(geometric_list[:trg_idx])
    sbtr_n -= geometric_list[trg_idx]


    # 経験した移動量から、適切な移動を算出
    while sbtr_n > 0:
        if sbtr_n in arithmetic_list:
            trg_idx = arithmetic_list.index(sbtr_n)
        else:
            trg_idx = sorted(arithmetic_list + [sbtr_n]).index(sbtr_n) - 1
        mov_count += 1
        sbtr_n -= arithmetic_list[trg_idx]

        roop_count += 1
        """
        print trg_idx
        print sbtr_n
        print roop_count
        raw_input()
        """

    return mov_count

print MOVING_TIME(10 ** 18)



