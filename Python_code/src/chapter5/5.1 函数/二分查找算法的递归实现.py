# 在一个有序列表中用二分查找查找某个元素
# 设计思路
# 定义一个递归函数binarySearch（），找到中间位置的关键字进行比较。
# 若等于，则找到；若小于中间位置的关键字，用列表的左半边进行递归查找，否则用列表的右半边进行递归查找；
# 若起始位置大于终止位置，查找失败。

def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 22]
    print("二分查找测试")
    key1 = 1
    key2 = 19
    # 调用二分查找函数进行比较，起始位置为0，重点位置是最后一个
    result1 = binarySearch(list, key1, 0, len(list))
    result2 = binarySearch(list, key2, 0, len(list))
    # print('123')
    if (result1 != -1):
        print('{0}成功找到，位置为{1}'.format(key1, result1))
    else:
        print('{0}未找到'.format(key1))
    if (result2 != -1):
        print('{0}成功找到，位置为{1}'.format(key2, result2))
    else:
        print('{0}未找到'.format(key2))


def binarySearch(list, key, start, end):
    # print(end)
    #     # exit()
    if (list == -1 or end == -1):
        return -1
    if (start > end):
        return -1
    # if (key > list[end-1]):
    #     return -1
    mid = start + int((end - start) / 2)
    if (key == list[mid]):
        return mid
    elif (key < list[mid]):
        return binarySearch(list, key, start, mid - 1)
    else:
        return binarySearch(list, key, mid + 1, end)


main()
