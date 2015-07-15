#-------------------------------------------------------------------------------
# coding: utf-8
# 以下の暗号を解け
# 11,32,41,25,46,35,92,33,71,65,52,43,12,44,15,32,14,44,
# 23,94,25,94,21,91,75,94,03,91,23,61,25,55,65,13,65,13
#
# 更に、このアルゴリズムで以下の文字を暗号化せよ。
# "りょうかいしましたあしたのおひるあいてます"
#
#-------------------------------------------------------------------------------

# あいうえおリスト
aiueo_list = [list(u"あいうえお"),
            list(u"かきくけこ"),
            list(u"さしすせそ"),
            list(u"たちつてとっ"),
            list(u"なにぬねの"),
            list(u"はひふへほ"),
            list(u"まみむめも"),
            list(u"やゆよゃゅょ"),
            list(u"らりるれろ"),
            list(u"わをん")]

# 数字の暗号
suji_inp = "11,32,41,25,46,35,92,33,71,65,52,43,12,44,15,32,14,44,23,94,25,94,21,91,75,94,03,91,23,61,25,55,65,13,65,13"
suji_inp_list = suji_inp.split(",") # 暗号をリスト化

suji_to_moji_ans_list = []      # 暗号→日本語
for i in range(len(suji_inp_list)):
    suji_int = int(suji_inp_list[i])
    moji_hoge = aiueo_list[(suji_int / 10) - 1][(suji_int % 10) - 1]
    suji_to_moji_ans_list.append(moji_hoge)

print "".join(suji_to_moji_ans_list)




moji_inp = u"りょうかいしましたあしたのおひるあいてます"
moji_inp_list = list(moji_inp)

moji_to_suji_ans_list = []      # 日本語→暗号
for i in range(len(moji_inp_list)):
    moji_str = moji_inp_list[i]
    hit = 0
    for shiin in range(len(aiueo_list)):
        if hit == 1:
            break
        for boin in range(len(aiueo_list[shiin])):
            if moji_str == aiueo_list[shiin][boin]:
                moji_to_suji_ans_list.append((shiin + 1) * 10 + (boin + 1))
                hit = 1
                break

print moji_to_suji_ans_list
