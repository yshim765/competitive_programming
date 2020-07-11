#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

n = int(input())

a = list(map(int,input().split()))

ans = 0

for i, a in enumerate(a):
    if (i + 1) % 2 == 1:
        if a % 2 == 1:
            ans += 1

print(ans)