#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
import random

random.seed(1)

def calc_point(point_list, interval, choice):
    point = 0

    for i, day in enumerate(interval):
        point -= c[i] * day

    point += point_list[choice - 1]

    return point

d = int(input())

c = list(map(int,input().split()))

s = []

for _ in range(d):
    temp = list(map(int,input().split()))

    s.append(temp)

choices = []

for i in range(d):
    choices.append(s[i].index(max(s[i])) + 1)

interval = [0] * 26
result = 0

for i in range(d):
    choice = choices[i]

    interval = [x + 1 for x in interval]

    interval[choice - 1] = 0

    result += calc_point(s[i], interval, choice)

for _ in range(1000):
    temp_choices = choices.copy()
    temp_result = 0

    temp_choices[random.randint(0, d - 1)] = random.randint(1, 26)

    interval = [0] * 26
    
    for i in range(d):
        choice = temp_choices[i]

        interval = [x + 1 for x in interval]

        interval[choice - 1] = 0

        temp_result += calc_point(s[i], interval, choice)

    if temp_result > result:
        choices = temp_choices
        result = temp_result

for choice in choices:
    print(choice)
