#%%

s = "abacaba"

#%%

s = input()

def kaibun_check(s):
    n = len(s)
    zenhan_s = s[:int((n - 1)/2)]
    zenhan = zenhan_s == zenhan_s[::-1]
    kouhan_s = s[int((n + 1)/2):]
    kouhan = kouhan_s == kouhan_s[::-1]
    return zenhan and kouhan and (s == s[::-1])

print("Yes" if kaibun_check(s) else "No")

# %%
