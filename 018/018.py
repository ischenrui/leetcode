# https://leetcode-cn.com/problems/4sum/description/

nums = [1,-5,1,-4,2,1,-3]
target = 1
nums.sort()
def getsum3list(target,nums):
    nums.sort()

    def getOpposite_nums(num, nums):
        a, b = -1, -1
        relist = []
        sum = -num + target
        i, j = 0, len(nums) - 1
        while (i < j):
            if nums[i] + nums[j] == sum:
                if not (nums[i] == a and nums[j] == b):
                    relist.append([nums[i], nums[j]])
                a = nums[i]
                b = nums[j]
                i += 1
                j -= 1
            elif nums[i] + nums[j] > sum:
                j -= 1
            else:
                i += 1
        return relist

    sum3list = []
    temp = 2147483647
    for i in range(len(nums) - 2):
        if not nums[i] == temp:
            relist = getOpposite_nums(nums[i], nums[i + 1:])
            temp = nums[i]
            if relist:
                for node in relist:
                    node.append(nums[i])
                    sum3list.append(node)
    return sum3list

sum4list = []
temp = 2147483647
for i in range(len(nums) - 3):
    if not nums[i] == temp:
        temp = nums[i]
        sum3target = target - nums[i]
        sum3list = getsum3list(sum3target, nums[i+1:])
        if sum3list:
            for node in sum3list:
                node.append(nums[i])
                sum4list.append(node)
print(sum4list)