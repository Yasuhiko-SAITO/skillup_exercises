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

# 【方針】
#   移動量が増えればゴールに早く近づくのは当然であるため、
# 出来るだけ大きな移動量を取る必要がある。
# ただし、移動量が増加していくまでの総移動量を考慮しなくてはならない。
# 移動するたびに必ず移動量を増やしたとして、
# i回移動した時の、i回目の移動量は2^(i - 1)で、総移動量は2^i - 1である。
# この総移動量が入力された数値より上回る直前のiの値を見つけ、
# その総移動量を入力数値から引く。
#   残りの値は、どの移動量を用いるかを考えればよい。
# 当然移動量が大きいほうが良いため、
# 残りの数値を上回らない最も大きな移動量を見つけ、
# その差分を取り、whileで回し続ければよい。


def MOVING_TIMES(N):

    # 10^3 > 2^10より、10^18 = (10^3)^6 < 2^60
    # 移動量リストmomentum_listのインデックスを、
    # 必ず移動量2倍した時の移動回数と一致させるため、0を加えておく。
    momentum_list = [0]
    for i in range(0, 61):
        momentum_list.append(2 ** i)

    sbtr_n = N
    mov_count = 0
    roop_count = 0

    while sbtr_n > 0:

        # 最大移動量を見つける処理を、初回ループで行う。
        if roop_count == 0:

            # i回移動した時の総移動量は2^i - 1であるため、
            # 入力された数値sbtr_nに1を加えた数値を探す。
            # 移動量リスト内にその値があれば、そのインデックスを取得する。
            if sbtr_n + 1 in momentum_list:
                trg_idx = momentum_list.index(sbtr_n + 1)
            # ない場合は、移動量リスト内で、
            # 入力数値を上回らない最も大きな値のインデックスを取得する。
            # その方法は、入力数値をリストに加えた新リストをソートしなおして、
            # 入力数値のインデックスを取得し、-1すれば良い。
            else:
                trg_idx = sorted(momentum_list + [sbtr_n]).index(sbtr_n) - 1

            # trg_idxは総移動量のインデックスiであり、
            # 移動回数はi - 1である。
            mov_count += trg_idx - 1
            # 総移動量は2^i - 1である。
            sbtr_n -= momentum_list[trg_idx] - 1
        # ifここまで

        # 2回目以降のループはこちらの処理。
        elif roop_count != 0:

            # 1回目と、ほぼ同様の処理。
            # 総移動量ではなく、移動量1回分を見ていることに注意。
            if sbtr_n in momentum_list:
                trg_idx = momentum_list.index(sbtr_n)
            else:
                trg_idx = sorted(momentum_list + [sbtr_n]).index(sbtr_n) - 1
            mov_count += 1
            sbtr_n -= momentum_list[trg_idx]
        # elifここまで

        roop_count += 1
    # whileここまで

    return mov_count

print u"N = 7の時、最小移動回数は", MOVING_TIMES(7), u"。"
print u"N = 32766の時、最小移動回数は", MOVING_TIMES(32766), u"。"
print u"N = 32767の時、最小移動回数は", MOVING_TIMES(32767), u"。"
print u"N = 10^18の時、最小移動回数は", MOVING_TIMES(10 ** 18), u"。"
