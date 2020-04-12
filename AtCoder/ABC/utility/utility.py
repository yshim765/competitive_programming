#%%
# 高速に出現回数を計算する
# 4 * 10**7 個で2秒弱くらい

temp = [1, 2, 3, 1] * 10**7

import collections

num_dict = dict(collections.Counter(temp))

print(num_dict)

# %%
# 2つの数の最大公約数(greatest common divisor)を求める

def gcd(a, b):
    if (b == 0):
        return(a)
    
    return gcd(b, a % b)

# 3つの場合でも、gcd(a, gcd(b, c))みたいにして求める。3つ以上でも同様。