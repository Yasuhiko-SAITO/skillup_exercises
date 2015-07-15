#-------------------------------------------------------------------------------
##2数の最小公倍数を求める。
##入力値は"a b"でスペース区切り
#-------------------------------------------------------------------------------

inp_list = raw_input().split(" ")
f_num = int(inp_list[0])
s_num = int(inp_list[1])

if f_num < s_num:
    limit_rep = f_num
else:
    limit_rep = s_num

by_2num = f_num * s_num
check_num = by_2num
warukazu = 2
ans = check_num

while warukazu < limit_rep:
    if check_num % warukazu != 0:
        warukazu +=1
        continue
    check_num = check_num / warukazu
    print check_num
    f_ch_amari = check_num % f_num
    s_ch_amari = check_num % s_num

    if f_ch_amari == 0 and s_ch_amari == 0:
        ans = check_num
        continue
    else:
        check_num = ans
        warukazu += 1
        continue

print inp_list
print ans