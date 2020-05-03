#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

import math

a, b, n = map(int,input().split())

if n < b:
    x = n
else:
    x = b - 1

c = x / b - math.floor(x / b)

print(math.floor(a * c))

# %%
