str = '   -with words'

str = str.strip()
rs = ''
#符号判断
flag = 0
if str[0] == '+':str = str[1:]
elif str[0] == '-':
    flag = 1
    str = str[1:]

#首字符判断
i = 0
while (str[i].isdigit()):
    rs += str[i]
    i += 1
if rs == "":print(0)
if int(rs)<-2147483648:print(-2147483648)
elif int(rs)>2147483647:print(2147483647)
else:print(int(rs))
