#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

k = int(input())

a, b = map(int,input().split())

res = "NG"

for i in range(a, b + 1):
    if i % k == 0:
        res = "OK"

print(res)

# %%
