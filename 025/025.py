# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#---测试数据初始化---
l1list = [1,2,3]
n = 2
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
def reverse(head,n):
    counter = 0
    tail = head.next
    headnode = ListNode(None)
    p = head.next
    while counter<n:
        tempnode = p
        p = p.next
        tempnode.next = headnode.next
        headnode.next = tempnode
        counter += 1
    tail.next = p
    head.next = headnode.next

    return (head,tail)


#


p1 = list1head
while p1:
    startp = p1
    i = 0
    while i < n and p1:
        i+=1
        p1 = p1.next
    if i==n and not(p1 is None):
        result = reverse(startp,n)
        p1 = result[1]
    else:
        break



pout = list1head
while pout.next:
    pout=pout.next
    print(pout.val)

