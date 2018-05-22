# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/
nums = [0,0,1,1,1,2,2,3,3,4]
MAXINT = 2147483647
i,j = 0,1

while j < len(nums):
    if nums[i]==nums[j]:
        j+=1
    else:
        i+=1
        nums[i] = nums[j]
        j+=1
print(i)
print(nums)