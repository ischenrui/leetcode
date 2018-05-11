# https://leetcode-cn.com/problems/longest-common-prefix/description/

strs = ["flower","flow","flight"]

same_str = ''
temp_s = ''
i = 0
try:
    while(1):
        temp_s = strs[0][i]
        for node in strs:
            if not node[i]==temp_s:print(same_str)
        same_str+=temp_s
        i+=1
except:
    print(same_str)