# 利用lanbda函数，实现四则运算表达式
add = lambda x, y: x+y
jian = lambda x, y: x-y
cheng = lambda x, y: x * y
chu = lambda x, y: x / y
def add(x,y):
    # print("计算器")
    return lambda:x + y
def jian(x,y):
    # print("计算器")
    return lambda:x - y
def cheng(x,y):
    # print("计算器")
    return lambda:x * y
def chu(x,y):
    # print("计算器")
    return lambda:x / y
a = input("请输入第一位数")
b = input("请输入第二位数")
print('{0}和{1}四则运算为{2}'.format(a,b,jian(a,b)()))
