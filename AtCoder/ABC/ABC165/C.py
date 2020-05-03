#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
import itertools

n, m, q = map(int,input().split())

x = []

for _ in range(q):
    x.append(list(map(int,input().split())))

res = 0

for l in itertools.combinations_with_replacement([x for x in range(m)], n):
    temp = 0
    
    for temp_x in x:
        if l[temp_x[1] - 1] - l[temp_x[0] - 1] == temp_x[2]:
            print(l)
            temp += temp_x[3]

    if res <= temp:
        res = temp

print(res)

# %%


# %%

import itertools

itertools.combinations_with_replacement([x for x in range(4)], 3)

# %%
