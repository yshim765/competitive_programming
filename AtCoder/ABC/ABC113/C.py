n, m = input().split()
n, m = int(n), int(m)

data = []

for i in range(m):
    temp_p, temp_y = input().split()
    temp_p, temp_y = int(temp_p), int(temp_y)
    data.append([temp_p, temp_y, i])

data.sort()

result = [[] for _ in range(m)]

i = data[0][0]

k = 1

for j in range(m):
    if i != data[j][0]:
        k = 1
        i = data[j][0]
    result[data[j][2]] = [data[j][0], k]
    k += 1

for temp_data in result:
    print("{:0>6}".format(temp_data[0]) + "{:0>6}".format(temp_data[1]))