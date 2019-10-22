# 模拟扑克发牌：2副牌，4个人玩
import random

print('模拟扑克发牌')
# 定义牌的数字元组
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
# 定义牌的花色元组
suits = ['红桃', '方块', '梅花', '黑桃']
# 合并元组
puke = [(x, y) for x in suits for y in ranks]
# 54张牌乘2
pai = puke * 2
# 打乱列表值
cardRand = random.sample(pai, 104)
# 定义四个玩家
paly1 = []
paly2 = []
paly3 = []
paly4 = []
for i in range(26):
    paly1.append(cardRand.pop())
    paly2.append(cardRand.pop())
    paly3.append(cardRand.pop())
    paly4.append(cardRand.pop())
# 按花色分到的牌进行排序，key = lambda是固定写法 x是临时表示，x:x[0]表示第一个元素
paly1.sort(key=lambda x: x[0])
paly2.sort(key=lambda x: x[0])
paly3.sort(key=lambda x: x[0])
paly4.sort(key=lambda x: x[0])
# 输出
print("玩家1的牌")
i = 1
for eich in paly1:
    print(eich, end='')
    if (i % 6 == 0):
        print()
    i += 1
print("\n玩家2的牌")
i = 1
for eich in paly2:
    print(eich, end=' ')
    if (i % 6 == 0):
        print()
    i += 1
print("\n玩家3的牌")
i = 1
for eich in paly3:
    print(eich, end='')
    if (i % 6 == 0):
        print()
    i += 1
print("\n玩家4的牌")
i = 1
for eich in paly4:
    print(eich, end='')
    if (i % 6 == 0):
        print()
    i += 1
