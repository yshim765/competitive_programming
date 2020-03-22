#%%
import copy, math, collections

n = int(input())
a = input().split()

result = []

num_dict = dict(collections.Counter(a))

def calc(x):
    if x >= 2:
        return math.factorial(x) / (math.factorial(x - 2) * 2)
    else:
        return 0

result_dict = {}
result_minus1_dict = {}

for key, value in num_dict.items():
    result_dict[key] = calc(num_dict[key])
    result_minus1_dict[key] = calc(num_dict[key] - 1)

result_all = sum(result_dict.values())

for i in range(len(a)):
    print(int(result_all - result_dict[a[i]] + result_minus1_dict[a[i]]))

# %%
