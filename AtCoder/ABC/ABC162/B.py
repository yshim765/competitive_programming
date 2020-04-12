#%%
n, m = input().split()
n, m = int(n), int(m)

#%%

n = int(input())

result = []

for i in range(1, n + 1):
    if (i % 3 != 0) and (i % 5 != 0):
        result.append(i)

print(sum(result))


# %%
