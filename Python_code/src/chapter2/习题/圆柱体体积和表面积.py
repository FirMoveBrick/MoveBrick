# 计算圆柱体的面积和体积
import math

print("计算圆柱体的面积和体积")
radius = float(input("输入圆柱体的半径"))
height = float(input("输入圆柱体的高"))
s = 2 * math.pi * radius * (radius + height)
v = math.pi * radius ** 2 * height
print('圆柱的表面积为{0:.2f}，圆柱的体积为{1:.2f}'.format(s, v))
