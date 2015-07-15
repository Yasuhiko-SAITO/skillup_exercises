#-------------------------------------------------------------------------------
# coding: utf-8
# ターゲットのIPと一致するログファイルを探索し、該当ログを指定に従って表示せよ。

# ＜入力＞
# A     ターゲットのIPアドレス
# N     ログファイル数
# log_1 ログファイル1つ目
# ...
# log_n ログファイルnつ目

# ただし、(1)IPアドレスは、"~.~.~.~"と記載され、
# 各数字は「オクテット(octet)」と呼ばれる。
# 第1,第2オクテットは定数(ただし、ログと必ず同じとは限らない)
# 第3,第4オクテットは、範囲指定は[0-100]、全範囲は*で記載される場合がある。
# 数字が取りうる範囲は0~255である。
# (2)logは「IPアドレス identユーザー名 認証ユーザー名 [アクセス日時]
# "リクエストヘッダ ファイル名 プロトコル" ステータスコード 転送されたバイト数
# 呼び出し元URL ブラウザ情報等」の9情報を含んでいる。
# この9情報は半角スペース区切りである。

# ターゲットIPアドレス例
# 192.168.[1-2].[10-20]
# 192.168.*.*

# ログファイル例
# 192.168.110.238 - - [10/Jul/2013:18:40:43 +0900] "GET /top.html HTTP/1.1" 404 8922 "http://gi-no.jp" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36"

# 該当ログのうち、IPアドレス、日付(タイムゾーン除く)、ファイル名を
# スペース区切りで表示せよ。
#-------------------------------------------------------------------------------

# 解法
# ターゲットIPに範囲指定がなければ、一致不一致の判定でOK
# 範囲指定あり・全範囲の場合は、その範囲の最初と最後の数字のリストを作って、
# その中にタゲが含まれるかを大小判定。

# ログの抜き出しは、IPはスペース区切りの後に0番目を、
# 日付は" ["区切りの後に1番目を、
# ファイル名は"GET "区切りの後に1番目を、それぞれ抜き出す。だせえw
#-------------------------------------------------------------------------------

target_ip_list = raw_input().split(".")

for i in [0, 1]:
    target_ip_list[i] = int(target_ip_list[i])

for i in [2, 3]:
    if target_ip_list[i] == "*":        # *が入力された時
        target_ip_list[i] = [0, 255]
    elif len(target_ip_list[i]) >= 5:   # 範囲指定された時
        hoge_tor = target_ip_list[i].split("-")
        # [を抜かして数字を抽出
        range_first = int(hoge_tor[0][1:])
        # ]を抜かして数字を抽出
        range_last = int(hoge_tor[1][:len(hoge_tor[1])-1])
        target_ip_list[i] = [range_first, range_last]
    else:                               # 数字が入力された時
        target_ip_list[i] = int(target_ip_list[i])

ans_list = []
inp_num = int(raw_input())  # ログファイル数N
for i in range(inp_num):
    hit = 0                 # ターゲットと一致した回数
    check = raw_input()
    # スペース区切りの0番目"~.~.~.~"をsplit
    check_ip_list = check.split(" ")[0].split(".")

    for j in range(4):  #IPアドレスのオクテット数は4つ
        # タゲのオクテットが整数で表記され、一致しない時
        if (type(target_ip_list[j]) == int) and \
           (int(check_ip_list[j]) != target_ip_list[j]):
            break
        # タゲのオクテットが整数で表記され、一致する時
        if (type(target_ip_list[j]) == int) and \
           (int(check_ip_list[j]) == target_ip_list[j]):
            hit += 1
        # タゲのオクテットがリストで表記され、
        # リストの最小より大きく、最大より小さい時
        if (type(target_ip_list[j]) == list) and \
        (target_ip_list[j][0] <= int(check_ip_list[j])) and \
        (target_ip_list[j][1] >= int(check_ip_list[j])):
            hit += 1

    # 4つのオクテット全てが条件に一致した時
    if hit == 4:
        # IPアドレスは、" "区切りの0番目
        ans_ip = check.split(" ")[0]
        # 日付は、" ["区切りの後に1番目"~ +~"を、更に" "区切りした0番目
        ans_access = check.split("[")[1].split(" ")[0]
        # ファイル名は"GET "区切りの後に1番目"~ HTTP~"を、更に" "区切りした0番目
        ans_filename = check.split("GET ")[1].split(" ")[0]
        # 以上3つをリストにして、半角スペースでくっつける
        hoge_ans = " ".join(map(str, [ans_ip, ans_access, ans_filename]))
        ans_list.append(hoge_ans)

print "\n".join(map(str, ans_list))
