#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     14/04/2015
# Copyright:   (c) admin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#落ち物ゲーのプログラム
#指定された座標が消えた時、
#その上のものが落ちて整列するような結果を返す。
#初期入力は、x y
#以下
#t_0_0 t_1_0 ... t_x_0
#t_0_1 t_1_1 ... t_x_1
#...
#t_0_y t_1_y ... t_x_y
#と入力される。
#t_x_y = 0, 1, 2で、0が空欄、1が残る、2が消える

coordinate_inp = raw_input().split(" ")
rc_inp = []

for i in range(int(coordinate_inp[1])):
    rc_inp.append(raw_input().split(" "))

count_one = []

#各列1の個数を数える
for column in range(int(coordinate_inp[0])):
    count_hoge = 0
    for raw in range(int(coordinate_inp[1])):
        if int(rc_inp[raw][column]) == 1:
            count_hoge += 1
    count_one.append(count_hoge)

#count_oneを基に、
#行列を入れ替えた結果を出す
ans_list_inv = []
for i in range(int(coordinate_inp[0])):
    hoge = []
    for j in range(int(coordinate_inp[1])):
        #0の時だけめんどくさくなるのでandを使って条件付け
        if count_one[i] != 0 and count_one[i] - j > 0:
            hoge.append(1)
        else:
            hoge.append(0)
    hoge.sort()
    ans_list_inv.append(hoge)

#行列を入れ替える。
ans_list = []
for i in range(int(coordinate_inp[1])):     #y行回繰り返し
    hoge = []
    for j in range(int(coordinate_inp[0])): #x列回繰り返し
        hoge.append(ans_list_inv[j][i])
    ans_hoge_str = " ".join(map(str, hoge)) #列を空白でくっつける
    ans_list.append(ans_hoge_str)

print "\n".join(map(str, ans_list))





