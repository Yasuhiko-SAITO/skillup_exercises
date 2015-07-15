#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# カンファレンスのタイムテーブルを作成せよ
#
# 【ルール】
# 10：00に開始する。トーク間は10分間の休憩を入れる。
# X氏のトーク終了予定時刻が12：01以降になる場合は、
# X氏のトーク前の10分休憩を、1時間のお昼休憩に変更する。
# お昼休憩は1回だけである。
#
# 【入力】
# N         発表者数
# n_1 m_1   1番目の名前と発表時間(分)
# ...
# n_N m_N   N番目の名前と発表時間(分)
#
# 【出力】
# 改行して以下の文字列で出力せよ
# st_1 - et_1 n_1   1番目の、開始時間、終了時間、名前
# ...
# st_N - et_N n_N   N番目の、開始時間、終了時間、名前
# ただし、時間は"hh:mm"の形で、分時は必ず2桁で表すこと。
# 開始時間と終了時間の間は" - "を、終了時間と名前の間は" "を挿入すること。
#
#-------------------------------------------------------------------------------

import datetime

ppt_num = int(raw_input())      # 発表者数N
ppt_list = []
for i in range(ppt_num):
    ppt_list.append(raw_input().split(" "))

start_hour = 10 # 会議の開始時間(時)
start_min = 0   # 会議の開始時間(分)
rest_min = 10   # 休憩時間

d = datetime.datetime(2015, 6, 12, start_hour, start_min)

ans_list = []
lunch_count = 0
for rep in range(ppt_num):
    add_min = int(ppt_list[rep][1])     # 発表時間

    # お昼休憩を入れるか
    hoge_d = d + datetime.timedelta(minutes = add_min)
    if (hoge_d.hour >= 12) and (hoge_d.minute != 0) and (lunch_count == 0):
        d += datetime.timedelta(minutes = 50)
        lunch_count += 1

    start_time = d      # 発表開始時間
    end_time = d + datetime.timedelta(minutes = add_min)    # 発表終了時間
    d = end_time + datetime.timedelta(minutes = rest_min)   # 休憩後
    # "開始時間 - 終了時間 名前"をリストに挿入
    ans_list.append(start_time.strftime("%H:%M") + " - " + end_time.strftime("%H:%M") + " " + ppt_list[rep][0])

print "\n".join(map(str, ans_list))