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
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = p = q = ListNode(0)
        dummy.next = head
        
        while p.next:
            if p.next.val != 9:
                q = p.next
            p = p.next
        
        if p.val != 9:
            p.val += 1
            return dummy.next
        else:
            q.val += 1
            q = q.next
            while q:
                q.val = 0
                q = q.next
            return dummy if dummy.val > 0 else dummy.next