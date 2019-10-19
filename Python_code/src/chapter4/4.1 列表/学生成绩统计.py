
print("学生成绩统计")
num=int(input("请输入学生人数："))
grade=[]
if(num<0):
    print("输入错误！")
    exit(0)
for i in range(num):
    stu=[]
    stu.append(input("请输入学生的学号："))
    stu.append(input("请输入学生的姓名："))
    stu.append(int(input("请输入学生的语文成绩：")))
    stu.append(int(input("请输入学生的数学成绩：")))
    stu.append(int(input("请输入学生的英语成绩：")))
    stu.append(int(input("请输入学生的综合成绩：")))
    grade.append(stu)
for i in range(num):
    stu=grade[i]
    stu.append(stu[2]+stu[3]+stu[4]+stu[5])
    stu.append(stu[6]/4)
for i in range(num):
    print(grade[i]) 
yuwen=[]
shuxue=[]
yingyu=[]
zonghe=[]
zp=[]  
for i in range(num):
    yuwen.append(grade[i][2])
    shuxue.append(grade[i][3])
    yingyu.append(grade[i][4])
    zonghe.append(grade[i][5])
    zp.append(grade[i][7])
maxyuwen=max(yuwen)
minyuwen=min(yuwen)
maxshuxue=max(shuxue)
minshuxue=min(shuxue)
maxyingyu=max(yingyu)
minyingyu=min(yingyu)
maxzonghe=max(zonghe)
minzonghe=min(zonghe)
maxzp=max(zp)
minzp=min(zp)
yuwenp=sum(yuwen)/num
shuxuep=sum(shuxue)/num
yingyup=sum(yingyu)/num
zonghep=sum(zonghe)/num
zpf=sum(zp)/num
print("{0}最高分是{1}，{0}最低分是{2},平均分是{3:.2f}".format('语文',maxyuwen,minyuwen,yuwenp))
print("{0}最高分是{1}，{0}最低分是{2},平均分是{3:.2f}".format('数学',maxshuxue,minshuxue,shuxuep))
print("{0}最高分是{1}，{0}最低分是{2},平均分是{3:.2f}".format('英语',maxyingyu,minyingyu,yingyup))
print("{0}最高分是{1}，{0}最低分是{2},平均分是{3:.2f}".format('综合',maxzonghe,minzonghe,zonghep))
print("总平均分是{0:.2f}".format(zpf))