#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# ネットサーフィンのパスを出力せよ
#
# 【ルール】
# 複数のクエリ(処理要求)が入力される。
# 最初は必ず"blank page"を開く。
# リンクを開くときは"go to hogehoge"、
# 前のページに戻るときは"use the back button"が入力される。
#
# 【入力】
# n         クエリ数
# q_1       1番目のクエリ
# q_2       2番目のクエリ
# ...
# q_n       n番目のクエリ
#
#   ただし、q_1 = "go to blank page",
#   q_i = "go to [page name]" or "use the back button"
#   [page name]は英小文字と半角スペースから成る文字列、
#   "go to hogehoge"はページ名hogehogeを開くクエリ、
#   "use the back button"は直前に開いていたページを開くクエリ
#
# 【出力】
# 閲覧したページ名のパスを、文字列で、改行して出力せよ。
#
#-------------------------------------------------------------------------------

# 【方針】
# 回答リストansListと、現在のパスリストcurrentPassListの2つを用意。
# 回答リストは、開いたページを加えていく。
# 現在のパスリストは、新規ページはそのまま加え、
# 戻った時は、一番最後に加えたページを削除すれば、
# 削除後のリストの-1番目が現在開いているページとなる。

query_num = int(raw_input())

ansList = []
currentPassList = []
for rep_num in range(query_num):
    query_str = raw_input()

    # 新規ページを開いた時
    if query_str[0] == "g":
        # query_str = "go to hogehoge"のため、
        # ページ名のインデックスは6番から最後まで
        ansList.append(query_str[6 : len(query_str)])
        currentPassList.append(query_str[6 : len(query_str)])

    # 戻るボタンをおした時
    elif query_str[0] == "u":
        # currentPassList = [blank page, ..., hogehoge, 「戻るクエリ」前に閲覧したページ]
        # 故に、最後のインデックスを削除し、
        # 「戻るクエリ」によって表示されたページ名を加える
        currentPassList = currentPassList[0:-1]
        ansList.append(currentPassList[-1])

print "\n".join(map(str, ansList))
