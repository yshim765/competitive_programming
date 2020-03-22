#%%
s = "0 3"

#%%

import math

n, m = input().split()
n, m = int(n), int(m)

def calc(x):
    if x >= 2:
        return math.factorial(x) / (math.factorial(x - 2) * 2)
    else:
        return 0

even = (calc(n)) + (calc(m))

print(int(even))

# %%
