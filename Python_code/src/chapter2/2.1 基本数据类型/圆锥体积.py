import math     #引入数学函数模块
print("计算圆锥的体积，请输入相关的数据")
radius = float(input("圆锥半径"))
height = float(input("圆锥高"))

volume = 1/3*math.pi*radius**2*height
print("圆锥的体积={0:.2f}".format(volume))