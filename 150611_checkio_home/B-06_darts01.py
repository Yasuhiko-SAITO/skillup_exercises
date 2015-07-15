#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# ダーツの矢が的に当たるか、当たるなら中心までどのくらいの距離か、算出せよ
#
# 的までの距離x[m]、高さo_y[m]から矢を放つ。
# 矢の初速はs[m/s]、X面に対して角度θ[度]とする。
# 的の直径はa[m]、的の中心の高さはy[m]とする。
# 重力加速度gを9.8[m/s^2]とすると、
# 的までの距離x[m]の地点での、X面(0)からの矢の高さyは以下のようになる
#                        g x^2
# y = o_y + x tanθ - ――――――――――――――
#                   　2 s^2 cos^2θ
#
# 【入力】
# o_y s θ   # 矢の初期高さ　矢の初速　矢の角度
# x y a     # 的までの距離　的の高さ　的の大きさ
#
# 【出力】
# 当たれば"Hit"、外れれば"Miss"。
# 更に当たる場合は、矢から中心までの距離を算出し、小数第2位で四捨五入せよ。
#   例１：Hit 3.3
#
# paizaで80点。特殊データで間違うのはしょうがないとして、
# 基本データでも一つミスが発生。一体何だ？
#-------------------------------------------------------------------------------

first_inp_list = raw_input().split(" ")
second_inp_list = raw_input().split(" ")


throwing_height = int(first_inp_list[0])    # 矢の初期高さo_y
initial_velocity = int(first_inp_list[1])   # 矢の初速s
throwing_angle_d = int(first_inp_list[2])   # 矢の角度θ
distance = int(second_inp_list[0])          # 的までの距離x
target_height = int(second_inp_list[1])     # 的の高さy
target_size = int(second_inp_list[2])       # 的の大きさa
g_acceleration = 9.8                        # 重力加速度g

# 当たる範囲
hit_range = [target_height - (target_size / 2), target_height + (target_size / 2)]

ans = "Miss"

import math     # tan cosの計算のためmathをインポート
# 矢の高さを算出
arrow_point = throwing_height + \
                (distance * math.tan(math.radians(throwing_angle_d))) - \
                ((g_acceleration * (distance ** 2)) / \
                    ((2 * (initial_velocity ** 2)) * (math.cos(math.radians(throwing_angle_d)) ** 2)))

# 当たる範囲に矢がある場合
if (hit_range[0] <= arrow_point) and (hit_range[1] >= arrow_point):
    ans = "Hit" + " " + str(round(math.fabs(arrow_point - target_height), 1))

print ans
