#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 初期座標と動き方を与えられた時、どの座標に居るか出力せよ
#
# 【ルール】
# 横幅X、縦幅Yのマップがあり、
# 左下から右に(0, 0), (1, 0), ..., (X-1, 0)
# 左下から上に(0, 0), (0, 1), ..., (0, Y-1)
# と座標が割り振られている。
# キャラクターが端まで動いたあとは、
# 上下、又は左右でループするように動くこととする。
#
# 【入力】
# X Y N     マップの横幅X、縦幅Y、動く回数N
# x y       キャラクターの初期座標(x, y)
# d_1 m_1   1回目の、動き方d_1、動く量m_1
# ...
# d_n m_n   n回目の、動き方d_n、動く量m_n
#
#   ただし、d_i = "U", "D", "L", or, "R"で、
#   それぞれ上下左右を表す。
#
# 【出力】
# 移動後のキャラクターの座標を"x_ans y_ans"の形で出力せよ。
#
#-------------------------------------------------------------------------------

# 【方針】
# 与えられた移動の総計を算出する。
# その後、初期座標に加える。
# マップからはみ出した場合は、
# その剰余値が縦横のrangeのインデックスを参照することで
# 現在の座標を算出する。

first_inp_list = map(int, raw_input().split(" "))
present_cor = map(int, raw_input().split(" "))

x_cor_list = range(first_inp_list[0]) # 横幅のrangeリスト
y_cor_list = range(first_inp_list[1]) # 縦幅のrangeリスト
walk_num = first_inp_list[2]          # 移動回数N


# 移動の総量を算出
x_add = 0
y_add = 0
for i in range(walk_num):
    walk_list = raw_input().split(" ")
    if walk_list[0] == "U":
        y_add += int(walk_list[1])
    elif walk_list[0] == "D":
        y_add -= int(walk_list[1])
    elif walk_list[0] == "R":
        x_add += int(walk_list[1])
    elif walk_list[0] == "L":
        x_add -= int(walk_list[1])

# 移動した後の座標とマップの大きさの剰余は、縦横のrangeリストのインデックスに等しくなる。
# 例えばx座標の場合、最小座標は0、最大座標はX-1であり、
# rangeは[0, 1, ..., X-1]である。現在の座標がXならば0、X+1ならば1・・・と考えると、
# [X * i + 0, X * i + 1, ..., X * i + (X-1)]ということがわかる。
# すなわち、初期座標と移動量の和を、マップの大きさで割った時の余り値は、
# 座標リストのインデックスに等しい。
# よくわからんけど、負値もこの式でOK。
after_x = x_cor_list[(present_cor[0] + x_add) % first_inp_list[0]]
after_y = y_cor_list[(present_cor[1] + y_add) % first_inp_list[1]]


print str(after_x) + " " + str(after_y)
