# https://leetcode-cn.com/problems/valid-parentheses/description/

s = "["
templist = []   #用于符号入栈
for node in s:
    try:
        if node == '(' or node == '{' or node == '[':
            templist.append(node)
        elif node==')' and  not templist.pop(-1)=='(':
            print('结束（')
        elif node=='}' and  not templist.pop(-1)=='{':
            print('结束}')
        elif node == ']' and not templist.pop(-1) == '[':
            print('结束[')
    except:
        print('栈为空')

if not templist:
    print('ok')