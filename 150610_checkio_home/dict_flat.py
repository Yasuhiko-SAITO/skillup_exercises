#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     10/06/2015
# Copyright:   (c) admin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
given_dict = \
    {
    "name": {
        "first": "One",
        "last": "Drone"
        },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"
            }
        }
    }

e = 0
ans_dict = {}
for layer_1 in given_dict.keys():
    path = layer_1
    hoge_path = path
    if type(given_dict[layer_1]) == dict:
        for layer_2 in given_dict[layer_1].keys():
            if type(given_dict[layer_1][layer_2]) == dict:
                path += "/" + layer_2
                hoge_path = path
                for layer_3 in given_dict[layer_1][layer_2].keys():
                    if type(given_dict[layer_1][layer_2][layer_3]) == dict:
                        e = 1
                    else:
                        path += "/" + layer_3
                        ans_dict[path] = given_dict[layer_1][layer_2][layer_3]
                        path = hoge_path
            else:
                path += "/" + layer_2
                ans_dict[path] = given_dict[layer_1][layer_2]
                path = hoge_path
    else:
        if given_dict[layer_1] == {}:
            given_dict[layer_1] = ""
        ans_dict[path] = given_dict[layer_1]
        path = hoge_path


print ans_dict
print e