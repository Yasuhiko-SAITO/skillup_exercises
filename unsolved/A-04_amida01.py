#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# N
# N
# N
# N
# N
# N
# N
# N
# N
# N
# N
# N
#-------------------------------------------------------------------------------
first_inp = map(int, raw_input().split(" "))

raw_amida = []
for i in range(first_inp[2]):
    hoge_inp = map(int, raw_input().split(" "))
    raw_amida.append(hoge_inp)

ref_list = range(1, first_inp[1]) + [1]
ref_list.sort()

curr_line = 1
left_line = ref_list[curr_line - 1]
curr_height = first_inp[0]
discri = 0
while discri != 1:

    for m_idx in range(1, first_inp[2] + 1):
        if (curr_line == raw_amida[-m_idx][0]) and\
           (curr_height > raw_amida[-m_idx][1]):
            if curr_line != first_inp[1] - 1:
                curr_line = ref_list[curr_line + 1]
                left_line = ref_list[curr_line - 1]
            else:
                left_line = ref_list[curr_line]
            curr_height = raw_amida[-m_idx][1]
            break
        elif (curr_line != raw_amida[-m_idx][0]) and\
             (left_line == raw_amida[-m_idx][0]) and\
             (curr_height > raw_amida[-m_idx][2]):
            if curr_line != 1:
                curr_line = ref_list[curr_line - 1]
                left_line = ref_list[curr_line - 1]
            else:
                left_line = 1
            curr_height = raw_amida[-m_idx][2]
            break

        if m_idx == first_inp[2]:
            discri = 1

print curr_line