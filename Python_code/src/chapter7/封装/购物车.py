import os
import csv
import copy
# 定义购物车类
class Cart:
    #定义构造方法，购物车列表初始化为空
    def __init__(self):
        # 定义私有实例变量
        self.__myCary = []

    # 定义实例化方法，用于完成购物车中商品添加功能
    def addGoods(self,goods):
        pass

    # 展示购物车所购商品
    def displayCart(self ):
        pass
    # 定义修改购物车信息的方法
    # param goodid  商品编号
    # param goodnum 商品编号
    def modifyGoods(self,goodid,goodnum):
        pass

    # 定义清空购物车的方法
    def deleteAllGoods(self):
        pass

    #定义购物车信息文件打开方法
    def openUserCart(self):
        pass

    #定义购物车信息保存方法
    def saveUserCart(self):
        pass

# 定义用户接口的主方法
def main():
    file = r'D:\Python_code\src\chapter7\goodinfo.csv'
    goodList = []
    titleList = []
    # print(len(titleList))
    # exit()
    with open(file,'r') as csvfile:
        lines = csv.reader(csvfile)
        for line in lines:
            if line!=[]:
                goodList.append(line)
        titleList = goodList[0]
        goodList = goodList[1:]
    # 初始化实例对象
    userCart = Cart
    while (True):
        # 输出菜单，让用户选择要执行的操作
        print('{:<14}'.format('1.添加商品到购物车'),end='  ')

main()