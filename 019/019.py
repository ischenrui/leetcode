# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

L = ListNode(None)


p = L
for i in range(1,6):
    p.next = ListNode(i)
    p = p.next

p = L
while p.next:
    p = p.next
    print(p.val)

n = 2
#---算法---
# if head.next is None and n==1:
#             return None
a,b = L,L
for i in range(n-1):
    b = b.next
while b.next.next:
    a = a.next
    b = b.next
print(a.val,b.val)
#删除a后面的结点
a.next = a.next.next
#------
p = L
while p.next:
    p = p.next
    print(p.val)


