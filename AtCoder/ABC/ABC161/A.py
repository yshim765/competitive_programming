#%%
n, m = input().split()
n, m = int(n), int(m)

#%%

x, y, z = input().split()
x, y, z = int(x), int(y), int(z)

x, y = y, x
x, z = z, x

print(x, y, z)