#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

x = list(map(int,input().split()))

for i, temp_x in enumerate(x):
    if temp_x == 0:
        print(i)
        break