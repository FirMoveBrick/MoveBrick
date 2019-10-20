# 编写一个程序，输入一个小数，计算小数点左、右各有几个小数
print("请输入一个数字")
number = float(input("数字:"))
first = str(int(number)) + '.' if(int(number) == number) else str(number)
# split方法是通过指定的字符串进行切片，第一个参数是切片次数
strs = first.split('.',2)
count = [len(x) for x in strs]
print('left = {0} \nright ={1}'.format(len(strs[0]) , len(strs[1])) )
