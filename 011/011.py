# https://leetcode-cn.com/problems/container-with-most-water/description/
height = [2,1,4,4,3,1,2]

i = 0
j = len(height)-1

maxC = min(height[i],height[j])*(j-i)
while(i<j):
    c = min(height[i], height[j]) * (j - i)
    if c > maxC: maxC = c
    if height[i]<height[j]:
        i += 1
    else:
        j -= 1

print(maxC)
