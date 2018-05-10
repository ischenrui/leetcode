# s = "ab"
# p = ".*"
#
s = "aaa"
p = "a.a"

""" 理解错题意，以为是在p中找到匹配s的子串即可
for i in range(len(p)):
    k = 0
    if p[i]=='*':continue
    for j in range(len(s)):
        if i+k<len(p): item = p[i+k]
        else: break

        if item == '.' or item==s[j]: k += 1
        elif item == '*' and (p[i+k-1] == '.' or p[i+k-1]==s[j]): k = k
        elif i+k+1 < len(p) and item == '*' and (p[i+k+1] == '.' or p[i+k+1]==s[j]): k += 2
        else:break
        if j==len(s)-1 and i+k==len(p)-1:print("匹配")
"""


""" 思路不可行
s += '+'
p += '+'
i,j = 0, 0
while(i<len(s) or j<len(p)):
    if s[i]==p[j] or (p[j]=='.' and not s[i]=='+'):
        i+=1
        j+=1
    elif p[j] == '*' :
        if not s[i]=='+' and (p[j - 1] == s[i] or p[j - 1] == '.'):
            i+=1
        else:
            j+=1
    elif j+1<len(p) and p[j+1] == '*':
        j+=2
    else:
        print('不匹配！')
        break

if i==len(s) and j==len(p):
    print('匹配')
else:print('不匹配')
"""

"""还是错误
def check(ta,tp):
    if ta[0]==tp[0] or tp[0]=='.':
        if tp[1]=='=' and ta[1]==tp[2]:return True
        elif tp[1]=='*' and ta[1]>=tp[2]:return True
        else:return False
    else:return False

def sumNode(p1,p2):
    one = p1[0] if p2[0]=='.' else p2[0]
    two = ''
    if p1[1]=='=' and p2[1]=='=':
        two = '='
    else:
        two = '*'
    three = p1[2] + p2[2]
    return (one,two,three)
#----初始化slist----
lists = []
if not s=="":
    temp = s[0]
    sum = 1
    for i in range(1,len(s)):
        if s[i] == temp: sum+=1
        else:
            lists.append((temp,sum))
            temp = s[i]
            sum = 1
    lists.append((temp,sum))
print(lists)
#----初始化plist----
listp = []
if not p=='':
    p+='++'
    temp = p[0]
    sum = 0 if p[1]=='*' else 1
    flag = 0
    for i in range(1,len(p)-1):
        if p[i]==temp and not p[i+1]=='*':sum+=1
        elif p[i]=='*':flag=1
        elif not p[i]==temp:
            if flag==0:listp.append((temp,'=',sum))
            else:listp.append((temp,'*',sum))
            temp = p[i]
            sum = 0 if p[i+1]=='*' else 1
            flag = 0
print(listp)
#---为空判断----
if not lists and not listp:print('匹配')
if not lists:
    for node in listp:
        if node[1]=='=':print('不匹配')
    else:print('匹配')
if not listp:
    print('不匹配')
#---匹配----
i,j = 0, 0
lists.append(('end',1))
listp.append(('end','=',1))

while(i<len(lists)-1 and j<len(listp)-1):
    if lists[i][0] == listp[j][0] :
        if check(lists[i],listp[j]):
            i+=1
            j+=1
        elif listp[j+1][0]=='.':
            if check(lists[i],sumNode(listp[j],listp[j+1])):
                i+=1
                j+=2
            else:
                print("不匹配")
                break
        else:
            print("不匹配")
            break
    elif listp[j][0] == '.':
        if listp[j+1][0] == lists[i][0]:
            if check(lists[i],sumNode(listp[j],listp[j+1])):
                i+=1
                j+=2
            elif j-1>=0 and check(lists[i],sumNode(listp[j],listp[j-1])):
                j+=1
            else:
                print('不匹配')
                break
        # elif check(lists[i],listp[j]):
        #     i+=1
        #     j+=1
        else:
            if not (listp[j+1][0] == 'end'):
                kk = i
                sumkk = 0
                while (not listp[j+1][0] == lists[kk][0]) and kk<len(lists)-1:
                    sumkk +=lists[kk][1]
                    kk+=1
                if (listp[j][1] == '*' and sumkk>=listp[j][2]) or (listp[j][1] == '=' and listp[j][2] == sumkk):
                    i=kk
                    j+=1
                else:
                    print("不匹配")
                    break
            else:
                sumkk = 0
                kk = i
                while kk<len(lists)-1:
                    sumkk += lists[kk][1]
                    kk+=1
                if (listp[j][1] == '*' and sumkk>=listp[j][2]) or (listp[j][1] == '=' and listp[j][2] == sumkk):
                    i=kk
                    j+=1
                else:
                    print("不匹配")
                    break


    elif not lists[i][0] == listp[j][0]:
        if listp[j][1] == '*' and listp[j][2]==0:
            j+=1
        else:
            print('不匹配')
            break
if i==len(lists)-1 and j==len(listp)-1:
    print('匹配')
"""



