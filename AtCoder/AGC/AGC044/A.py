#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

from collections import deque

# t = int(input())

# l = []

# for _ in range(t):
#     n, a, b, c, d = map(int,input().split())
#     l.append([n, a, b, c, d])

result = []

l = [map(int,"32 10 8 5 4".split())]

for n, a, b, c, d in l:
    temp_deque = deque()
    
    temp_deque.append((n, 0))

    min_cost = float("inf")

    while len(temp_deque) != 0:
        temp_num, temp_cost = temp_deque.pop()

        if min_cost <= temp_cost:
            continue

        if (temp_num == 1) and (temp_cost < min_cost):
            min_cost = temp_cost
            continue

        if temp_num % 2 == 0:
            temp_deque.append((temp_num / 2, a + temp_cost))
        if temp_num % 3 == 0:
            temp_deque.append((temp_num / 3, b + temp_cost))
        if temp_num % 5 == 0:
            temp_deque.append((temp_num / 5, c + temp_cost))

        temp_deque.append((temp_num + 1, d + temp_cost))
        temp_deque.append((temp_num - 1, d + temp_cost))

    result.append(min_cost + d)

print(result)


# %%
