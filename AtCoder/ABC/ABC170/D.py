#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

n = int(input())
a = list(map(int,input().split()))

a.sort()

max_a = a[-1]
is_available = [True] * (max_a + 1)

ans = 0

for i, x in enumerate(a[:-1]):
    if is_available[x]:
        if not a[i+1] == x:
            ans += 1
        for b in range(x, max_a + 1, x):
            is_available[b] = False

if is_available[a[-1]]:
    ans += 1

print(ans)

# %%
