#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
given_dict = \
    {
    "job": {"scout": {}},
    }



ans_dict = {}
root_key_list = given_dict.keys()       # ルート辞書のキーリスト

for root_key in root_key_list:
    pass_list = []
    key_count = 0                       # a
    current_dic_name = given_dict
    current_key = root_key
    current_key_list = root_key_list
    next_dic_name = current_dic_name[root_key]


    while key_count < len(current_key_list):
        print type(next_dic_name)
        raw_input()
        if next_dic_name == {}:
            next_dic_name = ""

        while type(next_dic_name) == dict:
            pass_list.append(current_key)
            current_dic_name = next_dic_name
            current_key_list = current_dic_name.keys()
            current_key = current_key_list[key_count]
            next_dic_name = current_dic_name[current_key]

        if current_dic_name[current_key] == {}:
            current_dic_name[current_key] = ""

        ans_dict["/".join(pass_list + [current_key_list[key_count]])] = current_dic_name[current_key]

        key_count += 1


        if key_count < len(current_key_list):
            current_key = current_key_list[key_count]
            next_dic_name = current_dic_name[current_key]


print ans_dict