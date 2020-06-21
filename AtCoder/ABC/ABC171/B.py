#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

n, k = map(int,input().split())

p = list(map(int,input().split()))

ans = 0

p.sort()

for i in range(k):
    ans += p[i]

print(ans)

# %%
