#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
n = int(input())
 
a = list(map(int,input().split()))
 
cumsum_a = a.copy()
 
for i in range(n-1, -1, -1):
    cumsum_a[i] += cumsum_a[i+1]
 
ans = 0
node = 1
 
for i in range(n + 1):
    if a[i] > node:
        ans = -1
        break
 
    ans += node
 
    if i < n:
        node = min(2 * (node - a[i]), cumsum_a[i + 1])
 
print(ans)

# %%
cumsum_a = numpy.cumsum(a[::-1])[::-1]
cumsum_a

# %%
