#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 7つのセグメントの点・消灯を組み合わせて、0～9の数字を表示した時、
# 正立・鏡立・回転条件で数字となるか否か、回答を出力せよ。
#
# 【ルール】
# 7つのセグメントの点・消灯の組み合わせを2セット作ることで、2桁の数字を表示する。
# 7つのセグメントをそれぞれa1 ~ a7, b1 ~ b7と名付けると、以下の配置になる。
#    a1             b1
# a6    a2      b6      b2
#    a7             b7
# a5    a3      b5      b3
#    a4             b4
# この時、正立で表示した時、鏡立で表示した時、回転して表示した時、
# 数字として見えるかどうかを出力せよ
#
# 【入力】
# a_1 a_2 ... a_7   a1からa7の点・消灯状態
# b_1 b_2 ... b_7   b1からb7の点・消灯状態
#   ただし、点灯状態は1、消灯状態は0で表す。
#
# 【出力】
# 1行目に正立条件、2行目に鏡立条件、3行目に回転条件の回答を、
# 数字となるならば"Yes"、ならないならば"No"で出力せよ。
#
#-------------------------------------------------------------------------------

# 【方針】
# 数字を表すことが出来る組み合わせをキーに、辞書を作成。
# 与えられた組み合わせを、正立条件、鏡立条件、回転条件にそれぞれ表示しなおし、
# 各条件での表示形式が辞書に存在するかどうかをチェックすることで、YesNoを出力する。

num_dic = {"1111110": "0",
            "0110000": "1",
            "1101101": "2",
            "1111001": "3",
            "0110011": "4",
            "1011011": "5",
            "1011111": "6",
            "1110010": "7",
            "1111111": "8",
            "1111011": "9",}

a_list = raw_input().split(" ")
b_list = raw_input().split(" ")

ans = ""

# 正立条件
# 入力のままのため、与えられた組み合わせリストをそのままjoinして文字列にする。
a_normal = "".join(map(str, a_list))
b_normal = "".join(map(str, b_list))

if (a_normal in num_dic) and (b_normal in num_dic):
    ans += "Yes" + "\n"
else:
    ans += "No" + "\n"


# 鏡条件
# この条件では、以下の並びになる
#    b1             a1
# b2    b6      a2      a6
#    b7             a7
# b3    b5      a3      a5
#    b4             a4
# 故に、リストの並び替えにはa1→a6→a5→a4→a3→a2→a7の順番にする。
a_mirror_list = []
b_mirror_list = []
for i in [1, 6, 5, 4, 3, 2, 7]:
    a_mirror_list.append(a_list[i - 1])     # インデックスのためi - 1
    b_mirror_list.append(b_list[i - 1])     # 同上
a_mirror = "".join(map(str, a_mirror_list))
b_mirror = "".join(map(str, b_mirror_list))

if (a_mirror in num_dic) and (b_mirror in num_dic):
    ans += "Yes" + "\n"
else:
    ans += "No" + "\n"


# 回転条件
# この条件では、以下の並びになる
#    b4             a4
# b3    b5      a3      a5
#    b7             a7
# b2    b6      a2      a6
#    b1             a1
# 故に、リストの並び替えにはa4→a5→a6→a1→a2→a3→a7の順番にする。
a_rotation_list = []
b_rotation_list = []
for i in [4, 5, 6, 1, 2, 3, 7]:
    a_rotation_list.append(a_list[i - 1])   # インデックスのためi - 1
    b_rotation_list.append(b_list[i - 1])   # 同上
a_rotation = "".join(map(str, a_rotation_list))
b_rotation = "".join(map(str, b_rotation_list))

if (a_rotation in num_dic) and (b_rotation in num_dic):
    ans += "Yes"
else:
    ans += "No"


# 回答
print ans