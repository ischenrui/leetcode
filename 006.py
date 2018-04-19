s = "PAYPALISHIRING"
numRows = 2

if numRows == 1:print(s)
numDic = {}
for i in range(numRows):
    numDic[i]= []

for index,item in enumerate(s):
    n = index%(2*numRows-2)
    if n < numRows: numDic[n%numRows].append(item)
    else:numDic[(numRows-2)-n%numRows].append(item)
print(numDic)
outs = ""
for value in numDic.values():
    outs +="".join(value)
print(outs)
