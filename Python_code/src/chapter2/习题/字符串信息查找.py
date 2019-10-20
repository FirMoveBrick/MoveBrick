# 编写程序，用字符串保存一个通信录，然后查找某人所有的通讯信息
address="李明13567102011liming@126.com;\
刘东13667102012 liudong@163.com;\
张晓13584023115 zhangxiao@sina.com;\
陈旭阳18884026791 chenxuyang@sohu.com;\
欧阳贝贝15840236688 ouyangbeibei@sina.com;"
name = input("请输入要查找的姓名: ")
start = address.find(name)
end = address[start:]
second = end.find(";")+start

print(address[start:second])