#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# ドローン同士で繋がりがあるかないか、出力せよ
#
# 【ルール】
# ネットワーク記録には、関係がある2つのドローンが記載され、
# それら２つの名前はハイフンで繋がれている。
# 記録はタプルで記載され、関係を示す集合は複数ある場合がある。
#
# 【入力】
# 2ドローンの関係の情報(タプル), ドローンAの名前、ドローンBの名前
#
# 【出力】
# ドローンAとドローンBが、いくつかの関係を経てつながりがあるかどうか、
# つながりがあればTrueを、なければFalseを出力せよ。
#-------------------------------------------------------------------------------

def check_connection(network, first, second):

    # 【方針】
    # 繋がりはセットで表現する。
    # 繋がりが複数の場合はリストにしてまとめる。
    # a
    # a
    # a
    # a

    # for文で回す前に、セットを用意しておく
    new_set = set([network[0].split("-")[0], network[0].split("-")[1]])
    set_list = [new_set]

    # セットを用意したから、networkの1から回す
    for each_nw in network[1:]:
        hoge_set = set([each_nw.split("-")[0], each_nw.split("-")[1]])
        # 繋がりセットのリストの長さ(つまりセットの個数)だけ繰り返す
        # 書き換えがあるため、
        for list_rep in range(len(set_list)):
            check_set = set_list[list_rep]
            if check_set & hoge_set:    # セットと共通する名前があったら
                check_set |= hoge_set   # 積集合をとる。
                set_list[list_rep] = check_set  #書き換えも忘れずに
            elif not(check_set & hoge_set) and (list_rep == len(set_list) - 1 ):
                set_list.append(hoge_set)
        i = 0
        while (len(set_list) > 1) and (i < len(set_list) - 1):
            if set_list[i] & set_list[i + 1]:
                set_list[i] |= set_list[i + 1]
                del set_list[i + 1]
            else:
                i += 1


    ans = False
    for check_set in set_list:
        if (first in check_set) and (second in check_set):
            ans = True

    return ans


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."



