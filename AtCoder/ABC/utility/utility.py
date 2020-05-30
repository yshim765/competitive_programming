#%%
# 高速に出現回数を計算する
# 4 * 10**7 個で2秒弱くらい

temp = [1, 2, 3, 1] * 10**7

import collections

num_dict = dict(collections.Counter(temp))

print(num_dict)

# %%
# 2つの数の最大公約数(greatest common divisor)を求める
# 3つの場合でも、gcd(a, gcd(b, c))みたいにして求める
# 3つ以上でも同様

def gcd(a, b):
    if (b == 0):
        return(a)
    
    return gcd(b, a % b)


# %%
# 2つの数の最小公倍数(least common multiple)を求める
# 最小公倍数と最大公約数の積が2数の積と等しいことを使う

def gcd(a, b):
    if (b == 0):
        return(a)
    
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

# %%
# 重複組み合わせを全列挙する
# [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3],
# [1, 3, 3], [2, 2, 2] ... 的な奴

import itertools

# 長さ3, 最大5 の組み合わせを生成
n = 3
m = 5

for l in itertools.combinations_with_replacement([x for x in range(1, m + 1)], n):
    print(l)

# %%
# cumsum
# それまでの総和を求める
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> cumsum_l = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cumsum_l = l.copy()

for i in range(len(l) - 1):
    cumsum_l[i + 1] += cumsum_l[i]

print(cumsum_l)

#%%
# reverse_cumsum
# それ以降の総和を求める
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> reverse_cumsum_l = [55, 54, 52, 49, 45, 40, 34, 27, 19, 10]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reverse_cumsum_l = l.copy()

for i in range(len(l)-2, -1, -1):
    reverse_cumsum_l[i] += reverse_cumsum_l[i+1]

print(reverse_cumsum_l)

# %%
