#-------------------------------------------------------------------------------
##平方根を求める式
##入力はa bの形で、
##aは求める数、bは桁数
#-------------------------------------------------------------------------------
#入力
inp_list = raw_input().split(" ")
moto = int(inp_list[0])
keta_su = int(inp_list[1])

#整数の位の数値を算出
ans = 1
while ans ** 2 < moto:
    ans += 1
ans += -1

#小数の位の算出
ans = float(ans)
for rep in range(keta_su):
    keta = round(0.1 ** rep, rep)           #位の指定
    keta_rep = 0
    while keta_rep < 10:                    #0～9までを代入
        hoge_test = ans + keta * keta_rep
        if hoge_test ** 2 < moto:           #
            keta_rep += 1
        #2乗値が超えたら、1つ前の数値をansに代入
        else:
            ans = ans + keta * (keta_rep - 1)
            break

print ans
