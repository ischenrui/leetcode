# https://leetcode-cn.com/problems/integer-to-roman/description/

def int2roman(num,a,b,c):
    if num == 0:return ""
    if num>0 and num<4:
        return a*num
    elif num==4:
        return a+b
    elif num>4 and num<9:
        return b+a*(num-5)
    elif num==9:
        return a+c

num = 1994
qian = int(num/1000)
bai = int(num % 1000 / 100)
shi = int(num % 100 / 10)
ge = int(num % 10)

str_qian = int2roman(qian,'M','','')
str_bai = int2roman(bai,'C','D','M')
str_shi = int2roman(shi,'X','L','C')
str_ge = int2roman(ge,'I','V','X')

print(str_qian+str_bai+str_shi+str_ge)

