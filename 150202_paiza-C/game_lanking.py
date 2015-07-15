#-------------------------------------------------------------------------------
##日付：2015/02/02
##解決：済！
##所要時間：64分

##ユーザーランキング
##総得点を求め(四捨五入)、上位K人スコアを改行表示せよ
##アイテムN個
##ユーザーM人
##上位K人
##各アイテムの1個あたりの得点Ci(i = 1~n)
##ユーザーが持ってる各アイテム数Xpi(p = 1~m, i = 1~n)

##入力値
##"N M K"
##"C1 C2 ... Cn"
##"X11 X12 ... X1n"
##"X21 X22 ... X2n"
##"Xm1 Xm2 ... Xmn"
#-------------------------------------------------------------------------------

first_inp = raw_input().split(" ")  #最初の入力→[N M K]
Ci = raw_input().split(" ")         #アイテム得点入力→[C1 C2 ... Cn]

item_num = int(first_inp[0])        #アイテム種類数→整数N
user_num = int(first_inp[1])        #ユーザー数→整数M
top = int(first_inp[2])             #表示する数→整数K

u_i_list = []                   #ユーザーのアイテム個数リスト
for rep_inp in range(user_num):
    hoge_u_i_list = raw_input()
    u_i_list.append(hoge_u_i_list)

e_point_list = []                   #総得点リスト
for u_point_rep in range(user_num):
    e_point = 0                     #得点初期化
    eu_i_list = u_i_list[u_point_rep].split(" ")
    if len(eu_i_list) != item_num:  #エラーが出たら0を入れて最初へ
        e_point_list.append(e_point)
        continue
    for cal_rep in range(item_num): #得点計算
        hoge_e_point = float(Ci[cal_rep]) * float(eu_i_list[cal_rep])
        e_point += hoge_e_point
    e_point = int(round(e_point))   #四捨五入して整数値に
    e_point_list.append(e_point)

e_point_list.sort()                 #昇順ソート
                                    #reverseを受け付けてくれなかった。

ans_list = []
for rep in range(top):              #一番後ろから順番に回答リストに付加
    ans_list.append(e_point_list[-1-rep])

print "\n".join(map(str, ans_list))

#-------------------------------------------------------------------------------
##所感
##比較演算子の!=(not equal)に注意
##変数の初期化に気付かずに苦しんだので次回から注意。
#-------------------------------------------------------------------------------