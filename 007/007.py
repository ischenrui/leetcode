# https://leetcode-cn.com/problems/reverse-integer/description/
x = -214

# s = str(x)
# rs = ""
# if s[0]=='-':
#     rs +='-'
#     s = s[1:]
# print(s)
#
# for i in range(len(s)):
#     rs+=s[len(s)-1-i]
# print(rs)

s = (x > 0) - (x < 0)
r = int(str(x*s)[::-1])
print( s*r * (r < 2**31))