# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#---测试数据初始化---
l1list = [1,4,5]
l2list = []
l3list = []

list1head = ListNode(None)
list2head = ListNode(None)
list3head = ListNode(None)

p1 = list1head
for node in l1list:
    p1.next = ListNode(node)
    p1 = p1.next

p2 = list2head
for node in l2list:
    p2.next = ListNode(node)
    p2 = p2.next

p3 = list3head
for node in l3list:
    p3.next = ListNode(node)
    p3 = p3.next

lists = [list1head.next,list2head.next,list3head.next]


#---算法部分
r = cur = ListNode(0)
# for node in lists:
#     print(node.val)

for i in range(len(lists)-1, -1, -1):
    if lists[i] is None:
        lists.remove(lists[i])

for node in lists:
    print(node.val)

while len(lists)>1:
    nums = []
    for node in lists:
        nums.append(node.val)
    minnum = min(nums)
    index = nums.index(minnum)
    p = lists[index]

    cur.next = p
    cur = cur.next
    lists[index] = p.next

    if lists[index] is None:
        lists.pop(index)

if len(lists)==1:
    cur.next = lists[0]
while r.next:
    r=r.next
    print(r.val)

#---最优解答（没有链接原有节点）
# class Solution:
#     def mergeKLists(self, lists):
#         l = []
#         res = head = ListNode(0)
#         for node in lists:
#             while node:
#                 l.append(node.val)
#                 node = node.next
#         l.sort()
#         for i in l:
#             head.next = ListNode(i)
#             head = head.next
#         return res.next
#
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """