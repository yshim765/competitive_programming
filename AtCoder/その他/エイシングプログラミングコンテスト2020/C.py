#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

import math, itertools

n = int(input())

result_dict = {}

for x in range(1, int(math.sqrt(10000) + 1)):
    for y in range(1, int(math.sqrt(10000) + 1)):
        for z in range(1, int(math.sqrt(10000) + 1)):
            result_dict[(x, y, z)] = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x

result = list(result_dict.values())

import collections

num_dict = dict(collections.Counter(result))

for i in range(1, n + 1):
    print(num_dict.get(i, default=0))