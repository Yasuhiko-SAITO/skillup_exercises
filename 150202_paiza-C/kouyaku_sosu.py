#-------------------------------------------------------------------------------
##2数の最大公約数を表示させるように作ろうと思ったけど、
##途中から2数の約数かつ素数だけのリストを表示するようになっちゃった。
#-------------------------------------------------------------------------------

first_list = raw_input().split(" ")
if int(first_list[0]) < int(first_list[1]):
    first_num = int(first_list[0])
    second_num = int(first_list[1])
else:
    first_num = int(first_list[1])
    second_num = int(first_list[0])

ans_list = []
check_rep = 1
while check_rep < first_num:
    check_f = first_num % check_rep
    check_s = second_num % check_rep
    if check_f == 0 and check_s == 0:
        ans_list.append(check_rep)
    check_rep += 1

print ans_list

sosu_c_1st = 2
sosu_check = sosu_c_1st
while sosu_check < len(ans_list):
    sosu_y_c = sosu_c_1st - 1
    while sosu_y_c < sosu_check:
        if ans_list[sosu_check] % ans_list[sosu_y_c] == 0:
            ans_list.pop(sosu_check)
            sosu_check += -1
            break
        sosu_y_c += 1
    sosu_check += 1

##ans = 0
##for ans_rep in range(len(ans_list)):
##    ans += int(ans_list[ans_rep])

##print ans
print ans_list