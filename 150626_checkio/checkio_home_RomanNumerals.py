#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Roman numerals: 入力された数字を、ローマ数字に変換して出力せよ
#
# 【ルール】
# アラビア数字とローマ数字の対応表は以下の通りである。
#
#   1   2   3   4	5	6	7	8       9
#   I	II	III	IV	V	VI	VII	VIII   IX
#
#   10	20	30	40	50	60	70	80     90
#   X	XX	XXX	XL	L	LX	LXX	LXXX   XC
#
#   100	200	300	400	500	600	700	800     900
#   C	CC	CCC	CD	D	DC	DCC	DCCC	CM
#
#   1000	2000	3000
#   M   	MM     MMM
#
# 【入力】
# N         数値。0 < N < 4000
#
# 【出力】
# ローマ数字を用いて、文字列で出力せよ。
#
#-------------------------------------------------------------------------------

# 【方針】
# インデックスと表記が対応したリストを作成する。
# あとは10, 100, 1000で割った商と余りの値を用いて、
# 対応するリストから引っ張ってくれば良い。

def checkio(data):

    # 割った値をインデックスとしたいため、インデックス0は""とする。
    onesList = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tensList = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hndsList = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tsnsList = ["", "M", "MM", "MMM"]

    ans = ""
    while data / 10 > 0:
        if data / 1000 > 0:
            ans += tsnsList[int(data / 1000)]
            data %= 1000
        elif data / 100 > 0:
            ans += hndsList[int(data / 100)]
            data %= 100
        elif data / 10 > 0:
            ans += tensList[int(data / 10)]
            data %= 10

    ans += onesList[int(data)]

    return ans


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'

