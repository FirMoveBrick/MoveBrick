a,b,c,d = 20,3.5,False,5+6j;
print(type(a),type(b),type(c),type(d))  #输出数据类型
e = 2017000000120000002017
f = e + 5
print(e)                                #输出长整形
print(f)

# 表示2017 * 10的0次方
g = 2.17e0 + 18
print(g)                                 #输出浮点型

print(bin(28),oct(28),hex(28))          #输出10进制的27对应的值
print(bin(0*28),oct(0*28),hex(0*28))

print(int(23.3),float(23))              #使用函数转换数据类型

a = 22
print(isinstance(a,float))              #判断数据是否是否个数据类型
print(isinstance(24.2,float))

print(complex(5))                       #整数转换为负数
print(complex(5,4))