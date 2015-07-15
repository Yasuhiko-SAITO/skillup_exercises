#-------------------------------------------------------------------------------
# coding: utf-8
# 親カードと子カードのどちらが強いか
# a b       親カードの1枚目aと2枚目b
# n         子カードの組数
# A_1 B_1   子カード1組目
# …
# A_n B_n   子カードn組目
# 親の勝ち：1枚目aが大きい時 or 1枚目が同じで、2枚目が小さい時
# 親が勝てば"High", 親が負ければ"Low"として、
# 改行で表示せよ。
#-------------------------------------------------------------------------------

# 親カード
parent_inp_list_s = raw_input().split(" ")
parent_inp =[int(parent_inp_list_s[0]), int(parent_inp_list_s[1])]


child_all_num = int(raw_input())    # 子カード組数

# 子カードリスト
child_inp_list = []
for i in range(child_all_num):
    hoge_child_inp_list_s = raw_input().split(" ")
    child_inp_list.append([int(hoge_child_inp_list_s[0]), int(hoge_child_inp_list_s[1])])

# 判別式
ans_list = []
for i in range(child_all_num):
    child_inp = child_inp_list[i]
    if parent_inp[0] > child_inp[0]:
        ans = "High"
    elif parent_inp[0] < child_inp[0]:
        ans = "Low"
    elif parent_inp[0] == child_inp[0]:
        if parent_inp[1] < child_inp[1]:
            ans = "High"
        elif parent_inp[1] > child_inp[1]:
            ans = "Low"
    ans_list.append(ans)

print "\n".join(map(str, ans_list))