#%%
# 高速に出現回数を計算する
# 4 * 10**7 個で2秒弱くらい

temp = [1, 2, 3, 1] * 10**7

import collections

num_dict = dict(collections.Counter(temp))

print(num_dict)

# %%
