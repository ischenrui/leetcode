# https://leetcode-cn.com/problems/3sum-closest/description/
nums = [1,1,1,0]
target = 100
nums.sort()

sum = 0
temp = 2147483647
print(nums)
for i in range(len(nums)-2):
    a = nums[i]
    rnums = nums[i+1:]
    i,j = 0,len(rnums)-1
    while(i<j):
        three_srum = a + rnums[i] + rnums[j]
        if target == three_srum:
            print('直接找到了')
        elif abs(target - three_srum) < temp:
            temp = abs(target - three_srum)
            sum = three_srum
        if target - three_srum > 0 :
            i += 1
        else: j -= 1
print(sum)