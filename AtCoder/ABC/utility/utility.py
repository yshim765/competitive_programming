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
# いもす法による要素の重なりの計算
# 複数の矩形関数を足した和を計算する時に使う

# 1次元配列の場合
# 初期値がすべて 0 の 10個の範囲を考える [0 0 0 0 0 0 0 0 0 0]
# これに、次の3つの値を足す
# [1 1 1 0 0 0 0 0 0 0]
# [0 0 0 0 1 1 1 1 0 0]
# [0 0 0 0 0 1 1 1 1 1]
# 結果として、次の値が得られる
# [1 1 1 0 1 2 2 2 1 1]
# 愚直にやると3 * 10 回計算が必要だが、いもす法を使うと 3*2 + 10 回の計算で済む

n = 10

start = [0, 4, 5]
end = [2, 7, 9]


arr = [0] * n

for i in range(len(start)):
    arr[max(0, start[i])] += 1
    
    if end[i] + 1 < n:
        arr[end[i] + 1] -= 1

for i in range(len(arr) - 1):
    arr[i + 1] += arr[i]

print(arr)

#%%

# 2次元配列の場合
# 愚直にやると3 * 6 * 10 回計算が必要だが、いもす法を使うと 3*4 + 6*10 回の計算で済む
# 座標は[x, y]で入っているものとする

n_y = 6
n_x = 6

start = [[0, 0], [2, 2], [1, 3]]
end = [[3, 3], [5, 5], [2, 4]]


arr = [[0] * n_x for _ in range(n_y)]

for i in range(len(start)):
    arr[max(0, start[i][1])][max(0, start[i][0])] += 1

    if end[i][0] + 1 < n_x:
        arr[max(0, start[i][1])][end[i][0] + 1] -= 1

    if end[i][1] + 1 < n_y:
        arr[end[i][1] + 1][max(0, start[i][0])] -= 1

    if (end[i][0] + 1 < n_x) and (end[i][1] + 1 < n_y):
        arr[end[i][1] + 1][end[i][0] + 1] += 1

for y in range(n_y):
    for x in range(1, n_x):
      arr[y][x] += arr[y][x - 1]

for y in range(1, n_y):
    for x in range(n_x):
      arr[y][x] += arr[y - 1][x]

for temp in arr:
    print(temp)

# %%
# 素因数分解をする
# 返り値は [[素因数1, 素因数1の数], [素因数2, 素因数2の数], ...]
# n = 2 -> prime_factor = [[2, 1]]
# n = 120 -> prime_factor = [[2, 3], [3, 1], [5, 1]]
# n = 1 -> prime_factor = []

def factorization(n):
    arr = []
    temp = n

    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp > 1:
        arr.append([temp, 1])

    return arr

n = 120

prime_factor = factorization(n)

print(n)
print(prime_factor)

# %%
# 正の整数に対する math を使わない切り捨て、切り上げ

n = 1.5

# 切り捨て
n_floor = int(n)

print(n_floor)

# 切り上げ
n_ceil = int(-(-n//1))

print(n_ceil)
