# 增
or_list = [1, "abc", 2.51]
or_list.append("JavaScript")    # append()方法在列表末尾追加元素(以整体形式追加)
or_list.insert(0, "Python")
print("or_list is: ", or_list)
print('-'*40)
ex_list = ["Python", 23, "game"]
or_list.extend(ex_list)         # extend()方法用于在列表末尾一次性追加另一个列表的多个值
print("or_list is: ", or_list)
# 删
print('-'*40)
del or_list[0:2]    # [0:2]删除第1个和第2个位置元素
print("or_list is: ", or_list)