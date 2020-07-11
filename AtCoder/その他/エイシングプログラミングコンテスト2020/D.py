#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
n = int(input())
x = input()

num_of_1 = x.count("1")

x_num = int(x, 2)

def f(x):
    if x == 0:
        return 0
    return 1 + f(x % bin(x).count('1'))

if num_of_1 == 1:
    for i in range(n):
        if x[i] == '1':
            print(0)
        elif i == n-1:
            print(2)
        else:
            print(1)
    exit()

# 大きい数の計算は時間がかかるので先に剰余をとって小さくしておく
a = x_num % (num_of_1 + 1)
b = x_num % (num_of_1 - 1)

for i in range(n):
    if x[i] == "0":
        print(1 + f((a + pow(2, n-i-1, num_of_1 + 1)) % (num_of_1 + 1)))
    else:
        print(1 + f((b - pow(2, n-i-1, num_of_1 - 1)) % (num_of_1 - 1)))
