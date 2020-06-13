#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

a, v = map(int,input().split())

b, w = map(int,input().split())

t = int(input())

if (v <= w):
    print("NO")
else:
    dist = abs(a - b)
    if dist - (v - w) * t > 0:
        print("NO")
    else:
        print("YES")