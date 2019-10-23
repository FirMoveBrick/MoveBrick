# （4）编写程序，输人一个整数，输出该整数的二进制编码，要求用堆栈来实现。
print("本程序输出一个整数的二进制编码")
a = int(input("请输入一个整数"))
# 将整数转化为二进制
b = bin(a).replace('0b','')
# 定义空列表
s = []
print('整数的二进制为 {0}'.format(b))
# 倒叙插到列表
for i in b:
    s.insert(0,i)
print('进栈序列为{}'.format(s))
print('出站,整数的二进制为',end=' ')
for i in range(len(s)):
    print(s.pop() ,end='')
