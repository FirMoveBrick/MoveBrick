import re #导入正则表达式
print("计算器")
str= input("请输入一个式子，如（2+3）")
p = re.compile(r'\d+')
op1 = int(p.findall(str)[0])
op2 = int(p.findall(str)[1])
q = re.compile(r'\W+')
opt = q.findall(str)[0]
# print(opt)
# exit()
# 检测除数是否为0
if ((opt == '/' or opt == '//' or opt == '%') and op2 == 0):
    print("除数不能为0")
    exit(0)
po = {
    '+':op1+op2,
    '-':op1-op2,
    '*':op1*op2,
    '/':op1/op2
}
result = po.get(opt)
print('{0}{1}{2}+{3}'.format(op1,opt,op2,result))