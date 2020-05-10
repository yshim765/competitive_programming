#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

a, b, c, k = map(int,input().split())

if k <= a:
    print(k)
elif k <= a + b:
    print(a)
else:
    print(a - (k - a - b ))

# %%
