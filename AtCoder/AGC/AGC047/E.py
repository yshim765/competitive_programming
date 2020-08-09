#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

print(322)
print("+ 0 1 3")
print("< 4 3 4")

print("+ 4 6 6")

for i in range(9):
    print("+ {} {} {}".format(4, 6 + i, 7 + i))

for i in range(10):
    print("< 1 {} {}".format(6 + i, 16 + i * 11))

    for j in range(10):
        print("< {} 0 {}".format(5 + j, 17 + j + i * 11))

for i in range(10):
    for j in range(10):
        print("< {} {} {}".format(16 + i * 11, 17 + j + i * 11, 126 + j + i * 10))

for i in range(10):
    for j in range(10):
        print("+ 2 {} 2".format(126 + j + i * 10))

