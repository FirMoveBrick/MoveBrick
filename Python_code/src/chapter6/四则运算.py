import random   #导入随机数
import pickle   #导入pickle模块
import os
def practice():
    formular = setQuestion()
    answerQuestion(formular)
def setQuestion():
    count = 0
    opr={1:'+',2:'-',3:'*',4:'/'}
    formular = []
    if os.path.exists('d:\\temp\\question.dat'):
        pkFile = open('d:\\temp\\question.dat','rb')
        data1 = pickle.load(pkFile)
        pkFile.close()
    else:
        data1 = []
    while True:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        opnum = random.randint(1,4)
        op = opr.get(opnum)
        result = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }[op](num1,num2)
        tmp = (num1,op,num2,result)
        if tmp in formular or tmp in data1:
            continue
        formular.append(tmp)
        count +=1
        if (count == 10):
            break
        data2 = data1[-21:-1]
        data2.extend(formular)
        pkFile = open('d:\\temp\\question.dat','rb')
        pickle.dump(data2,pkFile,-1)
        pkFile.close()
        return formular
def answerQuestion(formular):
    pass