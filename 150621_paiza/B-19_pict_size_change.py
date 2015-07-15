#-------------------------------------------------------------------------------
# -*- coding:utf-8 -*-
# 画像の大きさを縮小せよ。
#
# 【ルール】
# N * Nピクセルのグレースケール画像をK分の1に縮小する。手順は以下のとおり。
# (1)N * Nの行列データをブロックに分ける。1ブロックはK * Kで、総数(N/K) * (N/K)である。
# (2)ブロック内で平均値を取る(小数以下切り捨て)。
# (3)平均値を用いて(N/K) * (N/K)の行列データを作成する。
#
# 【入力】
# N K                   変換前の画像サイズNと、変換後の画像サイズK
# a_11 a_12 ... a_1N    1行目の1 <= j <= Nの各ピクセル値
# a_21 a_22 ... a_2N    2行目の1 <= j <= Nの各ピクセル値
# ...
# a_N1 a_N2 ... a_NN    N行目の1 <= j <= Nの各ピクセル値
#
#   ただし、2 <= K <= N <= 100、KはNの約数(すなわちN/Kは整数)
#   0 <= a_ij <= 255
#
# 【出力】
# 1行分は、文字列で、数字は半角スペース区切りで表記し、
# それを(N/K)行で出力せよ
# b_11 b_12 ... b_1K
# b_21 b_22 ... b_2K
# ...
# b_K1 b_K2 ... b_KK
#
#-------------------------------------------------------------------------------

# 【方針】
# N * Nのリストを作成する。
# 1ブロックの平均を取るには、該当範囲内にある長さKのリストをスライスして和を取り、
# それを該当範囲内で繰り返せば1ブロックを作成できる。
# 総数(N/K) * (N/K)個のため、二重ループで(N/K)回ずつ回せば良い。


first_inp_list = raw_input().split(" ")

big_size = int(first_inp_list[0])       # 変換前サイズN
small_size = int(first_inp_list[1])     # 変換後サイズK

# 変換前のピクセルデータリスト
# データの並び順は、データリスト[行][列]となっていることに注意
big_size_list = []
for i in range(big_size):
    big_size_list.append(map(int, raw_input().split(" ")))

repeat_num = big_size / small_size      # 繰り返し回数

new_matrix = []
for row in range(repeat_num):           # 行の繰り返し

    new_row = []
    for column in range(repeat_num):    # 列の繰り返し
        new_pix = 0
        waru = 0

        for rep in range(small_size):
            # 該当範囲内のリストを選択
            # 行は、変換後のサイズsmall_size(定数) * 変換後の行row(0 <= row <= N/K)\
            #   + 変換後サイズ範囲rep(インデックスのため、0 <= rep <= small_size - 1)
            # 列は、変換後のサイズsmall_size(定数) * 変換後の列column(0 <= column <= N/K)から
            # 変換後のサイズsmall_size(定数) * 変換後の行column + 1(インデックスのため)を
            # それぞれインデックスで指定する。
            hoge_list = big_size_list[small_size * row + rep][small_size * column : small_size * (column + 1)]
            new_pix += sum(hoge_list)
            waru += len(hoge_list)
        #

        new_pix /= waru
        new_row.append(new_pix)
    #

    new_matrix.append(new_row)
#


ans = ""
for hoge_list in new_matrix:
    # 初回以外は改行を加える
    if ans != "":
        ans += "\n"
    ans += " ".join(map(str, hoge_list))


print ans
