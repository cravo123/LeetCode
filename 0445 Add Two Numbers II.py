# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, node):
        prev, curr = None, node
        while curr:
            p = curr.next
            curr.next = prev
            prev = curr
            curr = p    
        return prev
    
    def merge(self, p, q):
        dummy = curr = ListNode(0)
        
        carry = 0
        while p or q or carry:
            if p:
                carry += p.val
                p = p.next
            if q:
                carry += q.val
                q = q.next
            carry, v = divmod(carry, 10)
            curr.next = ListNode(v)
            curr = curr.next
        
        return dummy.next
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2 = self.reverse(l1), self.reverse(l2)
        
        res = self.merge(l1, l2)
        
        res = self.reverse(res)
        
        return res