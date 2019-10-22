#利用随机数生成两个集合，集合元素是英文的小写字母，要求用户输入两个集合的运算结果，最后输出测试结果。
import random
n = random.randint(1,10)    #生成第一个集合的元素个数   例：7
m = random.randint(1,10)    #生成第二个集合的元素个数   例：2
set1 = set()                  #第一个集合初始化为空集
set2 = set()                  #第二个集合初始化为空集
# 通过集合元素给第一个集合添加n个元素
for i in range(n):
    #随机生成一个小写字母
    s = chr(random.randint(97,122))
    # 给集合赋值
    set1.add(s)
# 通过集合元素给第二个集合添加n个元素
for i in range(m):
    s = chr(random.randint(97, 122))
    set2.add(s)
op = random.randint(1,4)    #随机生成一个运算符的编号
# 如果条件为1，执行差集运算
if(op ==1):
    # 输出随机集合
    print("{0}-{1} = ".format(set1,set2))
    result = input("请输入结果：")
    # 将输入结果赋值给集合
    sety = set(result)
    # print(sety)
    # exit()
    # 执行集合运算结果
    setr = set1-set2
    if(sety == setr):
        print("正确")
    else:
        print("错误")
        print("正确答案为:{0}".format(setr))
# 如果条件为2，执行交集运算
if(op ==2):
    # 输出随机集合
    print("{0}&{1} = ".format(set1,set2))
    result = input("请输入结果：")
    # 将输入结果赋值给集合
    sety = set(result)
    # 执行集合运算结果
    setr = set1&set2
    if(sety == setr):
        print("正确")
    else:
        print("错误")
        print("正确答案为:{0}".format(setr))
# 如果条件为3，执行并集运算
if(op ==3):
    # 输出随机集合
    print("{0}|{1} = ".format(set1,set2))
    result = input("请输入结果：")
    # 将输入结果赋值给集合
    sety = set(result)
    # 执行集合运算结果
    setr = set1|set2
    if(sety == setr):
        print("正确")
    else:
        print("错误")
        print("正确答案为:{0}".format(setr))
# 如果条件为4，执行集合的对称差分运算
if(op ==4):
    # 输出随机集合
    print("{0}^{1} = ".format(set1,set2))
    result = input("请输入结果：")
    # 将输入结果赋值给集合
    sety = set(result)
    # 执行集合运算结果
    setr = set1^set2
    if(sety == setr):
        print("正确")
    else:
        print("错误")
        print("正确答案为:{0}".format(setr))