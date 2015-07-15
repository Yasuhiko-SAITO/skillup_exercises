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
recipe_all_num = int(raw_input())
recipe_list = []
recipe_material_list = []
recipe_dict = {}
for i in range(recipe_all_num):
    hoge_shokuzai = raw_input().split(" ")
    recipe_list.append([hoge_shokuzai[0], int(hoge_shokuzai[1])])
    recipe_material_list.append(hoge_shokuzai[0])
    recipe_dict[hoge_shokuzai[0]] = int(hoge_shokuzai[1])


material_all_num = int(raw_input())
material_list = []
material_dict = {}
for i in range(material_all_num):
    hoge_material = raw_input().split(" ")
    material_list.append([hoge_material[0], int(hoge_material[1])])
    material_dict[hoge_material[0]] = int(hoge_material[1])

# 食材を持っていなかった時
hoge_ans = []
for i in range(len(recipe_material_list)):
    if (recipe_material_list[i] in material_dict) == False:
        hoge_ans.append(0)

if len(hoge_ans) == 0:
    for i in range(len(recipe_material_list)):
        ans = material_dict[recipe_material_list[i]] / recipe_dict[recipe_material_list[i]]
        hoge_ans.append(ans)

hoge_ans.sort()

print hoge_ans[0]

