# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#---测试数据初始化---
l1list = [1,2,3,4,5,6]
list1head = ListNode(None)
p1 = list1head
for node in l1list:
    p1.next = ListNode(node)
    p1 = p1.next

# p1 = list1head
# while p1.next:
#     p1=p1.next
#     print(p1.val)
#---算法部分---
if list1head.next is None:
    print('None')
elif list1head.next.next is None:
    print(list1head.next)
else:
    p1 = list1head.next
    p2 = list1head.next.next
p = list1head

while p2:
    p2 = p2.next
    p.next = p1.next
    p1.next.next = p1
    p = p1
    p.next = p2
    p1 = p2
    if p1 is None:
        break
    p2 = p1.next

p1 = list1head
while p1.next:
    p1=p1.next
    print(p1.val)


