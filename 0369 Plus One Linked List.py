# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, reverse -> add one -> reverse
class Solution:
    def reverse(self, node):
        prev, curr = None, node
        while curr:
            p = curr.next
            curr.next = prev
            prev = curr
            curr = p
        return prev
    
    def plusOne(self, head: ListNode) -> ListNode:
        if head is None:
            return ListNode(1)
        
        p = self.reverse(head)
        
        curr = p
        carry = 1
        
        prev = None
        while curr:
            carry += curr.val
            carry, val = divmod(carry, 10)
            curr.val = val
            prev, curr = curr, curr.next
        if carry:
            prev.next = ListNode(carry)
        
        res = self.reverse(p)
        
        return res

# Solution 2, find the last non-9 node, and add
# first point to the node where it is the last node whose value is not 9
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = first = ListNode(0)
        dummy.next = head
        
        curr = dummy
        while curr.next:
            if curr.next.val != 9:
                first = curr.next
            curr = curr.next
        
        if curr.val != 9:
            curr.val += 1
            return head
        
        first.val += 1
        
        first = first.next
        while first:
            first.val = 0
            first = first.next
        
        return dummy.next if dummy.val == 0 else dummy