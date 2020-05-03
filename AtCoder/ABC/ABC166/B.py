#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

n, k = map(int,input().split())

x = set()

for _ in range(k):
    input()

    temp1 = list(map(int,input().split()))

    for temp2 in temp1:
        x.add(temp2)

print(n - len(x))

# %%
