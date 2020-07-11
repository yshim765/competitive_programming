#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
l, r, d = map(int,input().split())

ans = 0

temp = d

while temp <= 100:
    if (l <= temp) and (temp <= r):
        ans += 1

    temp += d

print(ans)