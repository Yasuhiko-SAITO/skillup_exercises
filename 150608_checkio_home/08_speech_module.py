#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 入力された数値を英語の文字列で出力せよ
#
# 【引数】
# number：数値(ただし、0 < number < 1000)
#   例1：143
#   例2：101
#
# 【出力】英語表記の文字列
#   例1：checkio(143)=='one hundred forty three'
#   例2：checkio(212)=='two hundred twelve'
#-------------------------------------------------------------------------------

def checkio(number):
    number_dic = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        }

    number_hozon = number   # 保存用
    ans_word = ""
    # 100以上の時
    if number >= 100:
        ans_word += number_dic[number / 100] + " " + "hundred"
        if number % 100 != 0:
            ans_word += " "
        number %= 100

    # 20以上の時
    if (number > 20) and (number % 10 == 0):
        ans_word += number_dic[number]
        number %= 10
    elif (number > 20):
        ans_word += number_dic[(number / 10) * 10] + " "
        number %= 10

    if number != 0:
        ans_word += number_dic[number]

    return ans_word

