# 计算一元二次方程的根
import math

print("请输入二元一次方程的三个系数")
a = float(input("请输入a："))
b = float(input("请输入b："))
c = float(input("请输入c："))
if a == 0:
    print("方程系数不能为零，非二元一次方程")
    exit(0)
tmp = (b * b) - (4 * a * c)
# print(tmp)
# exit()
if tmp >= 0:
    x1 = (-b + math.sqrt(tmp)) / (2 * a)
    x2 = (-b - math.sqrt(tmp)) / (2 * a)
    print("x1 = {:.3f},x2 = {:.3f}".format(x1, x2))
else:
    print("该方程没有实根")
