#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%
import sys

N,K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

P = []
M = []
Ans = []
p = 0
m = 0

for i in range(N):
    if 0 <= A[i]:
        P.append(A[i])
    else:
        M.append(A[i])

M.sort()

if K % 2 == 1 and len(P) != 0:
    Ans.append(P[p])
    p += 1
elif K % 2 == 1 and len(P) == 0:
    M.sort(reverse=True)
elif len(M) == 0:
    answer = 1
    for i in range(K):
        answer = (answer * P[i]) % 1000000007

    print(answer)
    sys.exit()

while len(Ans) < K:

    #Mのストックがもうない時
    if m+1 >= len(M) and p < len(P):
        Ans.append(P[p])
        if len(Ans) == K:
            break
        if p + 1 < len(P):
            Ans.append(P[p + 1])
            p += 2
        else:
            p += 1
        
    elif p+1 >= len(P) and m < len(M):
        Ans.append(M[m])
        if len(Ans) == K:
            break
        Ans.append(M[m + 1])
        m += 2
    elif m >= len(M) and p < len(P):
        Ans.append(P[p])
        p += 1
    elif p >= len(P) and m < len(M):
        Ans.append(M[m])
        m += 1
    else:
        if P[p]*P[p+1] < M[m]*M[m+1]:
            Ans.append(M[m])
            Ans.append(M[m+1])
            m += 2
        else:
            Ans.append(P[p])
            Ans.append(P[p + 1])
            p += 2

answer = 1
for i in range(K):
    answer = (answer * Ans[i]) % 1000000007

print(answer)
