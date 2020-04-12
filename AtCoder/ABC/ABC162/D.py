#%%
n, m = input().split()
n, m = int(n), int(m)

#%%

n = int(input())
s = input()

dict_x = {"R":0, "G":1, "B":2}
s = [dict_x[s] for s in s]

result = 0

for i in range(n):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            continue
        for k in range(j + 1, n):
            if (j - i) != (k - j):
                if s[i] + s[j] + s[k] == 3:
                    result += 1

print(result)

# %%
n = int(input())
s = input()
 
r_cnt = s.count('R')
g_cnt = s.count('G')
b_cnt = s.count('B')
 
ans = r_cnt * g_cnt * b_cnt
 
for i in range(n):
    for d in range(n):
        j = i + d
        k = j + d
        if k >= n:break
        if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
            ans -= 1
 
print(ans)