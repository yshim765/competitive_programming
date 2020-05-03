#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
import math

x = int(input())

res = {}

for a in range(-200, 200):
    for b in range(-200, 200):
        temp = math.pow(a, 5) - math.pow(b, 5)
        res[temp] = (a, b)

print(res[x][0], res[x][1])

# %%

a = 1
b = -2

a - math.pow(math.pow(b, 5) + 33, 1/5)

# %%
