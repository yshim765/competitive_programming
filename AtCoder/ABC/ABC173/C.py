#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
import itertools, copy

h, w, k = map(int,input().split())

c = []

for _ in range(h):
    c.append(list(input()))

ans = 0

iter_h_list = list(itertools.product([0,1], repeat=h))
iter_w_list = list(itertools.product([0,1], repeat=w))

for iter_h in iter_h_list:
    for iter_w in iter_w_list:
        temp_c = copy.deepcopy(c)

        for i in range(h):
            if iter_h[i] == 1:
                temp_c[i] = ["r" for x in temp_c[i]]

        for j in range(w):
            for i in range(h):
                if iter_w[j] == 1:
                    temp_c[i][j] = "r"

        sum_of_shape = [x.count("#") for x in temp_c]
        if sum(sum_of_shape) == k:
            ans += 1

print(ans)



