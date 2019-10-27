# 编写递归与非递归数列 输出斐波那契数列 1,1,2,3,5,8
# 非递归数列
print("非递归数列")
a = 0
b = 1
while b<1000:
    print(b,end=' ')
    a,b = b,a+b\

print("\n递归数列")

def func(n):
    # 给递归一个出口  第一位和第二位都是1
    if n == 1 or n == 2:
        return 1
    else:
        # 从第三位开始  返回上一个数加上上一个数
        return func(n-1) + func(n-2)


print(func(int(input("请输入第几项斐波那契数列"))))

