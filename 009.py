x =0
s = str(x)

for i in range(0, int(len(s) / 2)):
    if not s[i]==s[len(s)-1-i]:
        print("zhongzhi")
print("duicheng")
