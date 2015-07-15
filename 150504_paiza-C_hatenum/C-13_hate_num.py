#-------------------------------------------------------------------------------
# coding: utf-8
# 入力は以下のフォーマットで与えられます。
# n #嫌いな数字
# m #病室の総数
# r_1 #1個目の部屋番号
# r_2 #2個目の部屋番号
# ...
# r_m #m個目の部屋番号
# 嫌いな数字を含まない病室を改行で出力せよ。
# なければ"none"を出力せよ。

# 2015/5/4　ランタイムエラーが出てる
#-------------------------------------------------------------------------------
hate_num = int(raw_input())
all_room = int(raw_input())


test_all_room_list = []
hoge_all_room_list = []

for i in range(all_room):
    hoge_room = int(raw_input())
    hoge_all_room_list.append(hoge_room)


for i in range(all_room):
    if hoge_all_room_list[i] >= 100:
        rep = [2, 1, 0]
    elif hoge_all_room_list[i] >= 10 and hoge_all_room_list[i] < 100:
        rep = [1, 0]
    elif hoge_all_room_list[i] < 10:
        rep = [0]

    each_room_list = []
    for j in rep:
        hoge = hoge_all_room_list[i] / (10 ** j)
        if hoge >= 100:
            hoge = hoge - each_room_list[0] * 100 - each_room_list[1] * 10
        elif hoge >= 10 and hoge < 100:
            hoge = hoge - each_room_list[0] * 10

        each_room_list.append(hoge)
    test_all_room_list.append(each_room_list)


ans_list = []
for all_room_rep in range(all_room):
    descri_num = 0
    for each_room_rep in range(len(test_all_room_list[all_room_rep])):
        each_room_list = test_all_room_list[all_room_rep]
        if each_room_list[each_room_rep] == hate_num:
            descri_num += 1
    if descri_num == 0:
        ans_list.append(hoge_all_room_list[all_room_rep])


if len(ans_list) == 0:
    ans_list.append("none")

print "\n".join(map(str, ans_list))


