print("本程序判断表达式的括号是否匹配""")
exp = input("请输入一个带括号的表达式")
S = []
for i in exp:
    if(i == '('):
        S.append(i)
    if(i == ')'):
        if (len(S) == 0):
            print('缺少左括号')
            exit()
        else:
            S.pop()

if(len(S) == 0):
    print("括号匹配")
else:
    print("左括号多于右括号，不匹配！")