# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
digits = "23"

dicD = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz',}
outlist = []
def funP(s,digits,outlist):
    if digits == '':
        outlist.append(s)

    else:
        nows = dicD[digits[0]]
        for node in nows:
            ss = s+node
            funP(ss,digits[1:],outlist)

funP("",digits,outlist)
print(outlist)