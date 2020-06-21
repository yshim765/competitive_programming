#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

import collections

n = int(input())

a = list(map(int,input().split()))

q = int(input())

num_dict = dict(collections.Counter(a))

temp = [key * value for key, value in num_dict.items()]

ans = sum(temp)

for _ in range(q):
    b, c = map(int,input().split())

    if num_dict.get(b):
        num_dict[c] = num_dict[b] + num_dict.get(c, default=0)

        ans = ans - num_dict[b] * b + num_dict[b] * c

        del(num_dict[b])

    print(ans)
