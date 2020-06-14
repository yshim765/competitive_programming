#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

x, n = map(int,input().split())

if n != 0:
    p = list(map(int,input().split()))
else:
    p = []

result = []

i = 0

while len(result) == 0:
    if not (x - i in p):
        result.append(x - i)
    if not (x + i in p):
        result.append(x + i)
    
    i += 1

print(int(min(result)))


# %%
