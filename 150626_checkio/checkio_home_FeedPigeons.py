#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Feed Pigeons: 少なくとも一つ餌を食べれるハトの数は？
#
# 【ルール】
# ハトに餌をやる。1分毎にハトがやってきて、その数は変動する。
# 1分目は1匹、2分目には2匹、・・・、N分目にはN匹、新しいハトがやってくる。
# 一度来たハトは、飛び去ることはない。
# 新しいハトがやってきた時は、前からいたハトから餌を食べる。
#
# 【入力】
# N         餌の数が数値で入力される。0 < N < 10^5
#
# 【出力】
# 少なくとも一つ餌を食べれるハトの数を、数値で出力せよ。
#
#-------------------------------------------------------------------------------

# 【方針】
# 全てのハトに餌が与えられるのがN分目の時まで、whileで回し続ける。
# あとはN + 1分目の時に、どれだけ餌が与えられるかを考慮すれば良い。

def checkio(number):

    # 餌付け1分目の値
    pegeonAllNum = 1    # 全ハト数
    pegeonInc = 1       # ハトの増加量
    feed = 1            # N回目に全ハトに必要な餌量
    pegeonCount = 0     # N回目までの、餌付け完了したハト数

    # N分目の全てのハトに餌が行き渡る場合、
    # すなわち、残っている餌の手持ちnumber - N回目で必要な餌量feed > 0の場合。
    while number - feed > 0:
        pegeonCount += pegeonInc    # ハトの増加量分だけカウント
        number -= pegeonAllNum      # 餌の総量から全ハト数を引く

        # 後判定のための処理
        pegeonInc += 1              # N + 1分目のハトの増加量
        pegeonAllNum += pegeonInc   # N + 1分目の全ハト数
        feed = pegeonAllNum         # N + 1分目に必要な餌量


    pegeonAllNum -= pegeonInc       # N分目までの全ハト数
    # N + 1分目で、新たに来たハトに対して餌を与えられる場合、
    # すなわち餌の手持ちnumber - N分目までの全ハト数 > 0の場合。
    if number - pegeonAllNum > 0:
        pegeonCount += number - pegeonAllNum

    return pegeonCount

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"