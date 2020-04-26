#%%
n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

# 参考 https://kakedashi-engineer.appspot.com/2020/04/26/abc164/

N = 2019
cnt = [0] * N
S = input()
ans = 0
for s in S:
    s = int(s)
    new = [0] * N
    for n in range(N):
        idx = (10 * n + s) % N
        new[idx] += cnt[n]
    cnt = new
    cnt[s] += 1
    ans += cnt[0]
print (ans)

# %%
