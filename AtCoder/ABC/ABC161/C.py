#%%
n, m = input().split()
n, m = int(n), int(m)

#%%

n, k = input().split()
n, k = int(n), int(k)

n = n % k
if n < k - n:
    print(n)
else:
    print(k - n)