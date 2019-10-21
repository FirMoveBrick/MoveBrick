# 生成一幅扑克牌，有四个花色，每个花色有13只牌
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits = ['红桃','梅花','黑桃','方块']
print("生成一幅扑克牌")
for suit in suits:
    for rank in ranks:
        print(suit + rank,end=' ')
    print()