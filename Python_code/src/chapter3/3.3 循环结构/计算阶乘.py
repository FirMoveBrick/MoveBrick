print("本程序计算N的阶乘")
num= int(input("请输入一个正整数： "))
s = 1
for i in range(1,num+1):
    s = s*i
print('{0}! = {1}'.format(num,s))