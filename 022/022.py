# https://leetcode-cn.com/problems/generate-parentheses/description/

def gen(v,s,l,r):
    if l==0 and r==0:
        v.append(s)
    if l>0:
        gen(v,s+'(',l-1,r)
    if r>0 and l<r:
        gen(v,s+')',l,r-1)

v = []
gen(v,'',3,3)
print(v)
