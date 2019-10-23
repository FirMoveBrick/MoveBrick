# （8）编写程序，判断C语言源码中的大括号是否匹配。
print("本程序判断表达式的括号是否匹配""")
brace = input("请输入一个带大括号的表达式")
a = []
# print(len(a))
# exit()
for i in brace:
    if (i == '{'):
        a.append(i)
    if (i == '}'):
        if (len(a) == 0):
            print('缺少左大括号')
            exit()
        else:
            a.pop()
if(len(a) == 0):
    print('1')
else:
    print("缺少右括号")