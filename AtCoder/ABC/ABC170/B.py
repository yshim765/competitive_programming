#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

x, y = map(int,input().split())

if float.is_integer(-x + y/2) and float.is_integer(2 * x - y/2) and (0 <= 2 * x - y/2) and (0 <= -x + y/2):
    print("Yes")
else:
    print("No")



# %%
