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
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    number_hozon = number

    ans_word = ""
    # 100以上の時
    if number >= 100:
        ans_word += FIRST_TEN[int(number / 100) - 1] + " " + HUNDRED
        if number % 100 != 0:
            ans_word += " "
        number %= 100

    # 20以上の時
    if (number >= 20):
        ans_word += OTHER_TENS[(number / 10) - 2]
        if number % 10 != 0:
            ans_word += " "
        number %= 10

    # 10以上20未満の時
    if (number >= 10) and (number < 20):
        ans_word += SECOND_TEN[(number % 10)]
        number = 0

    if number != 0:
        ans_word += FIRST_TEN[number - 1]

    return ans_word

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"