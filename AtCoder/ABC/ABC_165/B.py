#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

import math

x = int(input())

n = 100

i = 0

while n < x:
    n = math.floor(n * 1.01)
    i += 1

print(i)

# %%
