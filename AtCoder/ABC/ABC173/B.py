#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

import collections

n = int(input())

s = []

for _ in range(n):
    s.append(input())

s_total = dict(collections.Counter(s))

print("AC x", s_total.get("AC", default=0))
print("WA x", s_total.get("WA", default=0))
print("TLE x", s_total.get("TLE", default=0))
print("RE x", s_total.get("RE", default=0))

# %%
