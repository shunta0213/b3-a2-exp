#####
##   計算量で無理
#####

# mの値を設定
m = 20040213

def lcg_period(a, c, m, seed):
    initial = seed
    next_value = (a * seed + c) % m
    count = 1
    while next_value != initial:
        seed = next_value
        next_value = (a * seed + c) % m
        count += 1
        if count > m:  # 保険としての上限
            return -1  # 理論的には周期はmを超えないはず
    return count

# 条件を満たす a と c を見つける関数
def find_optimal_ac(m):
    periods = []
    for a in range(1, m, 2):
        for c in range(1, m, 2):
            period = lcg_period(a, c, m, 0)
            if len(periods) == 0:
                periods.append((a, c, period))
            else:
                if period > periods[-1][2]:
                    periods.append((a, c, period))
            print(a, c, period)
    return periods



print(find_optimal_ac(m))
