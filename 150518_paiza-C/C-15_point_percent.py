#-------------------------------------------------------------------------------
# coding: utf-8
# レシートに書かれた金額と日付を基に、ポイントを計算せよ
# 入力は以下のフォーマットで与えられます。
# N　　　　#各レシートの数
# d_1 p_1　#1枚目のレシートの日付 d_1 日, 購入金額 p_1 円
# d_2 p_2　#2枚目のレシートの日付 d_2 日, 購入金額 p_2 円
# ...
# d_N p_N　#N枚目のレシートの日付 d_N 日, 購入金額 p_N 円
# d_nに3が付く(3, 13, 23, 30, 31)の時は3％
# d_nに5が付く(5, 15, 25)の時は5％
# それ以外は1%で、小数点以下は切り捨てで合算せよ。
# 出力は1行で。
#-------------------------------------------------------------------------------

receipt_all_num = int(raw_input())  # 入力N

receipt_list_str = []
for i in range(receipt_all_num):
    hoge_each_list = raw_input().split(" ") # 入力d_n p_n
    receipt_list_str.append(hoge_each_list) # 日付と価格のリスト(文字列)

# 判別式を用いて、パーセントと価格のリスト(数字)にする
percent_price_list = []
for rep in range(receipt_all_num):
    date_discri = int(receipt_list_str[rep][0])
    # 日付を10で割った時の商か余りのどちらかが、3か5と一致した時
    if date_discri / 10 == 3 or date_discri % 10 == 3:
        each_percent = 3
    elif date_discri / 10 == 5 or date_discri % 10 == 5:
        each_percent = 5
    else:
        each_percent = 1
    # パーセントと価格の組み合わせにして、それをリストに挿入
    hoge_each_list = [each_percent, int(receipt_list_str[rep][1])]
    percent_price_list.append(hoge_each_list)

# パーセントと価格のリストを用いて、ポイントの合算
ans = 0
for j in range(receipt_all_num):
    ans += percent_price_list[j][0] * percent_price_list[j][1] / 100

print ans