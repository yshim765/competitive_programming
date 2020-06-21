#%%
a = int(input())

n, m = map(int,input().split())

x = list(map(int,input().split()))

# %%

n = int(input())

def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)

ans = num2alpha(n)

print(ans.lower())


# %%

n = int(input())

def num_base10_to_num_baseN(num_base_10, base_N):
    if num_base_10 < base_N:
        return [num_base_10]
    else:
        result_list = num_base10_to_num_baseN(num_base_10 // base_N, base_N)
        result_list.append(num_base_10 % base_N)
        return result_list

s = num_base10_to_num_baseN(n, 26)

for i in range(len(s) - 1, 0, -1):
    if s[i] <= 0:
        s[i] += 26
        s[i - 1] -= 1

print("".join([chr(96 + x) for x in s if x != 0]))

