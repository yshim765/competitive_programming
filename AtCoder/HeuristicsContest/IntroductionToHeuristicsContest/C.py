#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
d = int(input())

c = list(map(int,input().split()))

s = []

for _ in range(d):
    temp = list(map(int,input().split()))

    s.append(temp)

choices = []

for _ in range(d):
    temp = int(input())

    choices.append(temp)

m = int(input())

queries = []

for _ in range(m):
    temp = list(map(int,input().split()))

    queries.append(temp)

changed_choices = [choices]

for day, new_choice in queries:
    temp = changed_choices[-1].copy()

    temp[day - 1] = new_choice

    changed_choices.append(temp)

def calc_point(point_list, interval, choice):
    point = 0

    for i, day in enumerate(interval):
        point -= c[i] * day

    point += point_list[choice - 1]

    return point

for temp_choices in changed_choices[1:]:
    interval = [0] * 26

    result = 0

    for i in range(d):
        choice = temp_choices[i]

        interval = [x + 1 for x in interval]

        interval[choice - 1] = 0

        result += calc_point(s[i], interval, choice)

    print(result)

