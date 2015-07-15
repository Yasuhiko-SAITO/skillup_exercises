#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 最も遅い出宅時刻を出力せよ
#
# 【ルール】
# 自宅から配座(パイザ)駅まで徒歩a分、
# 配座(パイザ)駅から儀野(ギノ)駅まで電車b分、
# 儀野(ギノ)駅から会社まで徒歩c分かかるとする。
# ただし、電車の待ち時間は考慮しなくてよい。
# 8：59までに出社しなければならない。
#
# 【入力】
# a b c         徒歩a分、電車b分、徒歩c分
# n             電車の本数
# t_1_h t_1_m   電車1の配座(パイザ)駅発車時分
# ...
# t_n_h t_n_m   電車nの配座(パイザ)駅発車時分
#   ただし、0 <= (a,b,c) <= 30。
#   電車は早い順に並んでいて、遅刻しない電車は1本以上存在する。
#
# 【出力】
# 出宅時刻をhh:mmの形で出力せよ。
#
#-------------------------------------------------------------------------------

# 【方針】
# datetimeを利用する。
# 電車の発車時分をリストにし、
# 出社時刻に間に合うような儀野(ギノ)駅に到着する電車をリストの後ろから検索。
# その電車に間に合うように出宅時刻を算出する。

import datetime
# 仕様により、timeだとtimedeltaが使えないため、datetimeで表す。
deadline = datetime.datetime(2015, 6, 18, 8, 59)

first_inp_list = raw_input().split(" ")
train_num = int(raw_input())    # 電車の本数n

train_list = []         # 電車リスト
for i in range(train_num):
    train_list.append(raw_input().split(" "))


# 電車は早い順に並んでいるため、
# 遅い方から検索をし、間に合う電車が見つかり次第、出宅時刻の算出に移るほうが効率的。
# 遅い方から検索をかけるには、インデックスの-1から検索をかける。
for t_index in range(1, len(train_list)+1):
    train = train_list[-t_index]
    train_departure = datetime.datetime(2015, 6, 18, int(train[0]), int(train[1]))
    train_td = datetime.timedelta(minutes = int(first_inp_list[1]))
    gino_arrival_time = train_departure + train_td
    gino_to_company_td = datetime.timedelta(minutes = int(first_inp_list[2]))
    # 電車到着時刻が間に合うか、判別。
    if deadline >= gino_arrival_time + gino_to_company_td:
        break

home_to_paiza_td = datetime.timedelta(minutes = int(first_inp_list[0]))
home_departure = train_departure - home_to_paiza_td

print home_departure.strftime("%H:%M")