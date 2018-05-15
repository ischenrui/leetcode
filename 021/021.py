# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#---测试数据初始化---
l1list = [1,2,4,5,6]
l2list = [1,3,4]

list1head = ListNode(None)
list2head = ListNode(None)

p1 = list1head
for node in l1list:
    p1.next = ListNode(node)
    p1 = p1.next

p2 = list2head
for node in l2list:
    p2.next = ListNode(node)
    p2 = p2.next

p = list1head
while p.next:
    p = p.next
    print(p.val)
p = list2head
while p.next:
    p = p.next
    print(p.val)

#---把list2剪切到list1中
p1 = list1head.next
p2 = list2head.next
p3 = list1head
while p1 and p2:
    if p1.val == p2.val:
        p3.next = p1
        p1 = p1.next
        p3 = p3.next
        p3.next = p2
        p2 = p2.next
        p3 = p3.next
        p3.next = None
    elif p1.val < p2.val:
        p3.next = p1
        p1 = p1.next
        p3 = p3.next
        p3.next = None
    elif p1.val > p2.val:
        p3.next = p2
        p2 = p2.next
        p3 = p3.next
        p3.next = None

if p1:
    p3.next = p1
else:p3.next = p2

p = list1head
while p.next:
    p = p.next
    print(p.val)