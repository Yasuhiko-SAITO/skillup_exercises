#-------------------------------------------------------------------------------
# cording: utf-8
# ?????????????????(????????????????)
# n r???        #???n, ??????r ????
# h_1 w_1 d_1???#1??????????????????
# h_2 w_2 d_2???#2??????????????????
# ...
# h_n w_n d_n???#n??????????????????
# ????????????????????
#-------------------------------------------------------------------------------

first_inp_list = raw_input().split(" ")
box_all_num = int(first_inp_list[0])    # ???n
ball_r = int(first_inp_list[1])         # ??????r

box_size_list = []                      # ??????????
for rep in range(box_all_num):
    hoge_each_box_size = raw_input().split(" ")
    hogege_e_b_s = []
    for i in range(len(hoge_each_box_size)):
        hogege_e_b_s.append(int(hoge_each_box_size[i]))
    box_size_list.append(hogege_e_b_s)

# ????????????(r * 2)????????????
ans_list = []
for i in range(box_all_num):
    disc_box_size = box_size_list[i]
    disc_OK = 0 # ?????
    for j in range(len(disc_box_size)):
        if disc_box_size[j] >= 2 * ball_r:
            disc_OK += 1
    if disc_OK == len(disc_box_size):   # disk_OK??????????????????
        ans_list.append(i + 1)  # i?0????????+1???

print "\n".join(map(str, ans_list))