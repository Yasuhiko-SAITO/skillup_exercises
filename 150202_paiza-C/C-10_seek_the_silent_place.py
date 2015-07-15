#-------------------------------------------------------------------------------
# coding: utf-8
# 1 行目には 3 つの整数 a、b、R が入力されます。
# a、b はそれぞれ工事現場の位置の x 座標、y 座標を、
# R は工事現場の騒音の大きさを表します。
# 2 行目には木陰の数を表す整数 N が入力されます。
# 続く N 行には各木陰の座標を表す 2 つの整数 x_i、y_i が入力されます。
# a b R　　　#工事現場のx座標,工事現場のy座標,工事現場の騒音の大きさ
# N　　　　　#木陰の数
# x_1 y_1　　#木陰1のx座標,木陰1のy座標
# x_2 y_2　　#木陰2のx座標,木陰2のy座標
# ...
# x_N y_N　　#木陰Nのx座標,木陰Nのy座標

# この時R ^ 2 =< (x - a) ^ 2 + (x - b) ^ 2
# 出力はN行で、R未満なら"noisy"、R以上なら"silent"を出力せよ。
#-------------------------------------------------------------------------------

first_inp_list = raw_input().split(" ")
# 工事現場の座標設定
construction_coordinate = [int(first_inp_list[0]),int(first_inp_list[1])]
# 騒音の大きさを設定
loudness = int(first_inp_list[2])
# 木陰の数を入力
all_tree = int(raw_input())
# 木陰のリストを入力
tree_coordinate_list = []
for i in range(all_tree):
    hoge_each_tree_coor = raw_input().split(" ")
    hoge_each_tree_coor_list = [int(hoge_each_tree_coor[0]), int(hoge_each_tree_coor[1])]
    tree_coordinate_list.append(hoge_each_tree_coor_list)

# 判別式
ans_list = []
for i in range(all_tree):
    e_tree_x = tree_coordinate_list[i][0]   # x座標
    e_tree_y = tree_coordinate_list[i][1]   # y座標
    hanbetsu = (e_tree_x - construction_coordinate[0]) ** 2 + (e_tree_y - construction_coordinate[1]) ** 2

    if hanbetsu >= loudness ** 2:
        ans_list.append("silent")
    else:
        ans_list.append("noisy")

print "\n".join(map(str, ans_list))

