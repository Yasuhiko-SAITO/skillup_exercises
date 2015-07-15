#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# The Flat Dictionary: 与えられた辞書の階層を全て一次にせよ。
#
# 【ルール】
# 多階層の辞書が与えられる。新しい辞書は以下のルールに従う。
# (1)階層は1次まで
# (2)多階層はキーをパスで表す(スラッシュ区切り)
# (3)空の辞書は、空の文字列に置き換える。
#
# 【入力】
# dict      多階層式の辞書(キーによって階層の深度は異なる)
#
# 【出力】
# 一次まで階層をフラットにした辞書を出力せよ。
#
#   例：{"name/first": "Yas",
#       "name/last": "Sai",
#       "job": ""
#       "address/Japan/Miyagi/": "Sendai"}
#
#-------------------------------------------------------------------------------

def checkio(dictionary):

    root_key_list = dictionary.keys()

    curr_dictionary = dictionary
    curr_key_list = curr_dictionary.keys()

    new_dict = {}
    for root_key in root_key_list:
        path_list = [root_key]
        if type(curr_dictionary[root_key]) == str():    #or int()
            path = "/".join(map(str, path_list))
            new_dict[path] = curr_dictionary[root_key]
        elif type(curr_dictionary[root_key]) == dict():



dictionary = \
{
"job": {
    "teacher": {
        "junior": 1,
        "senior": 3},
    "marketer": {},
    "saler": {
        "male":{
            "right": 2,
            "left": 3,},
        "female":{
            "right":{
                "pen": "Julia",
                "pencil":"Ann",},
            "left": 1,},
        },
    },
"hoge": 1,
}











