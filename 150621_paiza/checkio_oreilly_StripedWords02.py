#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# striped words：母音と子音が交互に出てくるワードの個数を調べよ
#
# 【ルール】
# アルファベットと数字と、スペースを含む句読点で成り立つ、ある文字列が与えられる。
# 母音VOWELSと子音CONSONANTSが交互に現れる単語の個数を出力せよ。
# ただし、VOWELS = "AEIOUY"、CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"とする。
#
# 【入力】
# checkio(test)     textは、英単語と、スペースを含む句読点
#
# 【出力】
# 母音と子音が交互に出てくる単語の個数を、数値で出力せよ
# 該当単語例：in, dog, are, have, vowel
# 非該当単語例：a, you, try, vowels
#
#-------------------------------------------------------------------------------

# 【方針】
# 与えられたtextを一文字ずつ判定。
# (1)母音の時、(2)子音の時、(3)数字の時、(4)句読点の時で場合分け。
# 単語毎のリストにまとめる。
# カウントしない条件と、それ以外の条件で場合分けして、個数を数える。

import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):

    # 単語ごとにリストにする。
    text = text.upper()
    text_str = ""
    for i in range(len(text)):
        if text[i] in VOWELS:           # 母音だった時
            text_str += "v"
        elif text[i] in CONSONANTS:     # 子音だった時
            text_str += "c"
        elif text[i].isdigit():         # 数値だった時
            text_str += text[i]
        else:                           # その他(句読点だった時)
            text_str += " "
    text_list = text_str.split(" ")


    ans_count = 0
    for word_v_c in text_list:
        # カウントしない条件。母音vか子音cか数字で表された単語の中に、
        # (1)母音か子音が連続で出てくる場合、
        # (2)単語の長さが1以下の場合、
        # (3)単語の冒頭・終わり以外に数字が含まれる場合。
        if  word_v_c.find("cc") != -1 or word_v_c.find("vv") != -1 or\
        len(word_v_c) <= 1 or \
        (re.search("\d", word_v_c) and\
         ( re.search("\d", word_v_c).start() != 0 or \
           re.search("\d", word_v_c).start() != len(word_v_c) - 1) ):
            ans_count += 0
        # それ以外の場合はカウントする。
        else:
            ans_count += 1

    return ans_count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("1st,2nd,3rd,fourth,fif") == 1, "fif"
    assert checkio("1 2 3 12 13") == 0, "digit"