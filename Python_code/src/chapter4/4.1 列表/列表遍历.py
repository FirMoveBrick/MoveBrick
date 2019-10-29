mylist = [1,2,3,'abc',[1,2,'c']]
# 1. in遍历
for item in mylist:
    print(item,end=' ')
print()
#2. range xrange
listLen = len(mylist)
for i in range(listLen):
    print(i, end=' ')
print()
# 3. item迭代器
for item in iter(mylist):
    print(item, end=' ')
print()
# 4. enumerate函数
for item in enumerate(mylist):
    print(item, end=' ')
print()