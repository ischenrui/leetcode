# https://leetcode-cn.com/problems/remove-element/description/
nums = [0,1,2,2,3,0,4,2]
val = 2

i = 0
while i<len(nums):
    if nums[i]==val:
        j = i+1
        flag = 0
        while j<len(nums):
            if nums[j]==val:
                j+=1
            else:
                nums[i] = nums[j]
                nums[j] = val
                flag = 1
                break
        if flag==0:
            break
    i+=1
print(i)
print(nums)
