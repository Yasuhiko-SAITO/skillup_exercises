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


target_ip_list = raw_input().split(".")

if target_ip_list[2] == "*":        # *が入力された時
    target_ip_list[2] = range(256)
elif len(target_ip_list[2]) >= 5:   # 範囲指定された時
    hoge_tor = target_ip_list[2].split("-")
    third_octed_range_first = int(hoge_tor[0][1:])  # [を抜かして数字を抽出
    third_octed_range_last = int(hoge_tor[1][:len(hoge_tor[1])-1])  # ]を抜かして数字を抽出
    hoge_3_range = range(third_octed_range_last + 1)
    target_ip_list[2] = hoge_3_range[third_octed_range_first + 1 :]
else:
    target_ip_list[2] = int(target_ip_list[2])

if target_ip_list[3] == "*":
    target_ip_list[3] = range(256)
elif len(target_ip_list[3]) >= 5:
    hoge_tor = target_ip_list[3].split("-")
    third_octed_range_first = int(hoge_tor[0][1:])
    third_octed_range_last = int(hoge_tor[1][:len(hoge_tor[1])-1])
    hoge_3_range = range(third_octed_range_last + 1)
    target_ip_list[3] = hoge_3_range[third_octed_range_first + 1 :]
else:
    target_ip_list[3] = int(target_ip_list[3])


inp_num = int(raw_input())
check_list = []
for i in range(inp_num):
    check_list.append(raw_input())



ans_list = []
for i in range(inp_num):
    hit = 0
    check = check_list[i]
    check_ip_list = check.split(" ")[0].split(".")

    if (type(target_ip_list[2]) == int) and (int(check_ip_list[2]) != target_ip_list[2]):
        continue
    if (type(target_ip_list[2]) == int) and (int(check_ip_list[2]) == target_ip_list[2]):
        hit += 1
    if type(target_ip_list[2]) == list:
        for j in range(len(target_ip_list[2])):
            if int(check_ip_list[2]) == target_ip_list[2][j]:
                hit += 1
                break

    if (type(target_ip_list[3]) == int) and (int(check_ip_list[3]) != target_ip_list[3]):
        continue
    if (type(target_ip_list[3]) == int) and (int(check_ip_list[3]) == target_ip_list[3]):
        hit += 1
    if type(target_ip_list[3]) == list:
        for j in range(len(target_ip_list[3])):
            if int(check_ip_list[3]) == target_ip_list[3][j]:
                hit += 1
                break

    if hit == 2:
        ans_ip = check.split(" ")[0]
        ans_access = check.split("[")[1].split(" ")[0]
        ans_filename = check.split("GET ")[1].split(" ")[0]
        hoge_ans = " ".join(map(str, [ans_ip, ans_access, ans_filename]))
        ans_list.append(hoge_ans)


print "\n".join(map(str, ans_list))
