#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
n, m = map(int,input().split())

j = 0

for i in range(1, m + 1):
    if (n - 2 * i + 1) == (2 * i - 1):
        j += 1
    print(i, n - i + 1 - j)


# %%
