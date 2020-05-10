#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

import numpy as np

n = int(input())

l = []

for _ in range(n):
    s = input()
    s = list(map(int, s.replace("(", "3").replace(")", "1")))

    s = np.array(s) - 2

    cumsum = s.cumsum()
    l.append([cumsum[-1] - cumsum.min(), abs(cumsum.min())])

print(l)
# print("Yes" if sum(l) == 0 else "No")