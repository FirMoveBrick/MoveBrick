# 某种商品对于订购数量小于100个的订单无折扣，100~200个的订单折扣1.5%，
# 200~500个的订单折扣常是5，5%，500个以上的订单折扣率是5%。
# 编写程序，输入商品的单价和数量，计算付款额。
print("输入商品的单价和数量，计算付款额")
money = int(input('商品单价'))
count = int(input("商品数量"))
if money<=0 and count<=0:
    print("商品数量或单价不能为0")
if count < 100:
    po =  money*count
elif 100<=count<=500:
    po = money * count*(1 - 0.035)
else:
    po =money * count * (1-0.05)

print('{0}*{1}={2}'.format(money,count,po))