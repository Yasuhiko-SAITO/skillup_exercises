#-------------------------------------------------------------------------------
# coding: utf-8
# レシピと食材を与えられた時、何人分作れるか答えよ
# n　　　　　#レシピに書かれている食材の数を表す整数 n
# a_1 b_1　　#レシピに書かれている食材の名前 a_1, 数 b_1
# a_2 b_2　　#レシピに書かれている食材の名前 a_2, 数 b_2
# ...
# a_n b_n　　#レシピに書かれている食材の名前 a_n, 数 b_n
# m　　　　　#あなたが所持している食材の数を表す整数 m
# c_1 d_1　　#所持している食材の名前 c_1, 数 d_1
# c_2 d_2　　#所持している食材の名前 c_2, 数 d_2
# ...
# c_m d_m　　#所持している食材の名前 c_m, 数 d_m
# 注：レシピに書かれた食材を持っていない場合もある(その時は0を返す)
# 何人分作れるか、数字1行で回答せよ

# 回答時間45分で67点だった。一発合格だけど、ちょい時間かかりすぎた。
# 辞書を使うかリストを使うかで悩んでしまったことと、
# 0人分のテストで時間がかかってしまったのが敗因か。
#-------------------------------------------------------------------------------

recipe_all_num = int(raw_input())   # レシピの食材数n
recipe_material_list = []           # レシピに出てくる食材リスト
recipe_dict = {}                    # レシピに出てくる食材と数の辞書
for i in range(recipe_all_num):
    hoge_material_r = raw_input().split(" ")    # 食材_recipe
    recipe_material_list.append(hoge_material_r[0])
    recipe_dict[hoge_material_r[0]] = int(hoge_material_r[1])


material_all_num = int(raw_input()) # 所持している食材m
material_dict = {}                  # 所持している食材と数の辞書
for i in range(material_all_num):
    hoge_material_s = raw_input().split(" ")    # 食材_self
    material_dict[hoge_material_s[0]] = int(hoge_material_s[1])

# 食材を持っていなかった時
ans_list = []
for i in range(len(recipe_material_list)):
    # レシピ内の食材リストの一つが、所持している食材の辞書になかった時
    if (recipe_material_list[i] in material_dict) == False:
        ans_list.append(0)      # 0人分

# 食材を持っている時
if ans_list == []:
    for i in range(len(recipe_material_list)):
        # 作れる人数は、持っている食材数をレシピの食材数で割れば算出できる
        # 各食材に対して上記の計算を行う
        ans = material_dict[recipe_material_list[i]] / recipe_dict[recipe_material_list[i]]
        ans_list.append(ans)

# 最も小さい数が、作れる最大人数である。
ans_list.sort()

print ans_list[0]