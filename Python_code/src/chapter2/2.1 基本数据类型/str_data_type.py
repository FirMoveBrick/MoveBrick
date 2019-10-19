mystr = 'I\'am a student'
print(mystr,type(mystr),len('my major is conputer'))
print('c:\\add\name')
print(r'c:\\add\name')
# + 表字符串连接 *运算符进行字符串重复
print('hello,'+mystr,mystr * 2)
#对字符串进行切片，默认下标为0
print(mystr[1:9])
print(mystr + ' My major is conputer')
print(mystr.find('am'))
print(mystr.lower(),mystr.upper())
# 替换匹配的字符串
print(mystr.replace('student','teacher'))

mystr1 = 'PythonInteresting'
print('%s swapcase = %s' % (mystr1,mystr1.swapcase()))