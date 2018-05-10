# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
s = "cccc"

if len(s)==1:print(s)
echo = ""
for i in range(1,len(s)):
    if i==1 and s[i-1]==s[i]: echo = s[:2]
    elif s[i] == s[i-2]:
        j = 0
        while i-1+j<len(s) and i-1-j>=0 and s[i-1+j] == s[i-1-j]:
            j += 1
            if len(echo)<1+2*(j-1): echo = s[i-j:i-1+j]
    if s[i] == s[i-1]:
        j = 0
        while i+j<len(s) and i-1-j>=0 and s[i+j] == s[i-1-j]:
            j += 1
            if len(echo) < 2 * j: echo = s[i-j:i+j]

print(echo)