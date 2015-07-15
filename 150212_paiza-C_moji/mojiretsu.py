#-------------------------------------------------------------------------------
# coding: utf-8
##日付：2015/02/12
##解決：未(テスト10でランタイムエラー)
##所要時間：？(途中で席を離れたため3時間近くになっていた)

##文字列の抽出
##最初に文字A<mojiA>と文字B<mojiB>を指定
##その後に入力される文字列で、文字Aと文字Bに挟まれた文字列を改行表示せよ
##また挟まれた文字列がない場合は"<blank>"と表示せよ

##入力値
##"<mojiA> <mojiB>"
##"hogehoge<mojiA>hogge<mojiB>hage<mojiA>hok<>e<mojiB><mojiA><mojiB>"

##出力値
##hogge
##hok<>e
##<blank>
#-------------------------------------------------------------------------------

#入力
inp_list = raw_input().split(" ")           #検索ワード
k_str = raw_input()                         #検索をかける文字列

#splitしやすくするため、"<"と">"の前後にスペースを入れる
hoge_k = k_str.replace("<", " <")
hogege_k = hoge_k.replace(">", "> ")

k_list = hogege_k.split(" ")
k_list = k_list[1:len(k_list)-1]            #最初と最後が空欄のため除外


#始まりの検索ワードのインデックスを調べる
rep = 0
mojiA_ind = []
while rep < len(k_list):
    if inp_list[0] == k_list[rep]:
        mojiA_ind.append(rep)
    rep += 1

#同様に終わりの検索ワードのインデックスを調べる
mojiB_ind = []
rep = 0
while rep < len(k_list):
    if inp_list[1] == k_list[rep]:
        mojiB_ind.append(rep)
    rep += 1


ans_list = []
for rep in range(len(mojiA_ind)):
#始まりのインデックス+1が空欄だったら、"<blank>"をくっつける
    if k_list[mojiA_ind[rep] + 1] == "":
        ans_list.append("<blank>")
#そうでない時は、文字列を結合させてリストに付加する
    else:
        ans_list.append("".join(k_list[mojiA_ind[rep]+1 : mojiB_ind[rep]]))

#出力
print "\n".join(map(str, ans_list))