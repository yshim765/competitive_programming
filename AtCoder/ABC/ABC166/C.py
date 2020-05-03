#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

n, m = map(int,input().split())

h = list(map(int,input().split()))

res =  [True] * n

for _ in range(m):
    x1, x2 = map(int,input().split())

    if h[x1 - 1] <= h[x2 - 1]:
        res[x1 - 1] = False
    if h[x2 - 1] <= h[x1 - 1]:
        res[x2 - 1] = False

print(sum(res))


# %%
