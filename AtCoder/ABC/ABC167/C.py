#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

import itertools
from operator import add

n, m, x = map(int,input().split())

l = []

for _ in range(n):
    l.append(list(map(int,input().split())))

min_cost = -1

can = False

for buy_or_not in itertools.product(range(2), repeat=n):
    cost = 0
    m_list = [0] * m
    
    for i, j in enumerate(buy_or_not):
        if j:
            cost += l[i][0]
            m_list = list(map(add, m_list, l[i][1:]))

    m_check = [True if temp_m >= x else False for temp_m in m_list]

    if all(m_check):
        if min_cost == -1:
            min_cost = cost
        elif cost <= min_cost:
            min_cost = cost
    
print(min_cost)

# %%



# %%
