#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      admin
#
# Created:     05/02/2015
# Copyright:   (c) admin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

inp_list = raw_input().split(" ")
##print "%s^%s" % (inp_list[0] , inp_list[1])
num_inp = len(inp_list)

inp_list.sort()
#素数のリストをつくるための素材リストをつくる
sosu_sozai = range(int(inp_list[-1]) + 1)     #入力された最大値を含む配列を作成


m = 3               #素材リストの抽出番号(抽出される数字はm-1)
sosu = [2]          #素数リスト

#素材リストの長さは、リスト内の最大値+1
while m < len(sosu_sozai):
    n = 0
    sosu_flag = 0

    while n < len(sosu):
#素材リストのm番目を抽出、素数リストのn番目で割る
#割り切れるならフラグに1足す
        if int(sosu_sozai[m]) % int(sosu[n]) == 0:
            sosu_flag += 1
        n += 1

#フラグが0のままだったら素数
    if sosu_flag == 0:
        sosu.append(m)

    m += 1

print sosu