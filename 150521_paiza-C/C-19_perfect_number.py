#-------------------------------------------------------------------------------
# coding: utf-8
# N を 2 以上の整数とし、N の約数のうち N 自身を除いたものの和を S と設定。
# ・N = S となるような N を完全数
# ・|N-S| = 1 となるような N をほぼ完全数
# とする。
# Q       判定したい整数の個数 Q
# N_1     判定したい整数N_1
# ...
# N_Q     判定したい整数N_Q
# ・N_i が完全数であれば "perfect"
# ・N_i がほぼ完全数であれば "nearly"
# ・どちらでもなければ "neither"
# 以上を改行で出力せよ
#-------------------------------------------------------------------------------

perfect_all_num = int(raw_input())
perf_list = []
for i in range(perfect_all_num):
    perf_list.append(int(raw_input()))


ans_list = []
for i in range(perfect_all_num):
    yakusu = 0
    # <おさらい> range(n)は0からn-1までを出力する。
    # 割る数をj+1にするため、range(n-1)に設定する。
    for j in range(perf_list[i] - 1):
        if perf_list[i] % (j + 1) == 0:
            yakusu += (j + 1)

    # 判別式
    if yakusu == perf_list[i]:
        ans_list.append("perfect")
    elif yakusu - perf_list[i] == 1 or yakusu - perf_list[i] == -1:
        ans_list.append("nearly")
    else:
        ans_list.append("neither")


print "\n".join(map(str, ans_list))