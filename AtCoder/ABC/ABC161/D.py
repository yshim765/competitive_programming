#%%
n, m = input().split()
n, m = int(n), int(m)

#%%

# k = int(input())
k = int("100000")

x = [0]

while(k > 0):
    len_x = len(x)

    if len_x == 1:
        if x[0] != 9:
            x[0] = x[0] + 1
        else:
            x[0] = 1
            x.append(0)
    elif len_x == 2:
        if (x[0] == 9 and x[1] == 9):
            x = [0] * len(x)
            x.insert(0, 1)
        elif x[1] - x[0] < 1:
            x[1] += 1
        else:
            x[0] += 1
            x[1] = x[0] - 1
    else:
        for i in range(len_x):
            if sum(x) == 9 * len_x:
                x = [0] * len(x)
                x.insert(0, 1)
                break
            elif i == len_x - 1:
                x[0] += 1
                temp = x[0]
                x = [temp - i if temp - i >= 0 else 0 for i in range(len_x)]
                break
            elif x[-1 - i] - x[-2 - i] < 1:
                if x[-1 - i] == 9:
                    continue
                x[-1 - i] = x[-1 - i] + 1
                temp = x[-1 - i]
                for j in range(i):
                    j = i - j
                    x[-j] = x[-1 -j] - 1 if x[-1 -j] - 1 >= 0 else 0
                break
    k -= 1

print("".join([str(x) for x in x]))

# %%
