#-------------------------------------------------------------------------------
# coding: utf-8
# 台風の暴風域に居るかどうかを答えよ。
# ただし台風には「台風の目」があり、そこは暴風域ではない。
#
# xc yc r_1 r_2     台風の座標(xc, yc)と、
#                   台風の目の半径r_1、台風の半径r_2
# n                 座標数n
# x_1 y_1           1つ目の座標(x_1, y_1)
# x_2 y_2           2つ目の座標(x_2, y_2)
# ...
# x_n y_n           nつ目の座標(x_n, y_n)
# 暴風域にいれば"yes"、いなければ"no"を改行で答えよ。
# ただし、座標(x, y)が暴風域に居るときは以下の式を満たす。
# (r_1)^2 <= (x - xc)^2 + (y - yc)^2 <= (r_2)^2
#-------------------------------------------------------------------------------

inp_list = raw_input().split(" ")
# 台風の座標(xc, yc)
typhoon_center = [int(inp_list[0]), int(inp_list[1])]
safe_range = int(inp_list[2])   # 台風の目の半径r_1
danger_range = int(inp_list[3]) # 台風の半径r_2

cor_all_num = int(raw_input())  # 座標数n
cor_list = []                   # 座標リスト
for i in range(cor_all_num):
    hoge_cor = raw_input().split(" ")
    cor_list.append([int(hoge_cor[0]), int(hoge_cor[1])])

ans_list = []
for rep in range(cor_all_num):
    e_cor = cor_list[rep]
    discriminate = (e_cor[0] - typhoon_center[0]) ** 2 + (e_cor[1] - typhoon_center[1]) ** 2
    # 暴風域にいる時。
    # 調べたい座標が、台風の目の外 かつ 台風の内 に居る時。
    if (safe_range ** 2 <= discriminate) and (discriminate <= danger_range ** 2):
        ans_list.append("yes")
    # 暴風域には居ない時
    else:
        ans_list.append("no")

print "\n".join(map(str, ans_list))