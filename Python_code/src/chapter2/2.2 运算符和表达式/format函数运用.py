import math

# 括号及里面的字符（称为格式化字段）将会被format（）函数中的参数代替
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# 括号中的数字用于指定传入对象在format（）函数中的参数位置，默认第一位是0
print('{0} and {1}'.format('chicken','eggs'))
print('{1} and {0}'.format('chicken','eggs'))

# 括号中的关键字参数用于指定该名字的参数的值
print('{one} and {two}'.format(one = "1",two = "2"))

# 保留后面7位小数
print('保留pai 后面7位小数{:.7f}'.format(math.pi))
# >18 固定宽度18个字符串
print('{:>18,.2f}'.format(123456.123))
# 通过下标参数匹配
fruit = ('apple','peach','oraneg')
print('fruit:{0[2]};{0[0]}'.format(fruit))