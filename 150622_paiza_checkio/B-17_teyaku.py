#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 与えられた手役が何かを判定せよ
#
# 【ルール】
# アルファベット26種+ワイルドカード"*"の全27種から成る4枚の手札が入力される。
# アルファベットは各種最大4枚(高々4枚)である。
# ワイルドカードは、どのアルファベットにも置き換え可能で、最大1枚(高々1枚)である。
# 手役は以下のとおりである。
#
# ある種類が4枚→      FourCard    例：AAAA　AAA*
# ある種類が3枚→      ThreeCard   例：AAAB  AAB*
# ある種類が2枚で2組→ TwoPair     例：AABB
# ある種類が2枚で1組→ OnePair     例：AABC　ABC*
# 役なし→             NoPair      例：ABCD
#
# 【入力】
# s         文字列、len(s) == 4
#   ただし、sはアルファベット26種+ワイルドカード"*"の、全27種から成る
#
# 【出力】
# ルールに従った手役を出力せよ。
#
#-------------------------------------------------------------------------------

# 【方針】
# 入力された文字列を、リストとセットに置き換える。
# なぜなら、セットにすると重複分が少なくなるため。
# 次にリスト内の文字をカウントする。
# 文字カウントとセットの長さに応じて、手役を判断する。

input_list = sorted(list(raw_input()))
input_set = set(input_list)

letter_count = 0
for letter in input_set:
    # 今までの文字カウントが小さかった時は、新しい文字カウントに置き換える。
    if letter_count < input_list.count(letter):
        letter_count = input_list.count(letter)

# ワイルドカードが混じっている場合は、文字カウントに1を加える。
# 後の手役判定で簡単になるように、セットから"*"を抜いておく。
if "*" in input_list:
    letter_count += 1
    input_set.remove("*")

# 手役判定
if letter_count == 4:
    ans = "FourCard"
elif letter_count == 3:
    ans = "ThreeCard"
elif letter_count == 2 and len(input_set) == 2:
    ans = "TwoPair"
# 仮にワイルドカードが入っていてもセットから抜いたため、
# OnePairのセットの長さは必ず3となる。
elif letter_count == 2 and len(input_set) == 3:
    ans = "OnePair"
else:
    ans = "NoPair"


print ans