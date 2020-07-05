#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
n = int(input())

a = list(map(int,input().split()))

a.sort(reverse=True)

ans = 0

ans += a[0]

for i in range(1, int(len(a)/2)):
    ans += a[i] * 2

if len(a) % 2 == 0:
    print(ans)
else:
    print(ans + a[int(len(a)/2)])