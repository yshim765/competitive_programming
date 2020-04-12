#%%
n, m = input().split()
n, m = int(n), int(m)

#%%

def calc_saidaikouyaku(a, b):
    if (b == 0):
        return(a)
    
    return calc_saidaikouyaku(b, a % b)

k = int(input())

result = []

for a in range(1, k + 1):
    for b in range(1, k + 1):
        for c in range(1, k + 1):
            result.append(calc_saidaikouyaku(a, calc_saidaikouyaku(b, c)))

print(sum(result))


# %%
