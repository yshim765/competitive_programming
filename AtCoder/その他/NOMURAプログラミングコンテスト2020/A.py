#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

h1, m1, h2, m2, k = map(int,input().split())

print(int(h2*60 + m2 - h1*60 - m1 - k))

# %%
