"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l1_cur = l1
        l2_cur = l2
        newlist = ListNode(0,None)
        newlist_cur = newlist
        at_end = False
        while True:
            sum = l1_cur.val + l2_cur.val + carry
            carry = 0
            if sum >= 10:
                sum -= 10
                carry = 1
            newlist_cur.val = sum
            if l1_cur.next == None:
                self.addList(newlist_cur, l2_cur.next, carry)
                return newlist
            elif l2_cur.next == None:
                self.addList(newlist_cur, l1_cur.next, carry)
                return newlist
            else:
                l1_cur = l1_cur.next
                l2_cur = l2_cur.next
                newlist_cur.next = ListNode(0, None)
                newlist_cur = newlist_cur.next
    
    def addList(self, list_start, list_to_add, carry):
        curlist = list_start
        curlist_add = list_to_add
        if curlist_add is None:
            if carry == 1:
                curlist.next = ListNode(1,None)
            return
        while True:
            if carry == 0:
                curlist.next = curlist_add
                return
            else:
                sum = curlist_add.val + carry
                carry = 0
                if sum >= 10:
                    carry = 1
                    sum -= 10
                curlist.next = ListNode(sum, None)
                curlist = curlist.next
                if curlist_add.next is None and carry == 1:
                    curlist.next = ListNode(1, None)
                    return
                elif curlist_add.next is None:
                    return
                curlist_add = curlist_add.next

list1 = ListNode(9,None)
cur = list1
for i in range(3):
    cur.next = ListNode(9,None)
    cur = cur.next

list2 = ListNode(9,None)
cur = list2
for i in range(4):
    cur.next = ListNode(9,None)
    cur = cur.next

s = Solution()
res1 = s.addTwoNumbers(list1, list2)
res2 = s.addTwoNumbers(list2, list1)

while res1 is not None:
    print(res1.val)
    res1 = res1.next

while res2 is not None:
    print(res2.val)
    res2 = res2.next