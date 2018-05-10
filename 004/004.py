# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
nums1 = [1,4,7,9]
nums2 = [2,3]

INT_MAX = 2147483647
INT_MIN = -INT_MAX-1

n = len(nums1)
m = len(nums2)
# if (n>m): return findMedianSortedArrays(nums2 ,nums1)   #保证数组1一定最短
L1,L2,R1,R2,c1,c2,lo = 0,0,0,0,0,0,0 #//我们目前是虚拟加了'#'所以数组1是2*n长度
hi = 2*n
while(lo <= hi): #二分
    c1 = int((lo+hi)/2)
    if 2*m>=m+n-c1:
        c2 = m + n - c1
    L1 = INT_MIN if c1 == 0 else nums1[int((c1-1)/2)]
    R1 = INT_MAX if c1 == 2*n else nums1[int(c1/2)]
    L2 = INT_MIN if c2 == 0 else nums2[int((c2-1)/2)]
    R2 = INT_MAX if c2 == 2*m else nums2[int(c2/2)]

    if(L1 > R2):
        hi = c1 - 1
    elif L2 >R1:
        lo = c1 + 1
    else:break
print((max(L1,L2)+ min(R1,R2))/2.0)
#https://blog.csdn.net/hk2291976/article/details/51107778  其中有错误，已改正

"""

l1 = (nums1 + nums2)
        l1.sort()
        lenth = len(l1)
        if  lenth == 1:
            return float(l1[0])
        elif lenth%2 !=0 :
            return float(l1[lenth//2])
        else:
            return (l1[lenth//2]+l1[lenth//2-1])/2
"""
