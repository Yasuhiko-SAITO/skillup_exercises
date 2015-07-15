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

hoge_inp_list = raw_input().split(" ")          #入力されたリスト
##print "%s^%s" % (inp_list[0] , inp_list[1])
inp_list = []
#入力されたリストはunicodeなので、数値に変換
for hoge in range(len(hoge_inp_list)):
    inp_list.append(int(hoge_inp_list[hoge]))
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

#素因数分解
#入力リストの1番目からn番目まで、素因数分解を繰り返す
#素数リストの1番目から順に何度も繰り返す。
soinsu_list = []                        #素因数分解したリスト.
for rep in range(num_inp):
    e_soinsu_list = []                  #入力された各値の指数リスト
    hoge_sosu = int(inp_list[rep])

#素数リストの個数分だけ繰り返し
    for num_sosu in range(len(sosu)):
        warukazu = int(sosu[num_sosu])
        num_watta = 0

#割る数で割り切れなくなるまで割り続ける
        while hoge_sosu % warukazu == 0:
            hoge_sosu = hoge_sosu / warukazu
            num_watta += 1

#リストにくっつける
        e_soinsu_list.append(num_watta)
        warukazu = int(sosu[num_sosu])

    soinsu_list.append(e_soinsu_list)


#最大公約数用の指数リストを作成
#素因数リストの1～n番の1番から順に、昇順で並べ、最も大きい数をリストに追加する。
koyakusu_sisu_list = []

#素因数リストの1～n番まで繰り返す
for rep in range(len(e_soinsu_list)):
    hoge_sisu_list = []

#抽出した各リストの1~n番までを抽出してリストを作成
    for rep_a in range(len(soinsu_list)):
        hoge_sisu_list.append(soinsu_list[rep_a][rep])

#昇順で並べ、最も大きい数を追加
    hoge_sisu_list.sort()
    koyakusu_sisu_list.append(hoge_sisu_list[-1])

#最大公約数の計算
koyakusu = 1
for rep in range(len(koyakusu_sisu_list)):
#(求めたい最大公約数) = (前の公約数) × (素数)^(指数)
    koyakusu = koyakusu * (int(sosu[rep]) ** int(koyakusu_sisu_list[rep]))

print inp_list
print sosu
print soinsu_list
print koyakusu_sisu_list
print koyakusu