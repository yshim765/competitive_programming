#%%
n, m = input().split()
n, m = int(n), int(m)

x = input().split()
x = [int(x) for x in x]

#%%

input_string = \
"""
4 3
1 2 3
4 5 6
7 8 9
10 11 12
"""

input_string_list = input_string.split("\n")[1:-1]

n, m = input_string_list[0].split()
n, m = int(n), int(m)

x = []

for i in range(n):
    x.append(input_string_list[i + 1].split())
    x[i] = [int(x) for x in x[i]]

print(n, m)
print(x)

# %%
