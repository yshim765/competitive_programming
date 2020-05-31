#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

# a_s, b_s = input().split()

# b_s = b_s.replace(".", "")

# s = str(int(a_s) * int(b_s))
# if len(s) > 2:
#     print(str(int(a_s) * int(b_s))[:-2])
# else:
#     print(0)

# %%
import decimal

a, b = input().split()

print(int(decimal.Decimal(a) * decimal.Decimal(b)))

# %%
