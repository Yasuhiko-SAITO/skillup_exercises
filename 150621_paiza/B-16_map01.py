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
# 与えられた移動を一回ずつ行う。
# マップの大きさから外れた際は、
# マップの大きさを足し引きすることでマップ上に戻す。

first_inp_list = map(int, raw_input().split(" "))
present_cor = map(int, raw_input().split(" "))

map_x_max = first_inp_list[0]   # マップの横幅X
map_y_max = first_inp_list[1]   # マップの縦幅Y
walk_num = first_inp_list[2]    # 移動回数N
present_x = present_cor[0]      # 現在のx座標
present_y = present_cor[1]      # 現在のy座標

for i in range(walk_num):
    walk_list = raw_input().split(" ")
    if walk_list[0] == "U":
        present_y += int(walk_list[1])
    elif walk_list[0] == "D":
        present_y -= int(walk_list[1])
    elif walk_list[0] == "R":
        present_x += int(walk_list[1])
    elif walk_list[0] == "L":
        present_x -= int(walk_list[1])

    # x座標がマップから外れている場合
    while (present_x < 0) or (present_x >= map_x_max):
        if present_x < 0:
            present_x += map_x_max
        elif present_x >= map_x_max:
            present_x -= map_x_max

    # y座標がマップから外れている場合
    while (present_y < 0) or (present_y >= map_y_max):
        if present_y < 0:
            present_y += map_y_max
        elif present_y >= map_y_max:
            present_y -= map_y_max


print str(present_x) + " " + str(present_y)







