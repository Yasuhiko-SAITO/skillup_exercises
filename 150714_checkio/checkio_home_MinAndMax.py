#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Min and Max: 新たなMax Min関数を作る。
#
# 【ルール】
# 新しい関数minとmaxを作る。
# 以下の組み込み関数を用いることを禁ずる→import, eval, exec, globals
# 引数が一つ以上とし、最大または最小値を返す。
# オプションとして、キーワード引数keyがある。
# 該当する値が複数ある場合は、最初に見つかったものを返す。
#
# 【入力】
# arg       iterableな単一の引数、或いは2つ以上の引数
#
# 【出力】
# 関数maxは引数の最大値を、関数minは引数の最小値を出力する。
#
#-------------------------------------------------------------------------------


def max(*args, **kargs):

    # いかなる引数でも、argsのタイプはタプルとなる。
    # 引数が、リスト、セット、タプル、文字列の場合、argsタプルの長さは1となる。
    # 引数が、整数、小数の場合、argsタプルの長さは、引数の個数と同じ。
    # ソート用args4sortを用意すると以下のようになる。
    if len(args) == 1:
        args4sort = args[0]
    else:
        args4sort = list(args)

    # 引数がジェネレーターだった場合
    # 全ての数値をリストにしてしまう。
    if "generator" in str(type(args[0])):
        args4sort = []
        while 1:
            try:
                args4sort.append(args[0].next())
            except StopIteration:
                break
        # whileここまで
    # ifここまで

    idx_num = -1    # 参照するインデックス
    # キーは必ず辞書型。
    # キーがなかった場合。
    if kargs == {}:
        ans = sorted(args4sort)[idx_num]

    # 並び替えキーがintの場合。
    # 該当する値が複数あると、整列後の最終インデックスが正答にならない場合がある。
    # そこで、最大値の整数値を見つけた後、その値がどこで出てくるかをチェックする。
    # 一応、並び替えキーの名前が"key"ではない条件も考慮して、
    # 条件式は「キーリストkargs.keys()の0番目をキーとした値kargs[kargs.keys()[0]]が
    # intの場合」とする。
    elif kargs[kargs.keys()[0]] == int:
        checkint = int(sorted(args4sort, key = kargs[kargs.keys()[0]])[idx_num])
        for i in args4sort:
            if checkint == int(i):
                ans = i
                break

    # キーがint以外の場合。
    else:
        ans = sorted(args4sort, key = kargs[kargs.keys()[0]])[idx_num]

    return ans
# def max(*args, **kargs)ここまで


def min(*args, **kargs):

    # いかなる引数でも、argsのタイプはタプルとなる。
    # 引数が、リスト、セット、タプル、文字列の場合、argsタプルの長さは1となる。
    # 引数が、整数、小数の場合、argsタプルの長さは、引数の個数と同じ。
    # ソート用args4sortを用意すると以下のようになる。
    if len(args) == 1:
        args4sort = args[0]
    else:
        args4sort = list(args)

    # 引数がジェネレーターだった場合
    # 全ての数値をリストにしてしまう。
    if "generator" in str(type(args[0])):
        args4sort = []
        while 1:
            try:
                args4sort.append(args[0].next())
            except StopIteration:
                break
        # whileここまで
    # ifここまで

    idx_num = 0    # 参照するインデックス
    # キーは必ず辞書型。
    # キーがなかった場合。
    if kargs == {}:
        ans = sorted(args4sort)[idx_num]
    # キーがある場合。
    # maxと違い、intの場合でも参照インデックスは0のまま。
    else:
        ans = sorted(args4sort, key = kargs[kargs.keys()[0]])[idx_num]

    return ans
# def min(*args, **kargs)ここまで

"""
一番すごい回答
def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]
​
​
def min(*args, key=None):
    return get_first_from_sorted(args, key, False)
​
​
def max(*args, key=None):
    return get_first_from_sorted(args, key, True)

"""


