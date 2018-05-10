# https://leetcode-cn.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = ListNode(0)
        p1.next = l1
        p2 = ListNode(0)
        p2.next = l2

        l3 = ListNode(0)
        ptr = l3
        flag = 0
        while p1.next and p2.next:
            p1 = p1.next
            p2 = p2.next
            sum = p1.val + p2.val

            if flag == 1:
                sum += 1
            flag = 0

            addnum = 0
            if sum < 10:
                addnum = sum
            else:
                addnum = sum - 10
                flag = 1

            ptr.next = ListNode(addnum)
            ptr = ptr.next

        while p1.next:
            p1 = p1.next

            sum = p1.val
            if flag == 1:
                sum += 1
            flag = 0

            addnum = 0
            if sum < 10:
                addnum = sum
            else:
                addnum = sum - 10
                flag = 1

            ptr.next = ListNode(addnum)
            ptr = ptr.next

        while p2.next:
            p2 = p2.next

            sum = p2.val
            if flag == 1:
                sum += 1
            flag = 0

            addnum = 0
            if sum < 10:
                addnum = sum
            else:
                addnum = sum - 10
                flag = 1

            ptr.next = ListNode(addnum)
            ptr = ptr.next

        if not (p1.next or p2.next) and flag == 1:
            ptr.next = ListNode(1)
            ptr = ptr.next

        # while l3.next:
        #     print(l3.val)
        #     l3 = l3.next

        return l3.next





