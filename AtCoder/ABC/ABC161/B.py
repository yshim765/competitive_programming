#%%
n, m = input().split()
n, m = int(n), int(m)

#%%

n, m = input().split()
n, m = int(n), int(m)

a = input().split()
a = [int(a) for a in a]

sum_a = sum(a)

a_can_choose = [True if a >= sum_a / (4 * m) else False for a in a]

print("Yes" if m <= sum(a_can_choose) else "No")

# %%
