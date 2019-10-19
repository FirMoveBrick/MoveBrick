# 用字符串保存所有的学生信息，末尾的\表示本行未结束，是续航符
address="李明13567102011liming@126.com;\
刘东13667102012 liudong@163.com;\
张晓13584023115 zhangxiao@sina.com;\
陈旭阳18884026791 chenxuyang@sohu.com;\
欧阳贝贝15840236688 ouyangbeibei@sina.com;"
name = input("请输入要查找的姓名: ")
# 获取名字
start = address.find(name)
# 找到记录信息的起始索引
temp = address[start:]
# 找到记录信息的尾索引
# 当前索引的值+查找字符串的值！
emd = temp.find(";") + start
#输出开始到结束的索引
print(address[start:emd])