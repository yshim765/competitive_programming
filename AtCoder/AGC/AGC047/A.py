#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

n = int(input())

a = []

for _ in range(n):
    a.append(int(float(input()) * 10 ** 9))

print(a)