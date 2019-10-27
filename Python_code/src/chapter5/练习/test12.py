# 编写函数，统计文本中单词出现的次数，用空格分隔
def main():
    print("请输入关键字和位置统计")
    str = input("输入文字")
    keywords = input("请输入若干字符关键字，用( )分割")
    # 用split方法切片输入的数据
    keys = keywords.split(' ')
    print(keys)
    result = keyscounds(str, keys)
    print(result)

def keyscounds(str,keys):
    # 初始化最终的列表，用于存放最终的数据
    result = []
    # 遍历关键字列表，对每个字符串进行统计
    for item in keys:
        # tmpstr用于存放下次和当前要用到的字符串
        tmpstr = str
        # 初始化出现的次数
        count = 0
        # 查找字符串位置
        location = tmpstr.find(item)
        # 初始化存放位置的列表
        loc = []
        # 初始化函数的切片位置
        length = 0
        # 余下的字符串继续查找，直到找不到为止
        while (location != -1):
            # 次数+1
            count += 1
            loc.append(location+length)
            # 计算下次检索的位置
            length += location + len(item)
            # 剪掉查找过的字符串
            tmpstr = tmpstr[length:]
            # 继续在为检索的字段查找关键字
            location = tmpstr.find(item)

        # 结果存放在列表中
        result.append([item, count, loc])
        return result

main()