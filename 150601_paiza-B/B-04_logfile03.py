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
# 範囲指定は[0-100]、全範囲は*で記載される。
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
# 範囲指定あり・全範囲の場合は、その範囲のリストを作って逐一判定させる

# ログの抜き出しは、IPはスペース区切りの後に0番目を、
# 日付は" ["区切りの後に1番めを、
# ファイル名は"GET "区切りの後に1番目を、それぞれ抜き出す。だせえw
#-------------------------------------------------------------------------------

target_ip_list = raw_input().split(".")

for i in [0, 1]:
    target_ip_list[i] = int(target_ip_list[i])

for i in [2, 3]:
    if target_ip_list[i] == "*":        # *が入力された時
        target_ip_list[i] = range(256)
    elif len(target_ip_list[i]) >= 5:   # 範囲指定された時
        hoge_tor = target_ip_list[i].split("-")
        range_first = int(hoge_tor[0][1:])  # [を抜かして数字を抽出
        range_last = int(hoge_tor[1][:len(hoge_tor[1])-1])  # ]を抜かして数字を抽出
        target_ip_list[i] = range(range_last+1)[range_first :]
    else:   # 数字が入力された時
        target_ip_list[i] = int(target_ip_list[i])

ans_list = []
inp_num = int(raw_input())
for i in range(inp_num):
    hit = 0
    check = raw_input()
    check_ip_list = check.split(" ")[0].split(".")

    for j in range(4):
        if (type(target_ip_list[j]) == int) and \
           (int(check_ip_list[j]) != target_ip_list[j]):
            break
        if (type(target_ip_list[j]) == int) and \
           (int(check_ip_list[j]) == target_ip_list[j]):
            hit += 1
        if (type(target_ip_list[j]) == list):
            for k in range(len(target_ip_list[j])):
                if int(check_ip_list[j]) == target_ip_list[j][k]:
                    hit += 1
                    break

    if hit == 4:
        ans_ip = check.split(" ")[0]
        ans_access = check.split("[")[1].split(" ")[0]
        ans_filename = check.split("GET ")[1].split(" ")[0]
        hoge_ans = " ".join(map(str, [ans_ip, ans_access, ans_filename]))
        ans_list.append(hoge_ans)

print "\n".join(map(str, ans_list))
