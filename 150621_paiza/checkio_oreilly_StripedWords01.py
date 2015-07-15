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
# Punctual markで分けられていてsplitで分けるのが難しい。
# そこで、textを一文字ずつisalphaとisdigitを用いて判断して、
# スペースに置き換えた後にsplitして、単語毎のリストにまとめる。
# その後、単語毎に一文字ずつ母音と子音の判断をして個数を数える。

VOWELS = "AEIOUY".lower()
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ".lower()

def checkio(text):

    # 単語ごとにリストにする。
    text_str = ""
    for i in range(len(text)):
        if text[i].isalpha() or text[i].isdigit():
            text_str += text[i].lower()
        else:
            text_str += " "
    text_list = text_str.split(" ")


    ans_count = 0
    for check_text in text_list:
        check_count = 0
        for text_index in range(1, len(check_text)):
            # 母音+子音か、子音+母音の時
            if ((check_text[text_index - 1] in VOWELS) and (check_text[text_index] in CONSONANTS)) or \
            ((check_text[text_index - 1] in CONSONANTS) and (check_text[text_index] in VOWELS)):
                check_count = 1
            else:
                check_count = -1
                break

        if check_count == 1:
            ans_count += 1

    return ans_count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("1st,2nd,3rd,fourth,fif") == 1, "fif"