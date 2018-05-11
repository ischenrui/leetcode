# https://leetcode-cn.com/problems/3sum/description/

nums = [1,2,-2,-1]

nums.sort()




def getOpposite_nums(num,nums):
    a,b = -1,-1
    relist = []
    sum = -num
    i,j = 0 , len(nums)-1
    while(i<j):
        if nums[i]+nums[j]==sum:
            if not(nums[i]==a and nums[j]==b):
                relist.append([nums[i],nums[j]])
            a = nums[i]
            b = nums[j]
            i+=1
            j-=1
        elif nums[i]+nums[j]>sum:
            j-=1
        else:
            i+=1
    return relist

sum3list = []
temp = 1
for i in range(len(nums)-2):
    if nums[i]<=0 and not nums[i]==temp:
        relist = getOpposite_nums(nums[i],nums[i+1:])
        temp = nums[i]
        if relist:
            for node in relist:
                node.append(nums[i])
                sum3list.append(node)
print(sum3list)