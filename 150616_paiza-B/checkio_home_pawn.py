#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 安全なポーンがいくつあるか、出力せよ
#
# 【ルール】
# チェスでは、左からa ~ h列、下から1～8行の座標となる。
# 持ちコマの一つであるポーンは、斜め前に一つだけ動くことが出来る。
# 駒が利いている時、利かれている駒はsafeとし、
# 他の駒によって利いていない駒はunsafeとする。
# 例えばP_1のポーンの位置(a4)がP_2のポーンの斜め前(b3)に居る時、
# P_1はsafeとなる。P_2は他のコマがa2かc2にない限り、unsafeとなる。
#
# 【入力】
# ["x_1y_1", "x_1y_1", …, "x_1y_1" ]
# ただしP_1の座標(x_1, y_1)、…P_nの座標(x_n, y_n)、
# 0 < P <= 8
#
# 【出力】
# 利かれている駒数を数字で出力せよ
#
#-------------------------------------------------------------------------------

def safe_pawns(pawns):

    # 【方針】
    # 列を1～8、行を10～80の数字に置き換える。
    # 与えられた座標を数字に変換したセットを用意する。
    # それらの座標に対応する、利き座標セットを用意する
    # 与えられた座標セットと、利き座標セットの和集合を取り、その長さを返す

    # 数値に変換するためのリスト
    cor_list = ["nothing", "a", "b", "c", "d", "e", "f", "g", "h"]
    cor_value_set = set()
    safe_cor_value_set = set()
    for check_pawn in pawns:
        level_ones = cor_list.index(check_pawn[0])  # 一の位
        level_tens = int(check_pawn[1])             # 十の位
        cor_value = level_tens * 10 + level_ones    # 数値に変換した座標
        cor_value_set.add(cor_value)
        # 利き座標は斜め前だから、+9と+11
        safe_cor_value_set.add(cor_value + 11)
        safe_cor_value_set.add(cor_value + 9)

    ans = cor_value_set & safe_cor_value_set        # 和集合

    return len(ans)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

