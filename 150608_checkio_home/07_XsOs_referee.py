#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 三目並べの勝敗判定プログラムを作成せよ。
#
# tic-tac-toe(三目並べ)
# 2人のプレイヤー("X"と"O")が、3x3のマスの空きマスに書き込む。
# 空きマスは"."で表される。
# 水平、垂直、対角線のいずれかで3つ並べたら勝ち。
#
# 【引数】
# game_result："X", "O", "."の文字列のリスト
#   例1：["OO.","OOO","OXX"]
#   例2：[".XO",".XX","X.."]
#
# 【出力】三目並べの勝者("X"または"O")の文字列、引き分けの場合は"D"の文字列。
#
#-------------------------------------------------------------------------------
def checkio(game_result):

    ans = "D"

    for i in [-1, 0, 1]:
        # 横判定
        if (game_result[i][0] != ".")\
        and (game_result[i][0] == game_result[i][1])\
        and (game_result[i][0] == game_result[i][2]):
            ans = game_result[i][0]
        # 縦判定
        elif (game_result[0][i] != ".")\
        and (game_result[0][i] == game_result[1][i])\
        and (game_result[0][i] == game_result[2][i]):
            ans = game_result[0][i]
        # 斜め判定
        elif (i != 0) and (game_result[1][1] != ".")\
        and (game_result[i + 1][0] == game_result[1][1])\
        and (game_result[1 - i][2] == game_result[1][1]):
            ans = game_result[1][1]
        # 1 - i |   2   |   0
        # i     |   -1  |   1
        # i + 1 |   0   |   2

    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
