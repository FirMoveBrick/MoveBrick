# input()输入的是字符串  假如要转类型必须强制转化
year = int(input("请输入年份:"))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("是闰年")
else:
    print("不是闰年")
