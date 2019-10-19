# 编写一个Python程序，用户输入贷款额、利润和贷款年限后，计算每月的还款额
r = float(input("请输入月复合利润率"))
n = float(input("请输入贷款年限"))
A = float(input("请输入贷款总额"))
i = r / 1200
s = (i / (1 - (i + 1) ** (-12 * n))) * A
print('月还款额为{:.2f}'.format(s))
