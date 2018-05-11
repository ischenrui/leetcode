# https://leetcode-cn.com/problems/roman-to-integer/description/

s = 'MCMXCIV'
D = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1,'e':0}
ss = s+'e'
sum = 0

for i in range(len(ss)-1):
    if D[ss[i]]<D[ss[i+1]]:
        sum-=D[ss[i]]
    else:sum+=D[ss[i]]
print(sum)
