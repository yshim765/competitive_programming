#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

n = int(input())

a = list(map(int,input().split()))

result = 1

if 0 in a:
    result = 0
else:
    for x in a:
        result *= x
        if result > 10 ** 18:
            result = -1
            break

print(result)

#%%
10 ** 18

# %%
