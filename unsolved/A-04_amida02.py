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
line_len = first_inp[0]
line_num = first_inp[1]
cross_num = first_inp[2]


cross_height_list = [[]]
for i in range(line_num):
    cross_height_list.append([])

raw_amida = []
for i in range(cross_num):
    hoge_inp = map(int, raw_input().split(" "))
    left_line = hoge_inp[0]
    right_line = left_line + 1
    left_line_height= hoge_inp[1]
    right_line_height = hoge_inp[2]

    # このやり方だと、本数が一の時に、インデックスが変わってくる。やりなおし。

    raw_amida.append(hoge_inp)
    cross_height_list[left_line].append([left_line_height, [right_line, right_line_height]])
    cross_height_list[left_line].sort()
    cross_height_list[right_line].append([right_line_height, [left_line, left_line_height]])
    cross_height_list[right_line].sort()

curr_line = 1
curr_height = line_len
discri = 0
m_idx = -1



while curr_height > 0:

    if curr_height < cross_height_list[curr_line][m_idx][0]:
        m_idx -= 1

    else:
        curr_height = cross_height_list[curr_line][m_idx][1]
        curr_line = cross_height_list[curr_line][m_idx][0]
        print curr_height
        print curr_line
        print cross_height_list
        raw_input()
        m_idx = -1


    if -m_idx == len(cross_height_list[curr_line]):
        break

print curr_line


