#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

n, k = map(int,input().split())

a = list(map(int,input().split()))

tel_list = []

next_city = 0

city_have_been_to = set([0])

way = [0]

while k > 0:
    k -= 1
    temp = len(city_have_been_to)

    next_city = a[next_city] - 1
    city_have_been_to.add(next_city)
    way.append(next_city)

    if temp == len(city_have_been_to):
        break

if k == 0:
    print(way[-1] + 1)
else:
    temp_index = way.index(next_city)
    print(way[temp_index:-1][k % len(way[temp_index:-1])] + 1)


# %%
