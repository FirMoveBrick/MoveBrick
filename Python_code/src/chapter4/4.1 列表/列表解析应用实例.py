import random

# 输出10随机数存放在列表中
mylist = [random.randint(1,100) for i in range(10)]
print(mylist)

# 输出随机数的平方根
mylist1 = [i * i for i in mylist]
print(mylist1)

# 挑选偶数
mylist2 = [ i for i in mylist if i%2==0]
print(mylist2)

mymatrix = [
    [1,3,5,8],
    [4,2,6,7],
    [9,0,4,2]
]
print('按行遍历矩阵')
print([row for row in mymatrix])
print('按列遍历矩阵')
print([mymatrix[row][1] for row in range(3)])

print('遍历每一个矩阵')
print([mymatrix[x][y] for x in range(3) for y in range(4)])