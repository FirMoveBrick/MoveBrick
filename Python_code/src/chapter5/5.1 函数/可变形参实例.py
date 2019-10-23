def func(a,b = "Python",*tupleArg,**dictArg):
    print("a = ",a)
    print("b = ",b)
    for i,elem in enumerate(tupleArg):
        print('tupleArg(元祖对象)%d-->%s'%(i,str(elem)))
    for key in dictArg:
        print("dict(字典对象) %s --> %s" % (key,dictArg[key]))
def main():
    myList = ['苹果','菠萝','哈密瓜','西瓜']
    myDict = {"name":"Tom","age":"22"}
    # 第一次函数调用，只传递一个参数，其他形式使用默认值
    func('第一个实参')
    # 分隔符
    print('*' * 40)
    # 第二次函数调用，只传递两个参数，其他形式使用默认值
    func('1','2',0)
    print('*' * 40)
    func(345,myList,myDict)
    print('*' * 40)
    func(345,rt = 123, *myList,**myDict)

main()