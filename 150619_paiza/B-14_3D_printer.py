#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 3Dプリンターで立体物を作成した時、ある方向から見た時の見え方を出力せよ
#
# 【ルール】
# yow軸をz軸、roll軸をx軸、pitch軸をy軸とする。
# yz面を正面とし、原点から視点に近づくほどx += 1とする。
# この視点から立体物を見た時の、見え方を出力せよ。
# 視力や視野角は考慮しなくてよい。
#
# 【入力】
# X Y Z                         XYZのそれぞれの最大座標
# C(1,1,1)C(1,2,1)...C(1,Y,1)   x = 1, z = 1, 1 <= y <= Yの各セルの状態
# C(2,1,1)C(2,2,1)...C(2,Y,1)   x = 2, z = 1, 1 <= y <= Yの各セルの状態
# ...
# C(X,1,1)C(X,2,1)...C(X,Y,1)   x = X, z = 1, 1 <= y <= Yの各セルの状態
# --                            z = 1の区切り
# C(1,1,2)C(1,2,2)...C(1,Y,2)   x = 1, z = 2, 1 <= y <= Yの各セルの状態
# C(2,1,2)C(2,2,2)...C(2,Y,2)   x = 2, z = 2, 1 <= y <= Yの各セルの状態
# ...
# C(X,1,2)C(X,2,2)...C(X,Y,2)   x = X, z = 2, 1 <= y <= Yの各セルの状態
# --                            z = 2の区切り
# ...
# --                            z = 3の区切り
# ...
# ......
# --                            z = (Z - 1)の区切り
# C(1,1,Z)C(1,2,Z)...C(1,Y,Z)   x = 1, z = Z, 1 <= y <= Yの各セルの状態
# C(2,1,Z)C(2,2,Z)...C(2,Y,Z)   x = 2, z = Z, 1 <= y <= Yの各セルの状態
# ...
# C(X,1,Z)C(X,2,Z)...C(X,Y,Z)   x = X, z = Z, 1 <= y <= Yの各セルの状態
# --                            z = Zの区切り
#   ただし、C(x,y,z) = "#" or "."(座標(x,y,z)が埋まっていれば"#", 空白なら".")、
#   1 <= (X,Y,Z) <= 50。
#
# 【出力】
# 正面から見た見え方を、"#"もしくは"."を用いて、改行で出力せよ。
# この時、一番上の座標の見えを1行目に、一番下の座標の見えをZ行目に記載せよ。
#
#-------------------------------------------------------------------------------

# 【方針】
# 入力される3次元座標を、三次元座標リストthree_dim_listにまとめる。
# 視点はyz面を正面にするように見た時の、最も手前に見える"#"ということは、
# 例えばz = 1として、1 <= y <= Yの各y座標において、1 <= x <= Xの範囲で"#"の検索をかけた時、
# 1つでも"#"があればその視点から見え、1つもない場合はその視点からは見えないということ。
# それを1 <= z <= Zまで積み重ねていけば、その視点からの見えのリストyz_planeが出来る。
#
first_inp_list = raw_input().split(" ")

# three_dim_listのインデックスに注意
# 入力の順番を考慮すると、three_dim_list[z][x][y]となる。
three_dim_list = []
for three_dim_rep in range(int(first_inp_list[2])):
    two_dim_list = []       # 1 <= z <= Zのxy面のリスト
    for two_dim_rep in range(int(first_inp_list[0])):
        two_dim_list.append(list(raw_input()))
    three_dim_list.append(two_dim_list)
    kugiri = raw_input()



yz_plane = []
for z_axis in range(int(first_inp_list[2])):
    apparent_line = ""

    for y_axis in range(int(first_inp_list[1])):

        # x_axisは、原点からではなく、視点に近い方から探したほうが良いため、
        # rangeは[1, 2, ..., X]が返るようにし、インデックスは負とする。
        for x_axis in range(1, int(first_inp_list[0]) + 1):
            if three_dim_list[z_axis][-x_axis][y_axis] == "#":
                apparent_line += "#"
                break
            # 最後まで検索かけて"."だったら
            elif (three_dim_list[z_axis][-x_axis][y_axis] == ".") and \
            (x_axis == int(first_inp_list[0])):
                apparent_line += "."
        #
    #
    yz_plane.append(apparent_line)

# 見えのリストyz_planeは、下から上への順番となっているため、
# インデックスを負にしてansに加えていく
ans = ""
for rep in range(1, len(yz_plane) + 1):
    if ans != "":       # 初め以外で改行を加える。
        ans += "\n"
    ans += yz_plane[-rep]

print ans
